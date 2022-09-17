from django.views import generic
from blog.models import Post
from django.http import HttpResponse



class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:3]
    template_name = 'header.html'

