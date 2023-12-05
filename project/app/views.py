# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from django.shortcuts import get_object_or_404

# views.py

def list_contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'myapp/list_contacts.html', {'contacts': contacts})


def add_contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phno = request.POST.get("phno")
        age = request.POST.get("age")
        from_destination = request.POST.get("from_destination")
        to_destination = request.POST.get("to_destination")
        airplane_no = request.POST.get("airplane_no")
        seat_no = request.POST.get("seat_no")

        Contact.objects.create(
            name=name,
            email=email,
            phno=phno,
            age=age,
            from_destination=from_destination,
            to_destination=to_destination,
            airplane_no=airplane_no,
            seat_no=seat_no
        )
        return redirect('list_contacts')

    return render(request, 'myapp/add_contact.html', {})

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        # Process the form data and update the contact
        name = request.POST.get("name")
        email = request.POST.get("email")
        phno = request.POST.get("phno")
        age = request.POST.get("age")
        from_destination = request.POST.get("from_destination")
        to_destination = request.POST.get("to_destination")
        airplane_no = request.POST.get("airplane_no")
        seat_no = request.POST.get("seat_no")

        contact.name = name
        contact.email = email
        contact.phno = phno
        contact.age = age
        contact.from_destination = from_destination
        contact.to_destination = to_destination
        contact.airplane_no = airplane_no
        contact.seat_no = seat_no

        contact.save()
        return redirect('list_contacts')

    return render(request, 'myapp/edit_contact.html', {'contact': contact})


def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('list_contacts')

