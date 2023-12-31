# Generated by Django 4.2.7 on 2023-12-05 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('money', models.PositiveIntegerField(verbose_name='Желаемая зарплата')),
                ('skills', models.TextField(help_text='Напиши все что умеешь', verbose_name='Навыки')),
                ('education', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Образование')),
                ('registered_in', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='работодатель')),
                ('position', models.CharField(max_length=128, verbose_name='должность')),
                ('duty', models.TextField(blank=True, null=True, verbose_name='Обязанности')),
                ('started_in', models.DateField(verbose_name='Начал работать')),
                ('finished_in', models.DateField(blank=True, null=True, verbose_name='Закончил работать')),
                ('registered_in', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('resume', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='slaves.resume', verbose_name='Резюме')),
            ],
        ),
    ]
