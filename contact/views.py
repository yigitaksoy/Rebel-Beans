from django.shortcuts import render

def contact(request):
    """" A view to return the Contact Page and Contact Form """

    return render(request, "contact/contact.html")
