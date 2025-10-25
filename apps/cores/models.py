from uuid import uuid4 as uuid
from django.db import models
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