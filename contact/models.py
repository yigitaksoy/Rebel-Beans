from django.db import models


class Contact(models.Model):
    """
    Contact Model for customers to contact the admin and store owner
    """

    class Meta:
        ordering = ("-message_date",)

    name = models.CharField(max_length=254)
    email = models.EmailField()
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
