# Generated by Django 4.2.5 on 2023-10-04 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug_description', models.TextField()),
                ('report_date', models.DateField()),
                ('bug_type', models.CharField(choices=[('error', 'error'), ('new feature', 'new feature'), ('enhancement', 'enhancement'), ('other', 'other')], max_length=20)),
                ('status', models.CharField(choices=[('To do', 'To do'), ('In Progress', 'In Progress'), ('Done', 'Done')], max_length=20)),
            ],
        ),
    ]
