# Generated by Django 4.0.2 on 2022-05-14 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Halalan2022', '0006_user_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(max_length=50),
        ),
    ]
