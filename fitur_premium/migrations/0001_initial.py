# Generated by Django 4.2.6 on 2023-10-29 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fitur_premium',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('jumlah_hari', models.TextField(blank=True, null=True)),
                ('id_user', models.TextField(blank=True, null=True)),
            ],
        ),
    ]