# Generated by Django 2.0.7 on 2019-01-24 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='email',
            field=models.CharField(default=True, max_length=20),
            preserve_default=False,
        ),
    ]