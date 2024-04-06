from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from app.contacts import CONTACTS


def home_page_view(request):
    contact_names = []
    for person in CONTACTS:
        contact_names.append(person.name)
    context = {
        "names": contact_names
    }
    return render(request, "home.html", context)

def contacts_page_view(request, contact):
    for person in CONTACTS:
        if contact == person.name:
            name = person.name
            number = person.number
            email = person.email
            address = person.address
    context = {
        "name": name,
        "number": number,
        "email": email,
        "address": address
    }
    return render(request, "contacts.html", context)