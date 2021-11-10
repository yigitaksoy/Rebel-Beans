from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm


def contact(request):
    """ 
    Contact Page view for customers to contact the Admin
        Args:
            request
        Returns:
            renders contact page template
    """

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            # Gathers user information from the form, and sends email to the Admin
            name = contact_form.cleaned_data['name']
            email = contact_form.cleaned_data['email']
            subject = contact_form.cleaned_data['subject']
            message = contact_form.cleaned_data['message']

            subject = render_to_string(
                'contact/confirmation/subject.txt',
                {'subject': subject})
            body = render_to_string(
                'contact/confirmation/body.txt',
                {'message': message, 'email': email, 'name': name})

            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False
            )

            messages.success(request, 'Your message has been sent!')
            return redirect(reverse('contact'))
        else:
            messages.error(request, 'Oops! Something went wrong with your form!')
    else:
        contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }
    template = 'contact/contact.html'
    return render(request, template, context)