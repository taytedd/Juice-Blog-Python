from django.shortcuts import render

posts = [
    {
        'author': 'Ted Ochingo',
        'title': 'Blog Post',
        'content': 'We The Best',
        'date_posted': 'Jun 20, 2011'
    },
    {
        'author': 'Key Glock',
        'title': 'Blog Post',
        'content': 'We The Best',
        'date_posted': 'May 2, 2015'
    }




]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')


