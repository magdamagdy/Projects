# Generated by Django 3.1.5 on 2021-01-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rating_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='category',
            field=models.CharField(default=0, max_length=70),
            preserve_default=False,
        ),
    ]
