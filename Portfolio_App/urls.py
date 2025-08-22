from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('portfolio/',PortfolioListView.as_view(), name='portfolio'),
    path('experience/', ExperienceListView.as_view(), name='experience-list'),
    path("skills/", SkillsAPIView.as_view(), name="skills-api"),
    path("contact/", ContactMessageCreateView.as_view(), name="contact-create"),
]