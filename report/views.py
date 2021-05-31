from django.shortcuts import redirect, render
from .models import DAR
from .forms import DARForm
from django.views.generic import UpdateView, DeleteView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings
from . import scraper
import datetime



date = datetime.datetime.now()
formated_date_for_email = date.strftime('%b %d, %y')


##send email view
def send_emails(request):
    subject = f'DAR {formated_date_for_email}'
    message = scraper.run_daily_report_header_scraper() + '\n \n' + scraper.run_daily_report_scraper()
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['lazlemlop@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return redirect('create-dar')
    


### asks the user if he wants to send an email.
def send_emails_confirm(request):
    return render(request, 'report/send_mail.html')
    


def home(request):
    context = {
        'date': date,
        'dar': DAR.objects.all()
    }
    return render(request, 'report/home.html', context)



@login_required
def create_dar(request):
    form = DARForm()
    if request.method == 'POST':
        form = DARForm(request.POST)
        if form.is_valid():
            new_dar = DAR(
                time=form.cleaned_data.get('time'),
                officer_relieving = form.cleaned_data.get('officer_relieving'),
                officer_relieved = form.cleaned_data.get('officer_relieved'),
                visitor_front_gate = form.cleaned_data.get('visitor_front_gate'),
                resident_front_gate = form.cleaned_data.get('resident_front_gate'),
                exit_front_gate = form.cleaned_data.get('exit_front_gate'),
                entrace_back_gate = form.cleaned_data.get('entrace_back_gate'),
                exit_back_gate = form.cleaned_data.get('exit_back_gate'),
                gym = form.cleaned_data.get('gym'),
                pool = form.cleaned_data.get('pool'),
                bascketball_court = form.cleaned_data.get('bascketball_court'),
                tennis_court = form.cleaned_data.get('tennis_court'),
                club_house = form.cleaned_data.get('club_house'),
                cameras_not_working = form.cleaned_data.get('cameras_not_working'),
                gates_not_working = form.cleaned_data.get('gates_not_working'),
                gate_arms_not_working = form.cleaned_data.get('gate_arms_not_working'),
                additional_comments=form.cleaned_data.get('additional_comments'),
                user = request.user,
            )
            new_dar.save()
            return redirect('home')
    else:
        form = DARForm()
    context = {
        'dar': DAR.objects.all().order_by('time'),
        'form': form,
        'date': date,
    }
    return render(request, 'report/report.html', context)




class DARUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DAR
    fields = [
        'time', 'officer_relieving', 'officer_relieved', 'visitor_front_gate',
        'resident_front_gate', 'exit_front_gate', 'entrace_back_gate', 'exit_back_gate',
        'gym', 'pool', 'bascketball_court', 'tennis_court', 'club_house', 'cameras_not_working',
        'gates_not_working', 'gate_arms_not_working', 'additional_comments'
    ]
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
           return True
        return False
    

class DARDeleteView(LoginRequiredMixin, DeleteView):
    model = DAR
    context_object_name = 'dar'
    success_url = '/'
     
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form) 

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
           return True
        return False



