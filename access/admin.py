from django.contrib import admin

# Register your models here.
from access.models import Profile, Store, Licence

admin.site.register(Profile)
admin.site.register(Store)
admin.site.register(Licence)