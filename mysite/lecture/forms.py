from django.forms import ModelForm
from lecture.models import Lecture

class LectureForm(ModelForm):
    class Meta:
        model = Lecture
        fields = '__all__'
        #['lecture_id', 'lecture', 'term']

