from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('full_news', kwargs={'pk': self.pk})


class AsideNews(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    iframe = models.TextField(default='none')
    url = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Боковые новости"


class MainNews(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    img = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Главные новости"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('full_news', kwargs={'pk': self.pk})


class Biografi(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    img = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Биографии"
        verbose_name_plural = "Биографии"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('full_news', kwargs={'pk': self.pk})


