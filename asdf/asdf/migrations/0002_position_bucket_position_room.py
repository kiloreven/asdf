# Generated by Django 5.0.8 on 2024-08-06 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asdf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='bucket',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='position',
            name='room',
            field=models.CharField(default='placeolder', max_length=64),
            preserve_default=False,
        ),
    ]
