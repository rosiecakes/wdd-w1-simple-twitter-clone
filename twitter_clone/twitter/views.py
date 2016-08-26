from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegisterForm, LoginForm, TweetForm
from .models import User, Tweet


# Create your views here.

def index(request):
	'''
	If user is not authenticated, show the login page. 
	If user is authenticated, show own tweets, 
	as well as an input box above to input new tweets.
	'''
	return render(request, 'twitter/index.html')


def login(request):
	'''
	I don't really know how this works with cookies / CSRF junk,
	but I know Django has an is_authenticated method we can leverage.
	Note as well the tests use an imported method called "get_user_model()"
	'''
	form = LoginForm()
	return render(request, 'login.html', {'form' : form})
	
	
def username(request, username):
	'''
	If user has full URL, even if not authenticated, 
	show the tweet feed for that username.
	'''
	# get the id for the user because that is what we need to get their tweets
	user_id = User.objects.get(username = username).id
	
	# grab their tweets, note all() did not work here, must filter by ID to get a proper iterable
	tweets = Tweet.objects.filter(user = user_id)
	
	# for the tweet view will need tweet info and username, pass that stuff
	context = {'tweets': tweets, 'username': username}
	
	return render(request, 'twitter/browsing_other_user_feed.html', context)
	

# from rose - pretty sure we don't need this
# def register(request):
# 	form = RegisterForm()
# 	return render(request, 'login.html', {'form' : form})
	
# from rose - I don't think we need this either
# def tweet(request):
#     form = TweetForm()
#     return render(request, 'xyz.html', {'form' : form})