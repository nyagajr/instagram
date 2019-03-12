from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewsLetterForm

# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
    else:
        form = NewsLetterForm()
    return render(request, 'signup.html')





# def welcome(request):
    # return render(request, 'welcome.html')
