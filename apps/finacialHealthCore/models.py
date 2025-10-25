from uuid import uuid4 as uuid
from django.db import models
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import TimeStampedModel


# Create your models here.

class BaseModel(TimeStampedModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid,
        editable=False
    )

    class Meta:
        abstract = True


class Customer(BaseModel):
    pass


class Account(BaseModel):
    class EnumTipo(models.TextChoices):
        CREDITO = "CR", _("Crédito")
        AHORRO = "SA", _("Ahorro")
        DEBITO="CH",_("Cheque")


    type_card = models.CharField(
        choices=EnumTipo,
        default=None,
        max_length=2
    )


class Income(BaseModel):
    class EnumTipo(models.TextChoices):
        DEPOSITO="DE",_("Deposito")
        TRANSFER="TR",_("Transferencia")
        
    amount_type=models.DecimalField(max_digits=10, decimal_places=2)
    name_type=models.CharField(max_length=100)
    type_income = models.CharField(
        choices=EnumTipo,
        default=None,
        max_length=2
    )
    
class Expense(BaseModel):
    class EnumTipo(models.TextChoices):
        DEPOSITO="DE",_("Deposito")
        TRANSFERENCIA="TR",_("Transferencia")
        FACTURA="BI",_("Factura")
        PURCHASE="PU",_("Compra")
        WITHDRAWAL="WI", _("Retiro")
        
    amount_type=models.DecimalField(max_digits=10, decimal_places=2)
    name_type=models.CharField(max_length=100)
    type_income = models.CharField(
        choices=EnumTipo,
        default=None,
        max_length=2
    )
    
