# Generated by Django 4.2.2 on 2023-08-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0016_files_uploadedfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='MappedExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_file', models.FileField(upload_to='mapped_excel/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
