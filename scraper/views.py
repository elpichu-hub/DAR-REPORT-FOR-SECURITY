from django.shortcuts import render, redirect
import datetime
from . import scraper
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.






date = datetime.datetime.now()
formated_date_for_email = date.strftime('%b %d, %y')



##send email view
def send_emails(request):
    subject = f'DAR {formated_date_for_email}'
    message = scraper.daily_report_header_string + '\n \n' + scraper.daily_report_string
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['lazlemlop@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return redirect('create-dar')
    


### asks the user if he wants to send an email.
def send_emails_confirm(request):
    return render(request, 'report/send_mail.html')