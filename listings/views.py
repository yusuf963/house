from webbrowser import get
from django.shortcuts import (render, get_object_or_404)
from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from .models import Listing


def index(request):
    listings = Listing.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': paged_listings
    }
    return render(request, 'templates/listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'templates/listings/listing.html', context)


def search(request):
    return render(request, 'templates/listings/search.html')
