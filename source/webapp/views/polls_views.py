from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse, reverse_lazy

from webapp.models import Poll
from webapp.forms import PollForm


class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'polls'
    paginate_by = 5
    paginate_orphans = 0

    def get_queryset(self):
        return Poll.objects.all().order_by('-created_at')


class PollView(DetailView):
    template_name = 'polls/view.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object
        choices = poll.choices.order_by('choice_text')
        context['choices'] = choices
        return context


class PollCreateView(CreateView):
    model = Poll
    template_name = 'polls/create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'polls/update.html'
    form_class = PollForm
    context_key = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'polls/delete.html'
    model = Poll
    context_object_name = 'poll'
    success_url = reverse_lazy('index')
