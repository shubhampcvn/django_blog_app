from django.shortcuts import render


def home_screen_view(request):
    context = {}
    context['some_string']= 'sample string'
    return render(request, "personal/home.html", context)