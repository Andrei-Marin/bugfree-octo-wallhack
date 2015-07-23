from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Cards

class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_card_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Cards.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Cards
    template_name = 'cards/detail.html'

