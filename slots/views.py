from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from classification.models import Sentence


class SlotView(generic.ListView):
    template_name = 'slots/sentence_list.html'
    def get_queryset(self):
        return Sentence.objects.all()

def SubmitView(request):
    for post in request.POST:
        if post != 'csrfmiddlewaretoken':
            value = request.POST[post]
            try:
                selected_sent = Sentence.objects.get(pk=post)
            except(KeyError, Sentence.DoesNotExist):
                return render(request, 'slots/sentence_list.html', {'error_message': 'What have you done !!!'})
            else:
                selected_sent.slots = value
                selected_sent.save()
    return HttpResponseRedirect(reverse('slots:done'))

def DoneView(request):
    return HttpResponse('All Done!!! Thank you for your cooperation.')
