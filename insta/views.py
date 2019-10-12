from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post,Profile,Comment
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

@login_required(login_url='/accounts/login')
def Comment_Image(request,pk):
    # user_comment = request.GET.get('comment')
    current_user = request.user
    current_image = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.username = current_user
            comment.post = current_image
            comment.save()
            # comment.comment = user_comment
            return redirect('home')

        else:
            return redirect('home')
