# Generated by Django 3.0 on 2019-12-21 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_page', '0002_asidenews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asidenews',
            name='date',
        ),
        migrations.RemoveField(
            model_name='asidenews',
            name='img',
        ),
        migrations.AddField(
            model_name='asidenews',
            name='iframe',
            field=models.TextField(default='none'),
        ),
        migrations.AddField(
            model_name='asidenews',
            name='url',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='MainNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
