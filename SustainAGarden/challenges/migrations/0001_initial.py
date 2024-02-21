# Generated by Django 4.1 on 2024-02-21 17:14

# Generated by Django 4.1.2 on 2024-02-18 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('coins', models.IntegerField(default=0)),
                ('completed_challenges', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('challenge_ID', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('coins', models.IntegerField()),
                ('challenge_setter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenges.user')),
            ],
        ),
    ]
