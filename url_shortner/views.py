from django.contrib import messages
from django.shortcuts import redirect, render
from url_shortner.models import Urls

# Create your views here.


def index(request):
    
    if request.method == 'POST':
        original_url = request.POST['original_url']
        new_name = request.POST['new_name']

        if not new_name.isalnum():
            messages.error(request, 'The Name should only contain Alphabet and Numbers')
            return redirect('index')

        if Urls.objects.filter(shortened_url=new_name).exists():
            messages.error(request, 'This name is already taken!!!')
            return redirect('index')

        data = Urls.objects.create(original_url=original_url, shortened_url=new_name)

        new_url = f"{request.build_absolute_uri().split('://')[1]}go/{new_name}"

        messages.success(request, 'Congratulations!!!! Your URL has been shortened.')
        messages.info(request, f'Your new url: {new_url}')

    return render(request, 'index.html')


def urlRedirect(request, query):
    url = Urls.objects.filter(shortened_url=query)

    if url.exists():
        for x in url:
            x.save()
        
        return redirect(url.values()[0]['original_url'])
    else:
        return redirect('error')


def error(request):
    return render(request, 'error.html')


def success(request):
    return render(request, 'success.html')
