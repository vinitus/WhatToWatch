# Generated by Django 3.2.6 on 2022-11-16 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
            ],
        ),
    ]
