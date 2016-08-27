from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .forms import RegisterForm, LoginForm, TweetForm
from .models import User, Tweet


def index(request):
	'''
	If user is not authenticated, show the login page.
	If user is authenticated, show own tweets, and allow
	to post and delete.
	'''

	# if user not authenticated, show login form, logic handled below

	# if user is authenticated, show textarea for new tweet, list of tweets,
	# and delete buttons for each tweet

	# if request method is POST, check to see whether it is too delete a tweet,
	# or to post a new tweet (not sure how we do that)

	# if new tweet, save to db, show success / toast message, otherwise show error

	# if delete tweet, use delete() method, show success / toast that it's
	# been deleted
	
	# if not request.user.is_authenticated():
	# 	return HttpResponseRedirect(reverse('user_login'))

	return render(request, 'twitter/index.html')


def user-login(request):
    '''
    Will log a user in with cookies / CSRF junk, check user.is_authenticated.
    Note as well the tests use an imported method called "get_user_model()"
    '''
    form = LoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('username-hp'))
            else:
                return HttpResponse(
                    "You Twitter_Clone account has disabled due to lame Tweets, sorry not sorry...")
        else:
            print(
                "Invalid login credentials: {0}, {1}".format(
                    username, password))
            return HttpResponse("Invalid login.")
    else:
        return render(request, 'twitter/login.html')
        

def user_logout(request):
	pass

'''
def register(request):
	
	registered = False
	
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		
		if user_form.is_valid() and profile_form.is_valid():
			# save data to db
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()
			registered = True
			
		else:
			print(user_form.errors, profile_form.errors)
		
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
		
	return render(request, 'twitter/register.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
'''
	
def username(request, username):
	'''
	If user has full URL, even if not authenticated, 
	show the tweet feed for that username.
	'''
	# get the id for the user because that is what we need to get their tweets,
	# the readme shows "@jack hasn't tweeted yet - added exception for no tweets
	try:
		user_id = User.objects.get(username = username).id
	except User.DoesNotExist:
		message = messages.error(request, 'does not exist')
		context = {'username':username, 'message': messages}
		
		return render(request, 'twitter/feed.html', context)
	
	# grab their tweets, note all() did not work here, must filter by ID to get a proper iterable
	tweets = Tweet.objects.filter(user = user_id)
	
	if not tweets:
		message = messages.info(request, 'hasn\'t tweeted yet :(')
		context = {'username':username, 'message': messages}
		
		return render(request, 'twitter/feed.html', context)
		
	# for the tweet view will need tweet info and username, pass that stuff
	context = {'tweets': tweets, 'username': username}
	
	return render(request, 'twitter/feed.html', context)
	


# from rose - pretty sure we don't need this
# def register(request):
# 	form = RegisterForm()
# 	return render(request, 'login.html', {'form' : form})
	
# from rose - I don't think we need this either
# def tweet(request):
#     form = TweetForm()
#     return render(request, 'xyz.html', {'form' : form})
