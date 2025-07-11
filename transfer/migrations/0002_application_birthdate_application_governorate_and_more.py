# Generated by Django 5.2.3 on 2025-06-16 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='application',
            name='governorate',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='student_grade',
            field=models.CharField(choices=[('1KG', '1 KG'), ('2KG', '2 KG'), ('1PR', '1 Primary'), ('2PR', '2 Primary'), ('3PR', '3 Primary'), ('4PR', '4 Primary'), ('5PR', '5 Primary'), ('6PR', '6 Primary'), ('1PA', '1 Preparatory'), ('2PA', '2 Preparatory'), ('3PA', '3 Preparatory')], max_length=3),
        ),
    ]
