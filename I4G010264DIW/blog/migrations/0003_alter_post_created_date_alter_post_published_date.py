# Generated by Django 4.0.5 on 2022-06-15 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_created_date_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Created_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='Published_date',
            field=models.DateTimeField(),
        ),
    ]
