# Generated by Django 2.2.6 on 2019-11-11 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_categoery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='categoery',
            new_name='category',
        ),
    ]
