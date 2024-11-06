from urllib.parse import urlencode

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm, BooleanField
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse
from django.utils.translation import gettext as _
from friendship.models import Friend

from takes.models import Take


class TakeForm(ModelForm):
    class Meta:
        model = Take
        fields = ['content', 'is_public']


class PrivateTakeForm(ModelForm):
    is_public = BooleanField(required=False, disabled=True, initial=False, help_text=_('this is a private thread'))

    class Meta:
        model = Take
        fields = ['content', 'is_public']


def view(request: HttpRequest, take_id: str) -> HttpResponse:
    take = Take.objects.get(id=take_id)

    if not take.is_public and take.author.id is not request.user.id:
        if not request.user.is_authenticated:
            # if user tries to view private take
            # redirect to login and then redirect to take again
            next_url = reverse('takes:take', kwargs={'take_id': take_id})
            login_url = reverse('login')
            redirect_url = f"{login_url}?{urlencode({'next': next_url})}"
            return HttpResponseRedirect(redirect_url)

        if not Friend.objects.are_friends(request.user, take.author):
            messages.warning(request,
                             _('This is a private Take, you are not friends with %(username)s')
                             % {'username': take.author.username})

    return render(request, 'takes-full-conversation.html', {'take': take})


@login_required
def reply(request: HttpRequest, reply_to_id: str) -> HttpResponse:
    take = Take.objects.get(id=reply_to_id)

    if take.is_public:
        form = TakeForm()
    else:
        form = PrivateTakeForm()

    if request.method == "POST":
        if take.is_public:
            form = TakeForm(request.POST)
        else:
            form = PrivateTakeForm(request.POST)

        if form.is_valid():
            take = form.save(commit=False)
            take.reply_to_id = reply_to_id
            take.author_id = request.user.id
            take.save()
            return HttpResponseRedirect(reverse('takes:take', kwargs={'take_id': reply_to_id}))

    return render(request, 'takes-reply.html', {
        'reply_form': form,
        'reply_to_take': take,
    })


@login_required
def create(request: HttpRequest) -> HttpResponse:
    form = TakeForm()

    if request.method == "POST":
        form = TakeForm(request.POST)
        if form.is_valid():
            take = form.save(commit=False)
            take.author_id = request.user.id
            take.save()
            return HttpResponseRedirect(reverse('takes:take', kwargs={'take_id': take.id}))

    return render(request, 'takes-create.html', {
        'create_form': form
    })


@login_required
def delete(request: HttpRequest, take_id: str) -> HttpResponse:
    if request.method == "POST":
        take = Take.objects.get(id=take_id)
        take.delete()
        messages.success(request, 'Take deleted')

    if request.GET.get('next', False):
        return HttpResponseRedirect(request.GET.get('next'))

    return HttpResponseRedirect(reverse('index'))


@login_required
def like(request: HttpRequest, take_id: str) -> HttpResponse:
    take = Take.objects.get(id=take_id)
    if not take.liked_by.contains(request.user):
        take.liked_by.add(request.user)
        take.disliked_by.remove(request.user)
        messages.success(request, 'You have like this take')

    if request.GET.get('next', False):
        return HttpResponseRedirect(request.GET.get('next'))

    return HttpResponseRedirect(reverse('takes:take', kwargs={'take_id': take_id}))


@login_required
def dislike(request: HttpRequest, take_id: str) -> HttpResponse:
    take = Take.objects.get(id=take_id)
    if not take.disliked_by.contains(request.user):
        take.disliked_by.add(request.user)
        take.liked_by.remove(request.user)
        messages.success(request, 'You have disliked this take')

    if request.GET.get('next', False):
        return HttpResponseRedirect(request.GET.get('next'))

    return HttpResponseRedirect(reverse('takes:take', kwargs={'take_id': take_id}))
