from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Message
from .forms import AddTextForm


def MessageView(req):
    if req.method == 'POST':
        form = AddTextForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            Message.objects.create(
                message=data['message'],
                author=req.user
            )

            return HttpResponseRedirect(reverse('homepage'))
    form = AddTextForm()
    return render(req, 'generic_form.html', {'form': form})
