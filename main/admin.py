from django.contrib import admin
from .models import ContactMessage, Page, SiteSetting, FocusArea, Testimonial


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_per_page = 20
    readonly_fields = ['created_at']

    fieldsets = (
        ('Sender Information', {
            'fields': ('name', 'email')
        }),
        ('Message Details', {
            'fields': ('subject', 'message', 'is_read')
        }),
        ('Meta Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'is_published', 'created_at']
    list_filter = ['is_published', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Page Information', {
            'fields': ('title', 'slug', 'content', 'is_published')
        }),
        ('SEO Information', {
            'fields': ('meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Meta Information', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at', 'updated_at']


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ['site_name', 'contact_email', 'contact_phone']

    def has_add_permission(self, request):
        # Only one instance should exist
        return not SiteSetting.objects.exists()


@admin.register(FocusArea)
class FocusAreaAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'order', 'is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('Focus Area Information', {
            'fields': ('title', 'icon', 'description')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'is_featured', 'created_at']
    list_filter = ['is_featured', 'created_at']
    search_fields = ['name', 'role', 'content']
    list_editable = ['is_featured']

    fieldsets = (
        ('Testimonial Information', {
            'fields': ('name', 'role', 'content', 'image', 'is_featured')
        }),
        ('Meta Information', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )

    readonly_fields = ['created_at']


from .models import HeroSlider, HomeContent


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['order', 'is_active']
    search_fields = ['title', 'subtitle']

    fieldsets = (
        ('Slider Content', {
            'fields': ('title', 'subtitle', 'image')
        }),
        ('Call to Action', {
            'fields': ('button_text', 'button_url')
        }),
        ('Display Settings', {
            'fields': ('order', 'is_active')
        }),
    )


@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    list_display = ['section_title', 'order', 'is_active']
    list_filter = ['is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['section_title', 'content']