# Generated by Django 4.2 on 2023-05-12 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0010_remove_mustpay_opened_date_remove_mustpay_recipient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mustpay',
            name='name_and_lastname',
            field=models.CharField(max_length=200, unique=True, verbose_name='Bergidaryň ady we familiýasy:'),
        ),
    ]