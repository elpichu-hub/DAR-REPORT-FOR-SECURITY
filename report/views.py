from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import DAR
from .forms import DARForm
from datetime import datetime
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

date = datetime.now()

@login_required
def home(request):
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
            print(type(new_dar.gym))
            new_dar.save()
            return redirect('report')
    else:
        form = DARForm()
    context = {
        'dar': DAR.objects.all().order_by('time'),
        'form': form,
        'date': date,
    }
    return render(request, 'report/report.html', context)




class DARUpdateView(UpdateView):
    model = DAR
    fields = [
        'time', 'officer_relieving', 'officer_relieved', 'visitor_front_gate',
        'resident_front_gate', 'exit_front_gate', 'entrace_back_gate', 'exit_back_gate',
        'gym', 'pool', 'bascketball_court', 'tennis_court', 'club_house', 'cameras_not_working',
        'gates_not_working', 'gate_arms_not_working', 'additional_comments'
    ]
    

class DARDeleteView(DeleteView):
    model = DAR
    context_object_name = 'dar'
    success_url = '/report/'


