# Generated by Django 5.1.3 on 2024-11-23 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_activity_pdf_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='pdf_file',
        ),
        migrations.CreateModel(
            name='ActivityPDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='activities/pdf/')),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pdfs', to='myapp.activity')),
            ],
        ),
    ]
