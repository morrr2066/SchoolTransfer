from django.shortcuts import render, redirect
from .forms import ApplicationForm
from django.contrib import messages
from .models import Application

def apply_view(request):
    if request.method == 'POST':
        print("Form is being submitted")
        form = ApplicationForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            national_id = form.cleaned_data['national_id']
            if Application.objects.filter(national_id=national_id).exists():
                print("Duplicate national ID")
                messages.error(request, "You already submitted an application with this National ID. تم إستخدام هذا الرقم القومى فى طلب تحويل من قبل")
            else:
                application = form.save()
                return render(request, 'transfer/confirmation.html', {'application': application})

        else:
            print("Form is NOT valid")
            print(form.errors)
    else:
        form = ApplicationForm()
    return render(request, 'transfer/apply.html', {'form': form})


def confirmation_view(request):
    return render(request, 'transfer/confirmation.html')
