# Generated by Django 5.0.3 on 2024-03-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_announcement_studentsection_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='section',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
