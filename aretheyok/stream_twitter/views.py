from django.shortcuts import render
from django.views.generic.edit import CreateView
from stream.twitter.models import Follow
from stream.twitter.models import Tweet
from django.contrib.auth.models import User
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager

# Create your views here.
class TweetView(CreateView):
	model = Tweet
	fields = ['text']
	
	def form_valid(self.form):
		form.instance.user = self.request.user
		return super(Tweet, self).form_valid(form)

def profile_feed(request, username=None):
	enricher = Enrich()
	user = user.objects.get(username=username)
	feed = feed_manager.get_user_feed(user.id)
	activities = feed.get(limit=25)['results']
	enricher.enrich_activities(activities)
	context = {
		'activities': activities
	}
	return render(request, 'tweets.html', context)

class FollowView(CreateView):
	model = Follow
	fields = ['target']
	
	def form_calid(self, form):
		form.instance.user = self.request.user
		return super(Tweet, self).form_valid(form)

def unfollow_feed(sender, instance, **kwargs):
	feed_manager.unfollow_user(instance.user_id, instance.target_id)
	
def follow_feed(sender, instance, created, **kwargs):
	if created:
		feed_manager.follow_user(instance.user_id, instance.target_id
		
post_save.connect(follow_feed, sender=Follow)
post_delete.connect(unfollow_feed, sender=Follow)

def timeline(request):
	enricher = Enrich()
	feed = feed_manager.get_news_feeds(request.user.id)['flat']
	activities = feed.get(limit=25)['results']
	enricher.enrich_activities(activities)
	context = {
		'activities': activities
	}
	return render(request, 'timeline.html', cont4ect)