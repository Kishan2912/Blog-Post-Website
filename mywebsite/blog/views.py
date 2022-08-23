from django.db import models
from django.shortcuts import render, get_list_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import DeleteView
from .models import post

# posts=[
#     {
#         'author': 'Prem chand',
#         'title': 'Blog Post no 1',
#         'content':'first post content',
#         'date_posted':'Sept 27, 2021'
#     },
#     {
#         'Author': 'Ram dhari singh dinkar',
#         'title': 'Blog Post no 2',
#         'content':'Second post content',
#         'date_posted':'Sept 28, 2021'
#     }
# ]

# Create your views here.
def home(request):
    context={
        'posts':post.objects.all()
    }
    return render(request,'blog/Home.html',context)

class PostListView(ListView):
    model = post
    template_name='blog/Home.html' # <app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=3

class UserPostListView(ListView):
    model = post
    template_name='blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name='posts'
    ordering=['-date_posted']
    paginate_by=3

    def get_queryset(self):
        user=get_list_or_404(User,username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date-posted')

class PostDetailView(DetailView):
    model = post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False        

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    success_url='/'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False  


def about(request):
    return render(request,'blog/about.html',{'title':'About'})  
