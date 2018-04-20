from django.shortcuts import render
from learning_logs.models import Topic, Entry
from learning_logs.forms import TopicForm, EntryForm
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


def index(request):
	return render(request, "learning_logs/index.html")


@login_required
def topics(request):
	"""显示topic"""
	topics = Topic.objects.filter(owner=request.user).order_by("pup_date")
	context = {"topics":topics}
	return render(request, "learning_logs/topics.html", context)


@login_required
def topic(request, topic_id):
	"""主题内容"""
	topic = Topic.objects.get(id=topic_id)
	if topic.owner != request.user:
		raise Http404
	entries = topic.entry_set.order_by("pup_date")
	context = {"topic":topic, "entries":entries}
	return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
	"""添加topic"""
	if request.method != "POST":
		form = TopicForm()
	else:
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save()
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse("topics"))

	context = {"form":form}
	return render(request, "learning_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
	"""添加条目"""
	topic = Topic.objects.get(id=topic_id)

	if request.method != "POST":
		form = EntryForm()
	else:
		form = EntryForm(data=request.POST)
		if form.is_valid():
			new_entry = form.save(commit=False)
			new_entry.topic = topic
			new_entry.save()
			return HttpResponseRedirect(reverse("topic", args=[topic_id]))

	context = {"topic":topic, "form":form}
	return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
	"""编辑"""
	entry = Entry.objects.get(id=entry_id)
	topic = entry.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != "POST":
		form = EntryForm(instance=entry)
	else:
		form = EntryForm(instance=entry, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse("topic", args=[topic.id]))

	context = {"topic":topic, "entry":entry, "form":form}
	return render(request, "learning_logs/edit_entry.html", context)