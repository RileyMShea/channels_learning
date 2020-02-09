from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html")


def room(request: HttpRequest, room_name: str) -> HttpResponse:
    return render(request, "chat/room.html", {"room_name": room_name})
