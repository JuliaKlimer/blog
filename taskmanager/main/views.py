from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.views.generic import DetailView, UpdateView, DeleteView


def index(request):
    posts = Post.objects.all()
    return render(request, 'main/index.html', {'title': 'Main Page', 'posts': posts})

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detail_views.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'main/add.html'

    form_class = PostForm

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'main/delete.html'


def about(request):
    return render(request, 'main/about.html')

def add(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Error'
    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add.html', context)