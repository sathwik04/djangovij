# Generated by Django 2.1.5 on 2020-05-21 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cycle', '0017_auto_20200516_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='phone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='cycle.Customer'),
        ),
    ]
