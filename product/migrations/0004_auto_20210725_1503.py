# Generated by Django 3.2.4 on 2021-07-25 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210724_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='desc',
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=100, null=True)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='product.product')),
            ],
        ),
    ]
