from django import forms
from .models import Listing, Message


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "location", "is_request", "price"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["sender_name", "content"]
