from django.contrib import admin

from user.models import Company, Person

admin.site.register(Person)
admin.site.register(Company)
