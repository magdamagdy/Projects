# Generated by Django 3.1.5 on 2021-01-11 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_reviews_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
