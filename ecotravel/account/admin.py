from django.contrib import admin
from .models import Accomodation
from .models import Destinations,Selections,BicycleModel
# Register your models here.



admin.site.register(Accomodation)
admin.site.register(Destinations)
admin.site.register(Selections)
admin.site.register(BicycleModel)
