from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    problem = models.TextField()
    approach = models.TextField()
    techStack = models.TextField()
    results = models.TextField()
    link = models.URLField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    category = models.TextField()
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    time = models.CharField(max_length=100) 
    work_done = models.JSONField() 

    def __str__(self):
        return f"{self.role} at {self.company}"
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g. "Programming Languages"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # e.g. "Python"
    level = models.PositiveIntegerField()  # percentage (0-100)

    def __str__(self):
        return f"{self.name} ({self.level}%)"
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"