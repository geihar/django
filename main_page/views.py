from django.shortcuts import render, get_object_or_404
from .models import News, AsideNews,MainNews, Biografi
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User


# def main_page(request):
#     data = {'aside': AsideNews.objects.order_by("text")[:4]}
#     return render(request, 'main_page/home.html', data)


class ShowMainView(ListView):
    model = MainNews
    template_name = 'main_page/home.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 3

    def get_context_data(self, **kwards):
        context = super(ShowMainView, self).get_context_data(**kwards)
        context['aside'] = AsideNews.objects.order_by("url")[:4]
        context['bio'] = Biografi.objects.order_by("-date")[:3]
        context['title'] = 'Главная страница '
        return context


class BioDetailView(DetailView):
    model = Biografi
    template_name = 'main_page/news_detail.html'

    def get_context_data(self, **kwards):
        context = super(BioDetailView, self).get_context_data(**kwards)
        context['title'] = Biografi.objects.filter(pk=self.kwargs['pk']).first()
        context['aside'] = AsideNews.objects.order_by("title")[:3]
        return context

class MainNewsDetailView(DetailView):
    model = MainNews
    template_name = 'main_page/news_detail.html'

    def get_context_data(self, **kwards):
        context = super(MainNewsDetailView, self).get_context_data(**kwards)
        context['title'] = MainNews.objects.filter(pk=self.kwargs['pk']).first()
        context['aside'] = AsideNews.objects.order_by("title")[:3]
        return context


class ShowNewsView(ListView):
    model = News
    template_name = 'main_page/news.html'
    context_object_name = 'news'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, **kwards):
        context = super(ShowNewsView, self).get_context_data(**kwards)
        context['aside'] = AsideNews.objects.order_by("url")[:3]
        context['title'] = 'Главная страница блога'
        return context


class ShowUserNews(ListView):
    model = News
    template_name = 'main_page/user_news.html'
    context_object_name = 'news'
    paginate_by = 5

    def get_context_data(self, **kwards):
        context = super(ShowUserNews, self).get_context_data(**kwards)
        context['title'] = 'Новости пользователя'
        context['aside'] = AsideNews.objects.order_by("autor")[:3]
        return context

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(autor=user).order_by('-date')


class NewsDetailView(DetailView):
    model = News

    def get_context_data(self, **kwards):
        context = super(NewsDetailView, self).get_context_data(**kwards)
        context['title'] = News.objects.filter(pk=self.kwargs['pk']).first()
        context['aside'] = AsideNews.objects.order_by("title")[:3]
        return context


class CreateNewsView(LoginRequiredMixin, CreateView):
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = News
    fields = ['title', 'text']

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False


class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    success_url = '/'

    def test_func(self):
        news = self.get_object()
        if self.request.user == news.autor:
            return True
        return False

