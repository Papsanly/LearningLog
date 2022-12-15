from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .forms import TopicForm, EntryForm
from .models import Topic, Entry


def index(request):
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    topics_ = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics_}
    return render(request, 'learning_logs/topics.html', context)


@login_required
def topic(request, topic_id):
    topic_ = Topic.objects.get(id=topic_id)
    if topic_.owner != request.user:
        raise Http404

    entries = topic_.entry_set.order_by('-date_added')
    context = {'topic': topic_, 'entries': entries}

    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic_ = form.save(commit=False)
            new_topic_.owner = request.user
            new_topic_.save()
            return redirect('learning_logs:topics')

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    topic_ = Topic.objects.get(id=topic_id)
    if topic_.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry_ = form.save(commit=False)
            new_entry_.topic = topic_
            new_entry_.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    context = {'topic': topic_, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic_ = entry.topic
    if topic_.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic_.id)

    context = {'entry': entry, 'topic': topic_, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
