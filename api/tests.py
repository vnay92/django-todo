# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Note

class ModelTestCase(TestCase):
    """This class defines the test suite for the note model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.note_name = "Write world class code"
        self.Note = Note(name=self.note_name)

    def test_model_can_create_a_note(self):
        """Test the note model can create a note."""
        old_count = Note.objects.count()
        self.Note.save()
        new_count = Note.objects.count()
        self.assertNotEqual(old_count, new_count)
