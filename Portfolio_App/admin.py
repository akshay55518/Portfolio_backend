from django.contrib import admin
from .models import *

admin.site.register(Project)

admin.site.register(Portfolio)

admin.site.register(Experience)

admin.site.register(SkillCategory)

admin.site.register(Skill)

admin.site.register(ContactMessage)