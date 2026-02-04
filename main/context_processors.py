from .models import SiteSetting, FocusArea, HeroSlider, HomeContent


def site_info(request):
    try:
        settings = SiteSetting.objects.get(pk=1)
    except SiteSetting.DoesNotExist:
        settings = SiteSetting.objects.create()

    focus_areas = FocusArea.objects.filter(is_active=True).order_by('order')
    hero_slides = HeroSlider.objects.filter(is_active=True).order_by('order')
    home_content = HomeContent.objects.filter(is_active=True).order_by('order')

    return {
        'site_name': settings.site_name,
        'site_slogan': settings.site_slogan,
        'contact_email': settings.contact_email,
        'contact_phone': settings.contact_phone,
        'address': settings.address,
        'facebook_url': settings.facebook_url,
        'twitter_url': settings.twitter_url,
        'instagram_url': settings.instagram_url,
        'youtube_url': settings.youtube_url,
        'focus_areas': focus_areas,
        'hero_slides': hero_slides,
        'home_content': home_content,
    }