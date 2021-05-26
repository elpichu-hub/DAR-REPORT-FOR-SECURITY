from django.http import request
from django.shortcuts import redirect
from report.models import DAR
from django import forms
from .choices import choices_for_time, choices_for_traffic, officer_relieving, officer_relieved





class DARForm(forms.Form):
    time = forms.ChoiceField(choices=choices_for_time)
    officer_relieving = forms.ChoiceField(choices=officer_relieving, required=False)
    officer_relieved = forms.ChoiceField(choices=officer_relieved, required=False)
    visitor_front_gate = forms.ChoiceField(choices=choices_for_traffic, required=False)
    resident_front_gate = forms.ChoiceField(choices=choices_for_traffic, required=False)
    exit_front_gate = forms.ChoiceField(choices=choices_for_traffic, required=False)
    entrace_back_gate = forms.ChoiceField(choices=choices_for_traffic, required=False)
    exit_back_gate = forms.ChoiceField(choices=choices_for_traffic, required=False)
    gym = forms.IntegerField(min_value=0, max_value=20, required=False)
    pool = forms.IntegerField(min_value=0, max_value=20, required=False)
    bascketball_court = forms.IntegerField(min_value=0, max_value=20, required=False)
    tennis_court = forms.IntegerField(min_value=0, max_value=20, required=False)
    club_house = forms.IntegerField(min_value=0, max_value=20, required=False)
    cameras_not_working = forms.IntegerField(min_value=0, max_value=20, required=False)
    gates_not_working = forms.IntegerField(min_value=0, max_value=7, required=False)
    gate_arms_not_working = forms.IntegerField(min_value=0, max_value=7, required=False)
    additional_comments = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'cols':20}), required=False)
    





    