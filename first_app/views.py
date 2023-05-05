from django.shortcuts import render
from django.http.response import HttpResponse

my_views={
"one":"the one page ",
"two":"the two page ",
"three":"the three page ",

}


def one_func_to_all(request,topic):
    return HttpResponse(my_views[topic])
   

def The_home_page_inApp(request):
    return render(request,"index.html")

# Create your views here.
