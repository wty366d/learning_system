from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from mysite.views import LoginRequiredMixin
from lecture.forms import LectureForm
from lecture.models import Lecture


# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'lecture/index.html'
    context_object_name = 'lecture_list'

    def get_queryset(self):
        return Lecture.objects.all()



class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Lecture
    template_name = 'lecture/detail.html'



#class LectureFormView(generic.edit.FormView):
    #template_name = 'lecture/create.html'
    #form_class = LectureForm
    #success_url = '/lecture/'

    #def form_valid(self, form):
        ## This method is called when valid form data has been POSTed.
        ## It should return an HttpResponse.
        #return super(CreateView, self).form_valid(form)



class CreateFormView(LoginRequiredMixin, generic.edit.CreateView):
    model = Lecture
    form_class = LectureForm
    #fields = ['lecture_id', 'lecture', 'term']    
    template_name = 'lecture/create.html'
    
    #def get_context_data(self, *args, **kwargs):
        #context_data = super(CreateFormView, self).get_context_data(
            #*args, **kwargs)
        #context_data.update({'test': '321312'})
        #return context_data


class UpdateFormView(LoginRequiredMixin, generic.edit.UpdateView):
    model = Lecture
    #fields = '__all__'
    form_class = LectureForm
    template_name = 'lecture/update.html'



class DeleteFormView(LoginRequiredMixin, generic.edit.DeleteView):
    model = Lecture
    template_name = 'lecture/delete.html'
    success_url = reverse_lazy('lecture:index')
