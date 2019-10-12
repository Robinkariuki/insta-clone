from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CommentForm,PostForm,ProfileForm
# Create your views here.
@login_required(login_url='/accounts/login/')
def timeline(request):
    
    posts = Post.objects.all()
    current_user = request.user
    profiles = Profile.objects.all()
    form = CommentForm()
    comments = Comment.objects.all()

    return render(request,'timeline.html',{ "posts": posts ,"form":form, "comments":comments,"profiles":profiles})