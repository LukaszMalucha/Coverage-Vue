# Generated by Django 2.1.5 on 2020-03-09 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200309_1015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicmodel',
            name='topic_parent',
        ),
        migrations.AddField(
            model_name='topicmodel',
            name='topic_breadcrumb',
            field=models.TextField(default='Not Specified'),
        ),
    ]