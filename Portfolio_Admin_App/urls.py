from django.urls import path
from .views import *

urlpatterns = [
    
    path("", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    
    path('projects', project_dashboard, name='projects'),
    path('projects/add/', project_create, name='project_create'),
    path('projects/<int:pk>/edit/', project_edit, name='project_edit'),
    path('projects/<int:pk>/delete/', project_delete, name='project_delete'),
    
    
    path('experience/', experience_dashboard, name='experience'),
    path('experience/add/', experience_create, name='experience_create'),
    path('experience/<int:pk>/edit/', experience_edit, name='experience_edit'),
    path('experience/<int:pk>/delete/', experience_delete, name='experience_delete'),
    
    path("skills/", skills_dashboard, name="skills"),
    path("skills/edit/<int:pk>/", skill_edit, name="skill_edit"),
    path("skills/delete/<int:pk>/",skill_delete, name="skill_delete"),
    path("skills/category/edit/<int:pk>/", skill_category_edit, name="skill_category_edit"),
    path("skills/category/delete/<int:pk>/",skill_category_delete, name="skill_category_delete"),
    
    path("portfolio/", portfolio_dashboard, name="portfolio"),
    path("portfolio/add/", portfolio_create, name="portfolio_create"),
    path("portfolio/<int:pk>/edit/", portfolio_edit, name="portfolio_edit"),
    path("portfolio/<int:pk>/delete/", portfolio_delete, name="portfolio_delete"),
    
    path("contact/", contact_message_list, name="contact"),
    
]