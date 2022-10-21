from django.contrib import admin
from . models import User, Topic, Category, Chapter, Level, MultipleChoice

# Register your models here.
admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Category)
admin.site.register(Chapter)
admin.site.register(Level)
admin.site.register(MultipleChoice)