# Generated by Django 4.2.5 on 2023-12-06 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_postservice_date_posted_postservice_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='dateAccepted',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='dateFinished',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
    ]
