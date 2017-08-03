from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Sentence

class IndexView(generic.ListView):
    model = Sentence

def CheckOK(request):
    if len(request.POST) != Sentence.objects.count()*2 +1:
        return render(request, 'classification/sentence_list.html', {'error_message': 'You did not select a choice.'})

    for post in request.POST:
        if post != 'csrfmiddlewaretoken':
            key, task = post.split('_')
            value = request.POST[post]
            try:
                selected_sent = Sentence.objects.get(pk=key)
            except(KeyError, Sentence.DoesNotExist):
                return render(request, 'classification/sentence_list.html', {'error_message': 'What have you done !!!'})
            else:
                if task == '1':
                    selected_sent.domain = int(value)
                elif task == '2':
                    selected_sent.intent = int(value)
                selected_sent.save()
    return HttpResponseRedirect(reverse('classification:results'))

def results(request):
    return HttpResponse('All Done!!! Thank you for your cooperation.')
