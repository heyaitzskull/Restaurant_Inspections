from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Restaurant
from django.urls import reverse

# Create your views here.
def chicago(request):

    # If coming from the home "Chicago" button via POST, redirect to clean GET list
    if request.method == "POST":
        return redirect(reverse('restaurants:chi'))

    query = request.GET.get("q", "").strip()

    qs = Restaurant.objects.order_by('aka_name')
    if query:
        qs = qs.filter(aka_name__icontains=query)

    paginator = Paginator(qs, 15)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "q": query,  # for keeping the box filled and preserving in links
    }
    return render(request, 'chicago-list.html', context)

def chi_rest(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)
    return render(request, 'chi-restaurant.html', {"restaurant": restaurant})