# Generated by Django 4.2.1 on 2023-05-22 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]