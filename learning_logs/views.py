from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.utils import timezone

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def check_topic_owner(owner, user):
    """Checks if the current user is the topic owner."""
    if owner != user:
        raise Http404
    else:
        return

# Create your views here.
def base(request):
    return render(request, 'learning_logs/base.html')

def base_bak(request):
    return render(request, 'learning_logs/base_bak.html')

def index(request):
    """The home page for learning_logs."""
    return render(request, 'learning_logs/index.html')

def about(request):
    """The about page for learning_logs."""
    return render(request, 'learning_logs/about.html')

def md_cheatsheet(request):
    return render(request, 'learning_logs/md_cheatsheet.html')

@login_required
def topics(request):
    """Shows all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by(Lower('text').asc())
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id)

    # Make sure the topic belongs to the current user
    check_topic_owner(topic.owner, request.user)

    entries = topic.entry_set.order_by('-id')
    context = {'topic':topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted. Create a blank form.
        form = TopicForm()
    else:
        # POST data submitted. Process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a selected topic."""
    topic = Topic.objects.get(id=topic_id)

    # Make sure entry topic belongs to the current user
    check_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        # No data submitted. Create a blank form.
        form = EntryForm()

    else:
        # POST data submitted. Process data.
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.owner = request.user
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'form':form, 'topic':topic}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # Make sure entry belongs to the current user
    check_topic_owner(topic.owner, request.user)

    if request.method != 'POST':
        # Initial request: pre-fill form with the current entry.
        form = EntryForm(instance=entry)

    else:
        # POST data submitted. Process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))

    context = {'form':form, 'topic':topic, 'entry':entry}
    return render(request, 'learning_logs/edit_entry.html', context)
