from django.shortcuts import render

# Create your views here.

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Play


class PlayListView(ListView):
    template_name = "play/play-list.html"
    model = Play


class PlayDetailView(DetailView):
    template_name = "play/play-detail.html"
    model = Play


class PlayCreateView(CreateView):
    template_name = "play/play-create.html"
    model = Play
    fields = ['name','purchaser','desc','img']


class PlayUpdateView(UpdateView):
    template_name = "play/play-update.html"
    model = Play
    fields = ['name','purchaser','desc','img']


class PlayDeleteView(DeleteView):
    template_name = "play/play-delete.html"
    model = Play
    success_url = reverse_lazy("play_list")
