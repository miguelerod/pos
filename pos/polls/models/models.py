from django.db import models
from datetime import datetime
from django.utils.translation import gettext_lazy as _
from datetime import timezone, timedelta


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=19, decimal_places=10)
    price = models.DecimalField(max_digits=19, decimal_places=10)
    purchase_date = models.DateTimeField('date purchased')
    itemCode = models.CharField(max_length=14)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.itemCode}"


class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_num = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    id_doc_num = models.CharField(max_length=100)
    companyName = models.CharField(max_length=50)
    status = models.BooleanField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Order(models.Model):
    items = models.ManyToManyField(Item)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField('order date')

    def __str__(self):
        return f"#{self.id:014}"


class Invoice(models.Model):
    class Status(models.TextChoices):
        VOID = "VO", _("Void")
        PENDING = "PE", _("Pending")
        PAID = "PA", _("Paid")

    class PaymentMethods(models.TextChoices):
        TRANSFER = "TR", _("Transfer")
        CASH = "CA", _("Cash")
        CREDIT_CARD = "CC", _("Credit Card")

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDING
    )
    paymentType = models.CharField(
        max_length=2,
        choices=PaymentMethods.choices,
    )
    emittedDate = models.DateTimeField('emission date', default=datetime.now())
    paidDate = models.DateTimeField('payment date')

    def __str__(self):
        return f"#{self.id:014}"
