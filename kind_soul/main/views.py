from django.shortcuts import render
from .models import News
from .models import Animal

# forum
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Topic, Comment

def index_view(request):
    return render(request, 'main/index.html')


def news_view(request):
    news_list = News.objects.all().order_by('-date')
    return render(request, 'main/news.html', {'news_list': news_list})


def animals_view(request):
    animals = Animal.objects.prefetch_related('photos').all()  # Prefetch related photos
    return render(request, 'main/animals.html', {'animals': animals})


# forum

class TopicListView(ListView):
    model = Topic
    template_name = 'main/forum/topic_list.html'
    context_object_name = 'topics'

class TopicDetailView(DetailView):
    model = Topic
    template_name = 'main/forum/topic_detail.html'
    context_object_name = 'topic'

class TopicCreateView(LoginRequiredMixin, CreateView):
    model = Topic
    fields = ['title', 'description']
    template_name = 'main/forum/topic_form.html'
    success_url = reverse_lazy('topic-list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ['content']
    template_name = 'main/forum/comment_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('topic-detail', kwargs={'pk': self.kwargs['pk']})