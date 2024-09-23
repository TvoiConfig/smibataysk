# Generated by Django 5.1.1 on 2024-09-23 11:52

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_stream_video'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='timeposted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='message',
            field=models.CharField(max_length=150, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='record',
            name='name',
            field=models.CharField(max_length=50, verbose_name='ФИО'),
        ),
        migrations.AlterField(
            model_name='record',
            name='number',
            field=models.CharField(max_length=15, verbose_name='Номер телефона'),
        ),
    ]