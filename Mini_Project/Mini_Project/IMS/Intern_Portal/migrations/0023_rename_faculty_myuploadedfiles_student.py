# Generated by Django 4.2.2 on 2023-09-21 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0022_remove_myuploadedfiles_faculty_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuploadedfiles',
            old_name='faculty',
            new_name='student',
        ),
    ]
