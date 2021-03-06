# Generated by Django 2.0.7 on 2019-01-23 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20190123_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='email',
            field=models.EmailField(max_length=50, null='No email given'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
