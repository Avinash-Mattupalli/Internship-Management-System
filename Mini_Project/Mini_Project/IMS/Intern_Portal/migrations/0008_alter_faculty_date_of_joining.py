# Generated by Django 4.2.2 on 2023-08-03 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Intern_Portal', '0007_alter_faculty_designation_alter_faculty_employee_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='date_of_joining',
            field=models.DateField(verbose_name=models.DateField(blank=True, null=True)),
        ),
    ]
