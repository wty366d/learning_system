from django.forms import ModelForm
from history.models import History

class HistoryForm(ModelForm):
    class Meta:
        model = History
        exclude = ('student',)
        #fields = '__all__'
        #['lecture_id', 'lecture', 'term']

