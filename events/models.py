from django.db import models
from django.urls import reverse
from mapbox_location_field.models import LocationField
from ckeditor_uploader.fields import RichTextUploadingField


class EventCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=6, unique=True)
    image = models.ImageField(upload_to='event_category/')
    priority = models.IntegerField(unique=True)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event-category-list')


class Event(models.Model):
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    uid = models.PositiveIntegerField(unique=True)
    description = RichTextUploadingField()
    scheduled_status = models.IntegerField()
    venue = models.CharField(max_length=255)
    agenda = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    location = LocationField()
    points = models.PositiveIntegerField()
    maximum_attende = models.PositiveIntegerField()
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='event_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='event_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('event-list')


class JobCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class EventJobCategoryLinking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    status = models.IntegerField()

    def __str__(self):
        return str(self.event)


class EventMember(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    attend_status = models.IntegerField()
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventmember_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventmember_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()


    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('join-event-list')


class EventUserWishList(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventwishlist_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventwishlist_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()


    class Meta:
        unique_together = ['event', 'user']

    def __str__(self):
        return str(self.event)
    
    def get_absolute_url(self):
        return reverse('event-wish-list')


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_image/')
    position = models.PositiveIntegerField(unique=True)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventimage_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventimage_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return str(self.event)


class UserCoin(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    gain_type = models.PositiveIntegerField()
    gain_coin = models.PositiveIntegerField()
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='usercoin_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='usercoin_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return str(self.user)


class EventNotofication(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventnotification_created_user')
    updated_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='eventnotification_updated_user')
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return str(self.event)


class EventNotoficationHistory(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    notification = models.ForeignKey(EventNotofication, on_delete=models.CASCADE)
    user_view_status = models.PositiveIntegerField()
    user_view_date = models.DateField(auto_now_add=True)
    status = models.IntegerField()

    def __str__(self):
        return str(self.notification)









