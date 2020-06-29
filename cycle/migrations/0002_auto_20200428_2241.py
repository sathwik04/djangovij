# Generated by Django 2.1.5 on 2020-04-28 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.AddField(
            model_name='order',
            name='works',
            field=models.CharField(choices=[('Dish washes', 'House Cleaning'), ('WaterCAn', 'Cooking'), ('Washroom Cleaning', 'Grocaries')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('ROOM RENT', 'Room Rent'), ('Maintance', 'Maintance')], max_length=200, null=True),
        ),
    ]
