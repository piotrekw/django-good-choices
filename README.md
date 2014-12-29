django-good-choices
===================

Simple and convenient approach to "choices" in Django

Example:

    from django.db import models
    from django.utils.translation import ugettext_lazy as _
    from good_choices import Choices
    
    class Order(models.Model):
        class Status(Choices):
            PLACED = 1, _('Placed')
            PAID = 2, _('Paid')
            SENT = 3, _('Sent')
            DELIVERED = 4, _('Delivered')
    
        product = models.ForeignKey('Product')
        status = models.SmallIntegerField(
            choices=Status.choices,
            default=Status.PLACED)
