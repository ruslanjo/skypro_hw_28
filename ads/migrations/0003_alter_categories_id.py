# Generated by Django 4.1.1 on 2022-10-04 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_alter_ads_options_alter_categories_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]