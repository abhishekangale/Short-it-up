# Generated by Django 3.1.4 on 2021-01-01 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0003_auto_20201229_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='longtoshort',
            name='city',
            field=models.CharField(default='India', max_length=25),
        ),
        migrations.AddField(
            model_name='longtoshort',
            name='lat',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='longtoshort',
            name='long',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=8),
        ),
    ]