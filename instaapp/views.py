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



# def news_today(request):
#     if request.method == 'POST':
#         form = NewsLetterForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['your_name']
#             email = form.cleaned_data['email']
#             recipient = NewsLetterRecipients(name = name,email =email)
#             recipient.save()
#             HttpResponseRedirect('news_today')
#     else:
#         form = NewsLetterForm()
#     return render(request, 'all-news/today-news.html', {"date": date,"news":news,"letterForm":form})

# def welcome(request):
    # return render(request, 'welcome.html')
