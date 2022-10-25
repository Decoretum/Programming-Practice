# Generated by Django 4.0.2 on 2022-03-15 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('City', models.CharField(max_length=500)),
                ('Country', models.CharField(max_length=500)),
                ('Createdat', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='WaterBottle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SKU', models.CharField(max_length=500)),
                ('Brand', models.CharField(max_length=500)),
                ('Cost', models.CharField(max_length=500)),
                ('Size', models.CharField(max_length=500)),
                ('MouthSize', models.CharField(max_length=500)),
                ('Color', models.CharField(max_length=500)),
                ('Suppliedby', models.CharField(max_length=500)),
                ('CurrentQuantity', models.CharField(max_length=500)),
            ],
        ),
    ]
