from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from .models import Guest
from django.template import loader
from .forms import GuestForm
from django.utils import timezone

def index(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['guest_name']
            number = form.cleaned_data['phone_number']
            g = Guest(guest_name=name, phone_number=number, register_time=timezone.now())
            g.save()
            return HttpResponseRedirect('thanks/')
    else:
        form = GuestForm()
    return render(request, 'name.html', {'form': form})

def results(request):
    waiting_list = Guest.objects.order_by('register_time')
    template = loader.get_template('mywaitfree/results.html')
    context = {
        'waiting_list' : waiting_list,
    }
    return HttpResponse(template.render(context, request))

def thanks(request):
    return render(request, 'mywaitfree/thanks.html')
