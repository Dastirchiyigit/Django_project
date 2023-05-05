from django.http.response import HttpResponse

def The_home_page_inApp(request):
    return render(request,"static/index.html")