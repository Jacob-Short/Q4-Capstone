from django.shortcuts import redirect, render, HttpResponseRedirect
from faq_comment.models import FaqComment
from faq_comment.forms import AddFaqCommentForm

from faq.models import UserFaq


def index_view(request):
    # id=request.user.id
    # files = File.objects.filter(id=id)
    files = UserFaq.objects.all()
    context = {'files': files}
    template = 'index.html'
    # breakpoint()
    return render(request, template, context)


def create_file(request):
    if request.method == 'POST':
        form = AddFaqCommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            faq_comment = UserFaq.objects.create(
                comment=data['comment'],
                parent=data['parent'],
                user = request.user
            )
            return redirect('home')
    form = AddFaqCommentForm()
    context = {'form': form}
    return render(request, 'generic_form.html', context)