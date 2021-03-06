# Generated by Django 2.1 on 2018-10-13 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181013_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]
