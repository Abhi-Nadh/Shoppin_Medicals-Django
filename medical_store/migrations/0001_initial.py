# Generated by Django 4.1.2 on 2023-05-31 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('medicine_description', models.CharField(max_length=300)),
                ('medicine_add_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
