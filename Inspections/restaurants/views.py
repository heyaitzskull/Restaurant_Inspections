from django.shortcuts import render, get_object_or_404
from .models import Restaurant
from django.db.models import Min, Max, Value, TextField
from django.db.models.functions import Replace, Lower
from django.core.paginator import Paginator
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.http import require_GET


def chicago(request):
    name = request.GET.get("q", "").strip()
    address = request.GET.get("p", "").strip()

    restaurant_qs = Restaurant.objects.none()

    if name or address:
        filters = {}
        if name:
            filters['aka_name__icontains'] = name
        if address:
            filters['address__icontains'] = address

        # cleaning: lowercase, get rid of spaces (and commas in address)
        base_qs = (
            Restaurant.objects
            .filter(**filters)
            .annotate(
                aka_name_no_space=Replace(
                    'aka_name',
                    Value(" ", output_field=TextField()),
                    Value("", output_field=TextField()),
                    output_field=TextField()
                ),
                address_no_space=Replace(
                    'address',
                    Value(" ", output_field=TextField()),
                    Value("", output_field=TextField()),
                    output_field=TextField()
                )
            )
            .annotate(
                address_clean=Replace(
                    'address_no_space',
                    Value(",", output_field=TextField()),
                    Value("", output_field=TextField()),
                    output_field=TextField()
                ),
                aka_name_clean=Lower('aka_name_no_space', output_field=TextField()),
                address_clean_lower=Lower('address_clean', output_field=TextField())
            )
        )

        # grouping by the cleaned name+address and picking the smallest id so that
        # we don't have duplicates in the results to be displayed
        sub = (
            base_qs
            .values('aka_name_clean', 'address_clean_lower')
            .annotate(rep_id=Min('id'))
            .values_list('rep_id', flat=True)
        )

        restaurant_qs = Restaurant.objects.filter(id__in=sub).order_by('aka_name', 'address')

    paginator = Paginator(restaurant_qs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "restaurant": restaurant_qs,
        "q": name,
        "p": address,
    }
    return render(request, 'search.html', context)

def chi_rest(request, restaurant_id):

    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    restaurant_all = list(
        Restaurant.objects.filter(
            aka_name=restaurant.aka_name,
            address=restaurant.address,
            city=restaurant.city,
            state=restaurant.state
        ).order_by('-inspection_date')
    )

    context = {
        "restaurant": restaurant,
        "restaurant_all": restaurant_all,
    }


    return render(request, 'chi-restaurant.html', context)

def chi_map(request):

    restaurant_all_non_repeating = Restaurant.objects.values(
        # 'id', 'zip', 'lattitude', 'longitude', 'aka_name', 'dba_name' , 'results', 'inspection_date'
        'results' , 'zip', 'longitude', 'lattitude'
    ).annotate(
        latest_inspection=Max('inspection_date')
    )

    context = {
        'restaurants': restaurant_all_non_repeating,
    }
    # print("HELLOOOOOOOOOOOOO")
    # print("Context for chi_map first restaurant:", restaurant_all_non_repeating.order_by('aka_name').first())
     # Debugging line to check context

    return render(request, 'chi-map.html', context)


@require_GET
def restaurants_in_bounds(request):
    try:
        sw_lat = float(request.GET.get('southWestLat'))
        sw_lng = float(request.GET.get('southWestLng'))
        ne_lat = float(request.GET.get('northEastLat'))
        ne_lng = float(request.GET.get('northEastLng'))
    except (TypeError, ValueError):
        return JsonResponse({'error': 'Invalid or missing bounding box parameters'}, status=400)

    # Filter restaurants in bounding box and only with valid coordinates
    restaurants = Restaurant.objects.filter(
        lattitude__gte=sw_lat,
        lattitude__lte=ne_lat,
        longitude__gte=sw_lng,
        longitude__lte=ne_lng,
    ).values(
        'id', 'aka_name', 'address', 'results', 'inspection_date', 'lattitude', 'longitude'
    ).annotate(
        latest_inspection=Max('inspection_date')
    )[:500]  # limit results to avoid huge payload

    # Serialize queryset to list of dicts
    data = list(restaurants)

    return JsonResponse(data, safe=False)