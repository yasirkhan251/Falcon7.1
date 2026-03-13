from django.contrib import admin
from .models import Booking, BookingAddress, BookingStatus

# ==========================================
# INLINES (Shows related data on the main Booking page)
# ==========================================

class BookingAddressInline(admin.StackedInline):
    model = BookingAddress
    can_delete = False
    verbose_name_plural = 'Customer Address & Coordinates'
    # Group the address fields neatly
    fields = ('house_no', 'building_name', 'street', 'landmark', 'coordination', 'city', 'state', 'pincode', 'country')
    readonly_fields = ('coordination',) # Optional: make coords read-only so admins don't accidentally break them

class BookingStatusInline(admin.TabularInline):
    model = BookingStatus
    extra = 1 # Allows adding a new status directly from the booking page
    readonly_fields = ('updated_at',)
    fields = ('status', 'updated_at')
    verbose_name_plural = 'Status History'


# ==========================================
# MAIN BOOKING ADMIN
# ==========================================

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    # What columns show up on the main list page
    list_display = ('order_id', 'user', 'service_name', 'purpose', 'status', 'booking_date')
    
    # Filter sidebar on the right
    list_filter = ('status', 'service_type', 'booking_date', 'created_at')
    
    # Search bar (Searches by Order ID, Token, Username, or Phone)
    search_fields = ('order_id', 'token', 'user__username', 'phone', 'service_name', 'model')
    
    # Fields that cannot be edited manually
    readonly_fields = ('sequence_number', 'token', 'order_id', 'created_at')
    
    # Attach the Address and Status models to this page
    inlines = [BookingAddressInline, BookingStatusInline]

    # Organize the form into clean sections
    fieldsets = (
        ('Order Tracking', {
            'fields': (('order_id', 'token', 'status'), 'sequence_number')
        }),
        ('Customer Info', {
            'fields': ('user', 'phone')
        }),
        ('Device & Service Details', {
            'fields': ('service_type', 'service_name', 'model', 'purpose', 'description')
        }),
        ('Schedule', {
            'fields': ('booking_date', 'created_at')
        }),
    )


# ==========================================
# STANDALONE ADMINS (Optional, but good for searching globally)
# ==========================================

@admin.register(BookingAddress)
class BookingAddressAdmin(admin.ModelAdmin):
    list_display = ('booking', 'city', 'pincode', 'coordination')
    search_fields = ('booking__order_id', 'booking__user__username', 'street', 'city', 'pincode')
    list_filter = ('city', 'state')

@admin.register(BookingStatus)
class BookingStatusAdmin(admin.ModelAdmin):
    list_display = ('booking', 'status', 'updated_at')
    search_fields = ('booking__order_id',)
    list_filter = ('status', 'updated_at')