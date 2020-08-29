from django.shortcuts import redirect
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.core.paginator import Paginator
from django.urls import reverse, reverse_lazy

from webapp.models import Poll


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        return Poll.objects.all().order_by('-created_at')

