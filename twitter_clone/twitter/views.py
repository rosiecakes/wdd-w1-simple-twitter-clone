from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages

from .forms import LoginForm, TweetForm
from .models import User, Tweet


def index(request):
    '''
    If user is not authenticated, show the login page.
    If user is authenticated, direct to tweets.
    '''
    if request.user.is_authenticated():
        username = request.user.username
        return HttpResponseRedirect(reverse('tweets', kwargs={'username':username}))
    
    return redirect('/login')


def userlogin(request):
    '''
    Authenticate, direct to tweets.
    '''
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('tweets', kwargs={'username':username}))
                
            else:
                return HttpResponse(
                    "You Twitter_Clone account has disabled due to lame Tweets, sorry not sorry... Love, Matt")
        else:
            messages.warning(request, 'Invalid login O_o')
            return render(request, 'twitter/feed.html')
    
    return render(request, 'twitter/login.html')
    

def tweets(request, username=None):
    '''
    If user has full URL, even if not authenticated, 
    show the tweet feed for that username. 
    '''
    User = get_user_model()
    
    try:
        get_user = User.objects.get(username=username)
    except User.DoesNotExist:
        messages.warning(request, 'does not exist')
        return render(request, 'twitter/feed.html', {'username':username})
    
    if request.method == "POST":
        tweet = request.POST['tweet']
        new_tweet = Tweet(tweet=tweet, user=get_user)
        new_tweet.save()
        
    tweets = Tweet.objects.filter(user=get_user)
    
    if not tweets:
        messages.warning(request, 'hasn\'t tweeted yet :(')
        return render(request, 'twitter/feed.html', {'username':username})
        
    return render(request, 'twitter/feed.html', {'tweets':tweets, 'username':username})
    

def userlogout(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    
    return render(request, 'twitter/feed.html')

