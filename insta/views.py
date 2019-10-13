from django.shortcuts import render,redirect
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
            return redirect('Timeline')

        else:
            return redirect('Timeline')


def search_results(request):
    current_user = request.user
    current_user_id=request.user.id
    posts = Post.objects.filter(username=current_user_id)
    if 'searchname' in request.GET and request.GET['searchname']:
        search_term = request.GET.get("searchname")
        searched_names = Profile.search_profile(search_term)
        message = f"{search_term}"

        return render(request,'search.html', {"message":message, "usernames":searched_names,"posts":posts})

    else:
        message = "You haven't searched for any username"
        return render(request,'search.html',{"message":message})





@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    current_user_id=request.user.id
    form = CommentForm()
    comments=Comment.objects.all()
    # comment_number=len(comments)

    try:
        profile = Profile.objects.get(user=current_user)
        posts = Post.objects.filter(username=current_user_id)
        title = profile.user
        username = profile.user
        post_number = len(posts)

    except ObjectDoesNotExist:
        return redirect('Timeline')

    return render(request, 'profile.html',{"profile":profile,"posts":posts,"form":form,"post_number":post_number,"title":title,"username":username,"comments":comments})