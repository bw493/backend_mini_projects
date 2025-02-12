from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    data = {
        "David": "Hey, choom! Welcome to the API. Remember, in Night City, you either burn out or fade away. Let's make sure you burn bright!",
        "Lucy": "Welcome to the API, netrunner. Keep your guard up—trust no one, not even your own code.",
        "Rebecca": "Yo, newbie! Welcome to the API. If you mess up, I’ll blast ya! But don’t worry, I’ve got your back... probably.",
        "Kiwi": "Welcome to the API, choom. Remember: Never trust a soul in Night City. Keep your eyes open and your firewalls tighter than a corpo’s vault.",
    }
    return JsonResponse(data, json_dumps_params={'indent': 4})  # Pretty-print JSON