# Generated by Django 4.2.2 on 2023-06-30 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CateringApp', '0018_order_pickup_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='otp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(1, 'Confirmation'), (2, 'Processing'), (3, 'Preparing'), (4, 'Ready'), (5, 'Completion'), (6, 'Cancel'), (7, 'Refund')], default=1),
        ),
    ]
