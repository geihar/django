from django.shortcuts import render, get_object_or_404
from .models import News, AsideNews,MainNews, Biografi
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import NewsViewSerialaizers


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
        context['main'] = True
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
        context['new'] = True
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


class ApiNewsView(APIView):

    def get (self, request):
        news = News.objects.all()
        serializer = NewsViewSerialaizers(news, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NewsViewSerialaizers(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApiNewsDetailView(APIView):

    def get(self, request, pk):
        new =  get_object_or_404(News, pk=pk)
        serializer = NewsViewSerialaizers(new)
        return Response(serializer.data)

    def delete(self, request, pk):
        new = get_object_or_404(News, pk=pk)
        serializer = NewsViewSerialaizers(new)
        data = serializer.data
        new.delete()
        return Response(data)