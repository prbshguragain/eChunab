from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Candidate

# Create your views here.

# def all_candidate(request):
    

@login_required(login_url="/accounts/login")
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required(login_url="/accounts/login")
def votes(request):
    candidates = Candidate.objects.all()
    return render(request, 'vote.html',{'candidates': candidates})