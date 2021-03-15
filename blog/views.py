from django.shortcuts import render
from django.http import HttpResponse


#Posts
posts = [
    {
        'author' : 'CoreyMs',
        'title' : 'Blog post 1',
        'content': 'First post content',
        'date_posted':'August 27, 2008'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog post 2',
        'content': 'second post content',
        'date_posted':'August 27, 2050'
    },
]

# Create your views here.
def home(request):
    context = {
        'posts' :  posts
    }
    return render(request, 'blog/home.html', context)

def About(request):
    return render(request, 'blog/about.html',{'title':'About'})