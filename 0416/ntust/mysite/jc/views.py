from django.shortcuts import render_to_response
from .models import User

# Create your views here.
def index(requset):
	user=User.objects.all()
	return render_to_response('jc/menu.html',locals())
