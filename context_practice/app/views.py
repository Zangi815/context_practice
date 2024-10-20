from django.shortcuts import render

def ip_address_processor(request):
    return {'ip_address': request.META['REMOTE_ADDR']}

def index(request):
    return render(request, 'index.html', ip_address_processor(request))


def user_info(request):
    context = {
        'username' : 'rezo',
        'password' : 'nigger123',
        'height' : "5'4ft" 
    }
    return render(request, 'user.html', context=context)