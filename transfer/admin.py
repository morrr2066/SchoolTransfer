import openpyxl
from django.http import HttpResponse
from .models import Application, School
from django.contrib import admin

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'national_id', 'birthdate', 'governorate',
        'student_grade', 'phone_number', 'from_school', 'to_school'
    )
    actions = ['export_as_excel']  # 👈 add this line

    def export_as_excel(self, request, queryset):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Applications"

        # Add headers
        headers = [
            'Full Name', 'National ID', 'Birthdate', 'Governorate',
            'Grade', 'Phone Number', 'From School', 'To School'
        ]
        ws.append(headers)

        # Add data
        for obj in queryset:
            ws.append([
                obj.full_name,
                obj.national_id,
                obj.birthdate,
                obj.governorate,
                obj.student_grade,
                obj.phone_number,
                str(obj.from_school) if obj.from_school else '',
                str(obj.to_school) if obj.to_school else ''
            ])

        # Send response
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="applications.xlsx"'
        wb.save(response)
        return response

    export_as_excel.short_description = "Export selected to Excel"


admin.site.register(School)
