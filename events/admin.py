from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import (
    EventCategory,
    Event,
    JobCategory,
    EventJobCategoryLinking,
    EventMember,
    EventUserWishList,
    UserCoin,
)

admin.site.register(EventCategory)
admin.site.register(Event, MapAdmin)
admin.site.register(JobCategory)
admin.site.register(EventJobCategoryLinking)
admin.site.register(EventMember)
admin.site.register(EventUserWishList)
admin.site.register(UserCoin)
