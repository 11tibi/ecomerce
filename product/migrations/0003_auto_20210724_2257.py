# Generated by Django 3.2.4 on 2021-07-24 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_warranty'),
    ]

    operations = [
        migrations.AddField(
            model_name='specs',
            name='tag',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='specs',
            name='description',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='specs',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]