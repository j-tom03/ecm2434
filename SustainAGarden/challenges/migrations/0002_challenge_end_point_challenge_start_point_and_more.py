# Generated by Django 4.1 on 2024-02-28 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='end_point',
            field=models.CharField(default='000, 000, 000', max_length=200),
        ),
        migrations.AddField(
            model_name='challenge',
            name='start_point',
            field=models.CharField(default='000, 000, 000', max_length=200),
        ),
        migrations.AddField(
            model_name='challenge',
            name='transport',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='garden',
            field=models.CharField(default='0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000', max_length=160),
        ),
    ]
