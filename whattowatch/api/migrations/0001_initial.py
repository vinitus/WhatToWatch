# Generated by Django 3.2.6 on 2022-11-16 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('overview', models.TextField()),
                ('poster_path', models.TextField(null=True)),
                ('popularity', models.FloatField()),
                ('release_date', models.TextField()),
                ('runtime', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('backdrop_path', models.TextField()),
                ('original_language', models.TextField()),
                ('adult', models.BooleanField()),
                ('country', models.CharField(max_length=30)),
                ('belongs_to_collection', models.IntegerField(null=True)),
                ('genres', models.ManyToManyField(to='api.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
            ],
        ),
    ]
