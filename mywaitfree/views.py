from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Guest
from django.template import loader
from .forms import GuestForm
from django.utils import timezone
from django.views.decorators.cache import never_cache

@never_cache
def index(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['guest_name']
            number = form.cleaned_data['phone_number']
            size = form.cleaned_data['group_size']
            g = Guest(guest_name=name, phone_number=number, group_size=int(size), register_time=timezone.now())
            g.save()
            return HttpResponseRedirect('thanks/')
    else:
        form = GuestForm()
    return render(request, 'name.html', {'form': form})

@never_cache
def results(request):
    waiting_list = Guest.objects.order_by('register_time')
    template = loader.get_template('mywaitfree/res.html')
    context = {
        'waiting_list' : waiting_list,
    }
    return HttpResponse(template.render(context, request))

@never_cache
def thanks(request):
    return render(request, 'mywaitfree/thanks.html')
