# Generated by Django 2.0.7 on 2019-01-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='recommendations',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
