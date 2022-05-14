# Generated by Django 4.0.4 on 2022-05-11 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_article_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Tytuł'),
        ),
    ]