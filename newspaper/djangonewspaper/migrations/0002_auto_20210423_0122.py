# Generated by Django 3.2 on 2021-04-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangonewspaper', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
