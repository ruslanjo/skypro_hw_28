# Generated by Django 4.1.1 on 2022-10-04 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_categories_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ads', to='ads.categories'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
