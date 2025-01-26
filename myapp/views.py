from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import NewsletterSignupForm
from django.http import HttpResponse
from django.db import IntegrityError
from django.views import View

class Index(View):
    def get(self, request):
        context = {
        'posts':Post.objects.all()
        }
        return render(request, 'myapp/index.html', context)

class Form(View):
    def get(self, request):
        return render(request, 'myapp/form.html')
    
    def post(self, request):
        title = request.POST.get('title')
        content = request.POST.get('description')
        image = request.FILES.get('image')
        author = request.POST.get('teller')
        
        Post.objects.create(
            title=title,
            content=content,
            image=image,
            author=author
        )
        return redirect('homepage') 

class Tale(View):
    def get(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        return render(request, 'myapp/tale.html', {'post': post})

class Detail(View):
    def get(self, request):
        query = request.GET.get('search', '')
        posts = Post.objects.filter(title__icontains=query) if query else Post.objects.all()
        context = {
            'posts': posts,
            'search_query': query
        }
        return render(request, 'myapp/detail.html', context)

class NewsletterSignup(View):
    def post(self, request):
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponse('''
                    <script>
                        alert('Successfully subscribed to our newsletter!');
                        window.location.href = '{}';
                    </script>
                '''.format(request.META.get('HTTP_REFERER', '/')))
            except IntegrityError:
                return HttpResponse('''
                    <script>
                        alert('This email is already subscribed.');
                        window.location.href = '{}';
                    </script>
                '''.format(request.META.get('HTTP_REFERER', '/')))
        else:
            return HttpResponse('''
                <script>
                    alert('Please enter a valid email address.');
                    window.location.href = '{}';
                </script>
            '''.format(request.META.get('HTTP_REFERER', '/')))

    def get(self, request):
        return redirect('homepage')