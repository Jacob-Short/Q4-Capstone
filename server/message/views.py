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

            return HttpResponseRedirect(reverse('profile', args=(id,)))
    form = AddTextForm()
    return render(req, 'generic_form.html', {'form': form})

def UserMessages(req, id):
    user = MyUser.objects.get(id=id)
    user_messages = Message.objects.filter(recipient=user)
    return render(req, 'messages.html', {'user_messages': user_messages})

def DeleteMessage(req, id):
    del_message = Message.objects.get(id=id)
    user_id = req.user.id
    del_message.delete()
    return HttpResponseRedirect(reverse('usermessages', args=(user_id,)))