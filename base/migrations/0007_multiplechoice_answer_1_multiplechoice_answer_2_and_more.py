# Generated by Django 4.1.2 on 2022-10-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_multiplechoice_answer_1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoice',
            name='answer_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='answer_2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='answer_3',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='answer_4',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='multiplechoice',
            name='correct_answer',
            field=models.CharField(choices=[(1, '1. answer'), (2, '2. answer'), (3, '3. answer'), (4, '4. answer')], max_length=1, null=True),
        ),
    ]