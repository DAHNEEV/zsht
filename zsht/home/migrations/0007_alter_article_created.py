# Generated by Django 4.0.4 on 2022-05-14 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_article_author_alter_article_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(blank=True, verbose_name='Utworzone'),
        ),
    ]
