#from django.forms import ModelForm,Form
from django import forms
from lecture.models import Lecture

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'
        #['lecture_id', 'lecture', 'term']

#class LectureSearchForm(forms.Form):
    #name = forms.CharField(required=False)
