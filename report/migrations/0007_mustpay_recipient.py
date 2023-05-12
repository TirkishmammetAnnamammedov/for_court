# Generated by Django 4.2 on 2023-05-12 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0006_recipient_mustpay_opened_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mustpay',
            name='recipient',
            field=models.ForeignKey(default=' ', on_delete=django.db.models.deletion.CASCADE, related_name='mustpay', to='report.recipient', to_field='name_and_lastname', verbose_name='Algydar'),
        ),
    ]