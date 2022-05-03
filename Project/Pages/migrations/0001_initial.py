# Generated by Django 4.0.4 on 2022-04-30 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='Photos/Team')),
                ('facebook_link', models.URLField(max_length=100)),
                ('twitter_link', models.URLField(max_length=100)),
                ('gmail_link', models.URLField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
