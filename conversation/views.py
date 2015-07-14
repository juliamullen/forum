from django.shortcuts import render
from conversation.models import Place, Conversation, Post
from conversation.forms import PostForm

def index(request):
    form = PostForm(request.POST or None,
                    label_suffix='')
    if form.is_valid():
        form.save()
        conversation = form.cleaned_data.get('conversation', None)
        conversation.update_post_count()
    conversations = Conversation.objects.all()
    context = {
        'conversations': conversations,
        'postform':      form,
    }
    return render(request, "index.html", context)
