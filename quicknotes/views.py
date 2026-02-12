from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from django.views.decorators.http import require_POST
from quicknotes_site.forms import NoteForm


def home(request):
    return HttpResponse("Welcome Home!")


def api_notes(request):
    data = list(Note.objects.values())
    return JsonResponse({'notes': data})
