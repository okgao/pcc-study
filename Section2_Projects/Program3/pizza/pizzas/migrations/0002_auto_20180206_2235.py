# Generated by Django 2.0 on 2018-02-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.TextField(),
        ),
    ]