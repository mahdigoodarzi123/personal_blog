# Generated by Django 4.2.3 on 2023-07-05 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['created_time']},
        ),
    ]
