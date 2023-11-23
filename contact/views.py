from django.shortcuts import render, redirect
from django.contrib import  messages
from contact.forms import ContactForm

# Create your views here.
def subscibe(request):
    context = {
        'title' : "Pool Masters"
    }
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,f"Your message has been sent. Thank you!")
            return redirect('home')

    else:
        context['form'] = form
    return render(request, "account/index.html") 