from django.shortcuts import render, redirect, get_object_or_404
from .models import Bug
from .forms import BugForm

# Create your views here.
def index(request):

    bug_list = Bug.objects.all()
    return render(request, 'index.html', {'bug_list': bug_list})

def register_bug(request):
    if request.method == 'POST':
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BugForm()
    return render(request, 'register_bug.html', {'form': form})

def bug_details(request, bug_id):
    bug = get_object_or_404(Bug, pk=bug_id)
    return render(request, 'bug_details.html', {'bug': bug})


