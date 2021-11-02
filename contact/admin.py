from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """ Add User Contact Section for the Admin Backend """

    list_display = ('name', 'email', 'subject', 'message',
                    'message_date',)
    
    readonly_fields = (
        'name', 'email', 'subject', 'message',
        'message_date',
    )

    ordering = ('-message_date',)


admin.site.register(Contact, ContactAdmin)