from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponseRedirect
from faq_comment.models import FaqComment
from django.views.generic import View
from faq_comment.forms import AddFaqCommentForm

from faq_comment.models import FaqComment
from faq.models import UserFaq
from message.models import Message
from faq_notification.models import FaqNotification
from faq_notification.views import create_faq_notification


class CreateFaqComment(View):
    '''can create a comment on a review'''

    def get(self, request, id):
        form = AddFaqCommentForm()
        target_user = request.user.id
        messages = Message.objects.filter(recipient=target_user)
        context = {'messages': messages, 'form': form}
        return render(request, 'generic_form.html', context)


    def post(self, request, id):
        faq = UserFaq.objects.get(id=id)
        faq_created = faq.user
        form = AddFaqCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_comment = FaqComment.objects.create(
                comment=data['answer'],
                parent=data['previous_answer'],
                user = request.user,
                faq=faq
            )
            create_faq_notification(faq, faq_created)
            return redirect('homepage')