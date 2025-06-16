from django.db import models
from datetime import datetime


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Application(models.Model):
    GRADES = [
        ('1KG', '1 KG'),
        ('2KG', '2 KG'),
        ('1PR', '1 Primary'),
        ('2PR', '2 Primary'),
        ('3PR', '3 Primary'),
        ('4PR', '4 Primary'),
        ('5PR', '5 Primary'),
        ('6PR', '6 Primary'),
        ('1PA', '1 Preparatory'),
        ('2PA', '2 Preparatory'),
        ('3PA', '3 Preparatory'),
    ]

    full_name = models.CharField(max_length=100)
    national_id = models.CharField(max_length=14, unique=True)
    student_grade = models.CharField(max_length=3, choices=GRADES)
    phone_number = models.CharField(max_length=20)
    birthdate = models.DateField(null=True, blank=True)
    governorate = models.CharField(max_length=50, null=True, blank=True)
    from_school = models.ForeignKey(School, related_name='from_applications', on_delete=models.SET_NULL, null=True)
    to_school = models.ForeignKey(School, related_name='to_applications', on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        # Parse birthdate and governorate from national_id before saving
        if self.national_id and len(self.national_id) == 14:
            century_code = int(self.national_id[0])
            year = int(self.national_id[1:3])
            month = int(self.national_id[3:5])
            day = int(self.national_id[5:7])
            gov_code = int(self.national_id[7:9])

            # Determine century
            if century_code == 2:
                year += 1900
            elif century_code == 3:
                year += 2000
            else:
                year += 1900  # fallback

            try:
                self.birthdate = datetime(year, month, day).date()
            except ValueError:
                self.birthdate = None

            # Map governorate code to name
            gov_map = {
                1: "Cairo", 2: "Alexandria", 3: "Port Said", 4: "Suez",
                11: "Damietta", 12: "Dakahlia", 13: "Sharqia", 14: "Kalyubia",
                15: "Kafr El Sheikh", 16: "Gharbia", 17: "Monufia", 18: "Beheira",
                19: "Ismailia", 21: "Giza", 22: "Beni Suef", 23: "Fayoum",
                24: "Minya", 25: "Asyut", 26: "Sohag", 27: "Qena",
                28: "Aswan", 29: "Luxor", 31: "Red Sea", 32: "New Valley",
                33: "Matrouh", 34: "North Sinai", 35: "South Sinai"
            }
            self.governorate = gov_map.get(gov_code, "Unknown")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name


