# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Note(models.Model):

    """This class represents the bucketlist model."""
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
