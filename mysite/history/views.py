from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic

from mysite.views import LoginRequiredMixin

from history.forms import HistoryForm
from history.models import History


# Create your views here.

class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'history/index.html'
    context_object_name = 'history_list'

    def get_queryset(self):
        return History.objects.filter(student=self.request.user).order_by('year')



class DetailView(LoginRequiredMixin, generic.DetailView):
    model = History
    template_name = 'history/detail.html'



#class HistoryFormView(generic.edit.FormView):
    #template_name = 'history/create.html'
    #form_class = HistoryForm
    #success_url = '/history/'

    #def form_valid(self, form):
        ## This method is called when valid form data has been POSTed.
        ## It should return an HttpResponse.
        #return super(CreateView, self).form_valid(form)



class CreateFormView(LoginRequiredMixin, generic.edit.CreateView):
    model = History
    form_class = HistoryForm
    
    #fields =   
    template_name = 'history/create.html'
    
    def form_valid(self, form):
        user = self.request.user
        form.instance.student = user
        return super(CreateFormView, self).form_valid(form)
    
    #def get_context_data(self, *args, **kwargs):
        #context_data = super(CreateFormView, self).get_context_data(
            #*args, **kwargs)
        #context_data.update({'test': '321312'})
        #return context_data


class UpdateFormView(LoginRequiredMixin, generic.edit.UpdateView):
    model = History
    #fields = '__all__'
    form_class = HistoryForm
    template_name = 'history/update.html'



class DeleteFormView(LoginRequiredMixin, generic.edit.DeleteView):
    model = History
    template_name = 'history/delete.html'
    success_url = reverse_lazy('history:index')
