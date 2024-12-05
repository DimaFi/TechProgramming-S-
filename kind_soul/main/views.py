from django.shortcuts import render
from .models import News
from .models import Animal

# forum
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Topic, Comment
from django.core.paginator import Paginator

from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic = self.object
        comments = topic.comments.all()

        # Пагинация комментариев
        paginator = Paginator(comments, 3)  # Показывать по 10 комментариев на странице
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['comment_form'] = CommentForm()  # Форма для добавления комментария
        return context

    def post(self, request, *args, **kwargs):
        topic = self.get_object()  # Получаем объект темы
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.topic = topic
            comment.save()
            return self.get(request, *args, **kwargs)  # Перезагружаем страницу с комментариями

        # В случае ошибки возвращаем страницу с ошибкой
        context = self.get_context_data()
        context['comment_form'] = form
        return self.render_to_response(context)
    
    
    
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
    template_name = 'main/forum/topic_comments.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.topic_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('topic-detail', kwargs={'pk': self.kwargs['pk']})
    
def topic_list(request):
    topics = Topic.objects.all()
    total_comments = Comment.objects.count()
    active_users = User.objects.filter(is_active=True).count()
    
    context = {
        'topics': topics,
        'total_comments': total_comments,
        'active_users': active_users,
    }
    return render(request, 'forum/topic_list.html', context)


# класс-представление для отображения всех комментариев для данной темы
class TopicCommentsView(DetailView):
    model = Topic
    template_name = 'main/forum/topic_comments.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = context['topic'].comments.all()  # Все комментарии
        return context