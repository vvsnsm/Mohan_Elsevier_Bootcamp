from django.shortcuts import render

from django.http import HttpResponse

def friends(request):
    return render (request,'friends/friends.html')
