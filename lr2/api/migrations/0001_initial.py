# Generated by Django 5.0.3 on 2024-03-06 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_url', models.CharField(default=None, null=True)),
                ('request_data', models.CharField(default=None, null=True)),
            ],
        ),
    ]