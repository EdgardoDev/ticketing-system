from django.http import HttpResponse
from django.shortcuts import render
from ticketing.models import Ticket
import random
import string

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def index(request):
    return render(request, "index.html")

def submit(request):
    if request.method == "POST":
        username = request.POST.get("username")
        body = request.POST.get("body")
        new_ticket = Ticket(submitter=username, body=body)
        new_ticket.save()
        return HttpResponse("The ticket has been successfully submitted!")
    return render(request, "submit.html")

def tickets(request):
    all_tickets = Ticket.objects.all()
    return render(request, "tickets.html", {"tickets": all_tickets})