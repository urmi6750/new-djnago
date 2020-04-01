from django.shortcuts import render
posts=[
   {'author':'urmi',
   'content':'pandemic',
    'title':'blog -1',
    'date':'28 th march'


},
   {
      'author':'fariya',
      'content':'Govt',
      'title':'blog -2',
      'date':'28 th march'

   }

]
def home (request):

    return render(request,'blog-app/homepage.html',context={'posts':posts})
def about(request):
    return  render(request,'blog-app/about.html')
