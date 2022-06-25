from django.shortcuts import render

from I4G026808KJ6.blog.models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "post.html"

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url  = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateViedw(UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields ="__all__"
    success_url = reverse_lazy("blog:all") 
