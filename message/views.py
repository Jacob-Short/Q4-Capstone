from django.shortcuts import render, reverse, HttpResponseRedirect
from .models import Message
from accounts.models import MyUser
from .forms import AddTextForm


def MessageView(req, id):
    if req.method == 'POST':
        recip = MyUser.objects.get(id=id)
        form = AddTextForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            Message.objects.create(
                message=data['message'],
                author=req.user,
                recipient=recip
            )

            return HttpResponseRedirect(reverse('homepage'))
    form = AddTextForm()
    return render(req, 'generic_form.html', {'form': form})
