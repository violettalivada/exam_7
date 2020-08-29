from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.models import Poll, Choice
from webapp.forms import ChoiceForm


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'choices/create.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = form.save(commit=False)
        choice.poll = poll
        choice.save()
        return redirect('poll_view', pk=poll.pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choices/update.html'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    template_name = 'choices/delete.html'
    model = Choice
    context_object_name = 'choice'
    success_url = reverse_lazy('index')

