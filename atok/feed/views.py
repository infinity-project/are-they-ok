from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views import generic


from .models import Update, Verify

# Create your views here.
class IndexView(generic.ListView):
	template_name = 'feed/index.html'
	context_object_name = 'latest_update_list'
	
	def get_queryset(self):
		return Update.objects.order_by('-pub_date')[:5]
	
class DetailView(generic.DetailView):
    model = Update
    template_name = 'feed/detail.html'
    
def verify(request, update_id):
	update = get_object_or_404(Update, pk=update_id)
	try:
		selected_verify = update.verify_set.get(pk=request.POST['verify'])
	except (KeyError, Verify.DoesNotExist):
		return render(request, 'feed/verify.html', {
			'update': update,
			'error_message': "Please select a level.",
		})
	else:
		selected_verify.affirmations += 1
		selected_verify.save()
		return HttpResponseRedirect(reverse('feed:detail', args=(update.id,)))
	
def profile(request, pk):
	user = User.objects.filter(pk=pk)
	return render(request, 'feed/profile.html', {'user': user})

def index_user(request, username):
    updates = Update.objects.filter(user__username__iexact=username)
    return render(request, 'feed/index.html', {
        'updates': updates,
        'reason': "Viewing all of {}'s updates".format(username)
    })