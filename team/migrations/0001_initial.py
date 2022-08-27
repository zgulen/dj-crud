# Generated by Django 4.1 on 2022-08-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Full Name')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=154, null=True, unique=True)),
                ('gender', models.CharField(choices=[('1', 'Female'), ('2', 'Male'), ('3', 'Other'), ('4', 'Prefer Not Say')], max_length=50)),
                ('number', models.IntegerField(blank=True, null=True, unique=True)),
                ('path', models.CharField(choices=[('1', 'Front-end'), ('2', 'Back-end'), ('3', 'AWS-DevOps'), ('4', 'Data-Science')], max_length=20)),
            ],
        ),
    ]
