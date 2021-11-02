from django.db import models


class Contact(models.Model):
    """
    Contact Model for customers to contact the admin and store owner
    """

    subject = (
    ('general', 'General Questions'),
    ('product_information', 'Product Information'),
    ('order_status', 'Order Status'),
    ('shipping_delivery', 'Shipping and Delivery'),
    ('bulk_purchasing', 'Wholesale Purchasing'),)
    
    class Meta:
        ordering = ("-message_date",)
        
        verbose_name_plural = 'Messages'

    name = models.CharField(max_length=254)
    email = models.EmailField()
    subject = models.CharField(max_length=254, choices=subject,
                               default='general')
    message = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
