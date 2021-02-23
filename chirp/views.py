from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests

from .models import Chirp

# Create your views here.

#view for the index page
def index(request):

    # get all chirps in descending recency order
    chirps = Chirp.objects.all().order_by("-id")

    # get message in session variable to pass to the template
    message = None
    if 'message' in request.session.keys():
        message=request.session['message']
        del request.session['message']

    # if there is a message send it with context
    if message:
        context = {'chirps': chirps, 'message': message}
    else:
        context = {'chirps': chirps}
    
    return render(request, 'chirp/index.html', context)

def new(request):

    try:
        #save chirp to database
        chirp = Chirp(text=request.POST['chirp'].upper())
        chirp.save()
        request.session['message'] = "Chirp successfully added!"

        # make api call
        apiurl =  "https://bellbird.joinhandshake-internal.com/push"
        payload = {"chirp_id": chirp.id}
        response = requests.post(apiurl, params=payload)

    except:

        #display error message
        request.session['message'] = "Chirp Adding Error :( "
    
    # chirps = Chirp.objects.all()
    # context = {"chirps": chirps, "message": message}
    return redirect(reverse('chirp:index'))

