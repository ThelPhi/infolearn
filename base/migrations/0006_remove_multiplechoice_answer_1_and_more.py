# Generated by Django 4.1.2 on 2022-10-20 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_multiplechoice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='multiplechoice',
            name='answer_1',
        ),
        migrations.RemoveField(
            model_name='multiplechoice',
            name='checks',
        ),
    ]
