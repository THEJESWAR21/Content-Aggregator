from django.contrib import admin
from .models import Source, Authors, Articles

# TODO: Add a Source Model with all the foreign keys configured

# Register your models here.
admin.site.register(Source)
admin.site.register(Authors)
admin.site.register(Articles)





