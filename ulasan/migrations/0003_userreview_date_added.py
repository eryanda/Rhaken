# Generated by Django 4.2.6 on 2023-10-29 05:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ulasan', '0002_alter_userreview_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='userreview',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
