from django.shortcuts import render, redirect
import datetime
from django.conf import settings
from django.core.mail import send_mail
from bs4 import BeautifulSoup
import requests


# Create your views here.






date = datetime.datetime.now()
formated_date_for_email = date.strftime('%b %d, %y')



##send email view
def send_emails(request):
    url = requests.get(url='https://icu-dar-report.herokuapp.com/')
    soup = BeautifulSoup(url.content, 'lxml')
    
    daily_report_header = []
    daily_report_header_string = ''
    report_header = soup.find_all('h3')
    for line in report_header:
        line = line.text
        line = " ".join(line.split())
        daily_report_header.append(line)
        daily_report_header_string = " \n".join(daily_report_header)
        
   
    daily_report = []
    daily_report_string = ''
    hourly_report = soup.find_all('h4')
    for line in hourly_report:
        line = line.text
        line = " ".join(line.split())
        daily_report.append(line)
        daily_report_string = "  \n".join(daily_report)
        
    
    subject = f'DAR {formated_date_for_email}'
    message = daily_report_header_string + '\n \n' + daily_report_string
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['lazlemlop@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return redirect('create-dar')
    


### asks the user if he wants to send an email.
def send_emails_confirm(request):
    return render(request, 'report/send_mail.html')