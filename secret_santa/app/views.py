from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app.repositories import SantaRepository
from app.domain.participants import GenerateAndSaveDraw, UpdateParticipantList, GetParticipantList, GetDrawList
import json

def base(request):
    return render(request, "base.html", {})

@csrf_exempt
def participants(request):
    if request.method == "POST":
        data = json.loads(request.body)
        UpdateParticipantList(SantaRepository()).execute(data["plist"])
        return HttpResponse(b"OK")
    if request.method == "GET":
        return JsonResponse({"data": GetParticipantList(SantaRepository()).execute()})


@csrf_exempt
def draw(request):
    santa_repo = SantaRepository()
    if request.method == "POST":
        GenerateAndSaveDraw(santa_repo).execute()
        return HttpResponse(b"OK")
    if request.method == "GET":
        draw_list = GetDrawList(santa_repo).execute()
        print("draw_list", draw_list)
        return JsonResponse({"data": draw_list})
