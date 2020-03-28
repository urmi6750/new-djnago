from django.shortcuts import render
def home (request):
    return render(request,'blog-app/homepage.html')
def about(request):
    return  render(request,'blog-app/about.html')