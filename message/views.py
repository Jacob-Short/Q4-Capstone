from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Text
from .forms import AddTextForm


def MessageView(req):
    if req.method == 'POST':
        form = AddTextForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            Text.objects.create(
                title=data['title'],
                description=data['description'],
            )

            return HttpResponseRedirect(reverse('homepage'))
    form = AddTextForm()
    return render(req, 'generic_form.html', {'form': form})
