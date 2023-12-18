"""Test app models."""
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class SimpleModel(models.Model):
    """Simple model."""

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    truthy = models.BooleanField(default=True)
    numeric = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta options."""

        verbose_name = "Simple Model"
        verbose_name_plural = "Simple Models"
        db_table = "simple_model"


class RelatedModel(models.Model):
    """Related model."""

    simple = models.ForeignKey(SimpleModel, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    properties = models.JSONField(default=dict)

    class Meta:
        """Meta options."""

        verbose_name = "Related Model"
        verbose_name_plural = "Related Models"
        db_table = "related_model"
