from django.contrib import admin
from .models import Listing, Message


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_request', 'price', 'created_at')
    list_filter = ('is_request',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'sender', 'recipient', 'listing', 'created_at')
    search_fields = ('sender_name', 'content')
