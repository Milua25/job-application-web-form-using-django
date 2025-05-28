from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages
from django.core.mail import EmailMessage

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            occupation = form.cleaned_data['occupation']
            date = form.cleaned_data['date']

            Form.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                occupation=occupation,
                date=date,)

            message_body = f"""
            New Job Application was submitted.
            Thank you {first_name}!
            
            Regards,
            Admin 
            """
            email_message = EmailMessage(
                subject="Form submitted successfully",
                body=message_body,
                to=[email]
            )
            print(email_message.from_email)

            email_message.send()

            messages.success(request, 'Form Submitted successfully!')
            return render(request, 'index.html')

    else:
        return render(request, 'index.html')