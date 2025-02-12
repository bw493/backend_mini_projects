from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    denji = "Denji: Revving up the server! Chainsaw Django, ready to cut through bugs! 🔪"
    power = "Power: Blood-fueled API responses incoming! Fear me, devils! 🩸"
    aki = "Aki: Mission clear. Django server operational. No devils detected. 🕶️"
    makima = "Makima: Everything is under control. The API obeys my commands. 🐍"
    
    return HttpResponse(f"{denji}<br>{power}<br>{aki}<br>{makima}")