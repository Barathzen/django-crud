# Generated by Django 4.1.13 on 2023-11-19 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='age',
            field=models.IntegerField(default=18),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='airplane_no',
            field=models.CharField(default=53221, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='from_destination',
            field=models.CharField(default='chennai', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phno',
            field=models.CharField(default=9334983474, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='seat_no',
            field=models.CharField(default=62, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='to_destination',
            field=models.CharField(default='Mumbai', max_length=255),
            preserve_default=False,
        ),
    ]
