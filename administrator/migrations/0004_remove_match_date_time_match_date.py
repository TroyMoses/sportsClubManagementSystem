# Generated by Django 5.0.2 on 2024-04-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0003_staff_contact_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='date_time',
        ),
        migrations.AddField(
            model_name='match',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
