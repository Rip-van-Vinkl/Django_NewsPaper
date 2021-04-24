# Generated by Django 3.2 on 2021-04-23 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djangonewspaper', '0004_auto_20210423_0201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_rating', models.IntegerField(default=0)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField()),
                ('comment_datetime', models.DateTimeField(auto_now_add=True)),
                ('comment_rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_type', models.CharField(choices=[('NW', 'news'), ('AR', 'articles')], max_length=2)),
                ('post_datetime', models.DateTimeField(auto_now_add=True)),
                ('post_title', models.CharField(max_length=255)),
                ('post_text', models.TextField()),
                ('post_rating', models.IntegerField(default=0.0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangonewspaper.author')),
            ],
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='category',
            field=models.CharField(default='...', max_length=40, unique=True),
        ),
        migrations.DeleteModel(
            name='Good',
        ),
        migrations.AddField(
            model_name='postcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangonewspaper.category'),
        ),
        migrations.AddField(
            model_name='postcategory',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangonewspaper.post'),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(through='djangonewspaper.PostCategory', to='djangonewspaper.Category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangonewspaper.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]