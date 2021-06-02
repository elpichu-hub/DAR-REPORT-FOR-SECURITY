from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from django.urls import reverse




class DAR(models.Model):
    #time = models.CharField(max_length=50, default='13:00')
    time = models.DateTimeField(default=datetime.now)
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


    def get_absolute_url(self):
        return reverse('create-dar')



class End_Of_Shift_Dar(models.Model):
    date = models.DateTimeField(default=datetime.now)
    report = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    

    def __repr__(self):
        return f'{self.date}'




