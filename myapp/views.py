from django.shortcuts import render, redirect
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import NewsletterSignupForm
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib import messages

def index(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'myapp/index.html', context)

def form(request):
    if request.method == 'POST':
        # Process form submission
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
        return redirect('homepage')  # Redirect after successful submission
    return render(request, 'myapp/form.html')

# def tale(request):
#     context = {
#         'posts':Post.objects.all()
#     }
#     return render(request, 'myapp/tale.html', context)
def tale(request, post_id):  # Change post_id to pk
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'myapp/tale.html', {'post': post})

def detail(request):
    query = request.GET.get('search', '')
    posts = Post.objects.filter(title__icontains=query) if query else Post.objects.all()
    context = {
        'posts': posts,
        'search_query': query
    }
    return render(request, 'myapp/detail.html', context)

# def newsletter_signup(request):
#     if request.method == 'POST':
#         form = NewsletterSignupForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 messages.success(request, 'Successfully subscribed to our newsletter!')
#                 return HttpResponse('''
#                     <script>
#                         alert('Successfully subscribed to our newsletter!');
#                         window.location.href = '/';
#                     </script>
#                 ''')
#             except IntegrityError:
#                 messages.error(request, 'This email is already subscribed.')
#                 return HttpResponse('''
#                     <script>
#                         alert('This email is already subscribed.');
#                         window.location.href = '/';
#                     </script>
#                 ''')
#         else:
#             messages.error(request, 'Please enter a valid email address.')
#             return HttpResponse('''
#                 <script>
#                     alert('Please enter a valid email address.');
#                     window.location.href = '/';
#                 </script>
#             ''')
#     return redirect('homepage')

def newsletter_signup(request):
    if request.method == 'POST':
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
    return redirect('homepage')