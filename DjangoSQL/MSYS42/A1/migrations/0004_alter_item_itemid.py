# Generated by Django 4.2 on 2023-04-21 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('A1', '0003_item_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemid',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False, verbose_name=200),
        ),
    ]
