# Generated by Django 3.1.7 on 2021-03-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gram', models.CharField(max_length=50)),
                ('today', models.CharField(max_length=50)),
                ('yesterday', models.CharField(max_length=50)),
                ('change', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pricesilver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sgram', models.CharField(max_length=50)),
                ('stoday', models.CharField(max_length=50)),
                ('syesterday', models.CharField(max_length=50)),
                ('schange', models.CharField(max_length=50)),
            ],
        ),
    ]
