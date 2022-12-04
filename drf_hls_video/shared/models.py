from django.db import models
import uuid


class UUIDModel(models.Model):
    """
    Custom model with basic fields
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    hidden = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    editable = models.BooleanField(default=True)  # prevent changes
    locked = models.BooleanField(default=False)  # prevent deletion
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
