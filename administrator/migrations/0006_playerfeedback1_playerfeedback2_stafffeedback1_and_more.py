# Generated by Django 5.0.2 on 2024-04-02 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0005_remove_trainingsession_date_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerFeedback1',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Observations', 'Observations'), ('Complaint', 'Complaint')], default='Observations', max_length=30)),
                ('description', models.TextField(default=None, max_length=200)),
                ('player_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.player')),
                ('training_session_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.trainingsession')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerFeedback2',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Observations', 'Observations'), ('Complaint', 'Complaint')], default='Observations', max_length=30)),
                ('description', models.TextField(default=None, max_length=200)),
                ('match_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.match')),
                ('player_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.player')),
            ],
        ),
        migrations.CreateModel(
            name='StaffFeedback1',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Observations', 'Observations'), ('Complaint', 'Complaint')], default='Observations', max_length=30)),
                ('description', models.TextField(default=None, max_length=200)),
                ('staff_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.staff')),
                ('training_session_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.trainingsession')),
            ],
        ),
        migrations.CreateModel(
            name='StaffFeedback2',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('Observations', 'Observations'), ('Complaint', 'Complaint')], default='Observations', max_length=30)),
                ('description', models.TextField(default=None, max_length=200)),
                ('match_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.match')),
                ('staff_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='administrator.staff')),
            ],
        ),
        migrations.DeleteModel(
            name='Feedback',
        ),
    ]
