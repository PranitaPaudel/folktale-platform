# Generated by Django 4.2.3 on 2025-01-23 17:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='story_images/')),
                ('author', models.CharField(max_length=100)),
                ('culture', models.CharField(blank=True, max_length=100, null=True)),
                ('practices', models.TextField(blank=True, null=True)),
                ('date_association', models.BooleanField(default=False)),
                ('day', models.IntegerField(blank=True, null=True)),
                ('month', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
