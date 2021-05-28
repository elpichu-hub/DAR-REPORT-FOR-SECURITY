from django.test import TestCase




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








class DAR(models.Model):
    time = models.CharField(max_length=50, default='13:00')
    officer_relieving= models.CharField(blank=True, null=True, max_length=20)
    officer_relieved = models.CharField(blank=True, null=True, max_length=20)
    visitor_front_gate = models.CharField(blank=True, null=True, max_length=20)
    resident_front_gate = models.CharField(blank=True, null=True, max_length=20)
    exit_front_gate = models.CharField(blank=True, null=True, max_length=20)
    entrace_back_gate = models.CharField(blank=True, null=True, max_length=20)
    exit_back_gate = models.CharField(blank=True, null=True, max_length=20)
    gym = models.IntegerField(blank=True, null=True)
    pool = models.IntegerField(blank=True, null=True)
    bascketball_court = models.IntegerField(blank=True, null=True)
    tennis_court = models.IntegerField(blank=True, null=True)
    club_house = models.IntegerField(blank=True, null=True)
    cameras_not_working = models.IntegerField(blank=True, null=True)
    gates_not_working = models.IntegerField(blank=True, null=True)
    gate_arms_not_working = models.IntegerField(blank=True, null=True)
    additional_comments = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    

    def __repr__(self):
        return f'{self.title}'


    #def get_absolute_url(self):
        #return reverse('report')

 

    
  