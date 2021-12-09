from django.db.models.expressions import OrderBy
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import ListView
from .filters import StyleFilter, HousingFilter
from django.views.generic.edit import CreateView
from .models import Housing, Style
import json
from .filters import *
from .models import *
from .forms import CommentForm


# Home Page


class IndexView(generic.TemplateView):
    template_name = 'app/index.html'

# Filtering


def FilterView(request):
    houses = Housing.objects.all()
    otherFilter = HousingFilter(request.GET, queryset=houses)
    housings = otherFilter.qs
    for i in housings:
        if i.housing_type == 'Town_House':
            i.housing_type = "Town House"

    style = Style.objects.all()
    style_filter = StyleFilter(request.GET, queryset=style)
    style_qs = style_filter.qs

    context = {'houses': houses, 'style': style,
               'style_filter': style_filter, 'style_qs': style_qs,
               'otherFilter': otherFilter, 'housings': housings,
               }

    return render(request, 'app/filter.html', context)


def PropertyView(request, name):
    property = Housing.objects.get(name=name)
    lat = property.lat
    long = property.long
    address = property.address
    # detail = Style.objects.get(name=property.id)
    detail = Style.objects.filter(name=property.id)
    amenities = Amenity.objects.filter(name=property.id)

    pics = Images.objects.get(name=property.id)
    reviews = Review.objects.filter(housing=property.id, active=True)
    #ratings = Review.objects.get(housing=property.id, active = True).rating
    sum = 0
    for x in reviews:
        sum += x.rating
    if(len(reviews) > 0):
        avg_rating = sum / len(reviews)
    else:
        avg_rating = "None"

    #reviews = review.filter(active=True)
    new_review = None

    if request.method == "POST":
        form = CommentForm(request.POST, initial={'housing': property})
        if form.is_valid():
            new_review = form.save()
            #new_review.review = review
            # new_review.save()
    else:
        form = CommentForm(initial={'housing': property})

    context = {'pics': pics, 'property': property, 'detail': detail, 'amenities': amenities, 'address': json.dumps(address), 'lateral': json.dumps(
        lat), 'longet': json.dumps(long), 'reviews': reviews, 'new_review': new_review, 'form': form, 'avg_rating': avg_rating}
    return render(request, 'app/property.html', context)


class MapView(CreateView):
    model = Housing
    fields = ['address']
    template_name = 'app/map.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1Ijoic2hpdmFtYW4iLCJhIjoiY2t2cHZjOTY2MmlodzJvbXRuOXMzMTRpNiJ9.8mKcr3_Z1IcZMKpO3VRC6A'
        #addresses = list(Housing.objects.values('lat', 'long'))
        addresses = list(Housing.objects.all())
        context['addresses'] = addresses
        context['address'] = Housing
        return context


def map_housing(request):

    return render(
        request,
        'app/map.html',
        {
            'addresses': Housing.objects.all(),
            'mapbox_access_token':
            'pk.eyJ1Ijoic2hpdmFtYW4iLCJhIjoiY2t2cHZjOTY2MmlodzJvbXRuOXMzMTRpNiJ9.8mKcr3_Z1IcZMKpO3VRC6A',
            'housing': Housing})


class AboutView(generic.TemplateView):
    template_name = 'app/about.html'


class HouseSearchView(ListView):
    model = Housing
    template_name = 'app/index.html'
    context_object_name = 'housing'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Housing.objects.filter(name__icontains=query).order_by('-created_at')


def search_housing(request):
    if request.method == "POST":
        searching = request.POST['searching']
        empty = (searching != "")
        if (searching != ""):
            housing = Housing.objects.filter(name__icontains=searching)
            return render(request, 'app/search.html', {'searching': searching, 'housing': housing, 'empty': empty})

        else:
            return render(request, 'app/indexnosearch.html', {})
