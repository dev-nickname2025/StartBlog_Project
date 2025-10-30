from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import UserForm, PostForm, CommentForm

def register_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Register Successful!")
        else:
            messages.error(request, "Register Fail. < Please Try Again. >")
    else:
        form = UserForm()
    return render(request, 'blog/register.html', {'form': form})

def login_form(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login Successfully.")
            return redirect('post_list')
        else:
            messages.warning(request, "Please Check Username and Password.")
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_form(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'blog/profile.html')

@login_required
def post_list(request):  #.all()
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_post.html', {'posts': posts})

@login_required
def create_post(request):
    if request.method == 'POST':        #For Media File Upload
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, "Post Created Successfully.")
            return redirect('post_list')
        else:
            messages.error(request, "Failed to Create Post. < Please Try Again. >")
    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

@login_required
def update_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(request.POST or None, request.FILES ,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post Updated Successfully.")
            return redirect('post_list')
        else:
            messages.error(request, "Failed to Update Post. < Please Try Again. >")
    else:
        post = get_object_or_404(Post, pk=pk)
        form = PostForm(instance=post)
        return render(request, 'blog/post_form.html', {'form': form})
    
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author == request.user:
        post.delete()
    messages.success(request, "Post Deleted Successfully.")
    return redirect('post_list')

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })