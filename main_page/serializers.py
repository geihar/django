from rest_framework import serializers
from .models import News

class NewsViewSerialaizers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'title', 'text', 'date', 'autor'
