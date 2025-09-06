from rest_framework import serializers,status
from .models import Project, Portfolio, Experience, Skill, SkillCategory, ContactMessage, About


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ["name", "level"]


class SkillCategorySerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True)

    class Meta:
        model = SkillCategory
        fields = ["name", "skills"]
        
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = [
            "name",
            "email",
            "mobile",
            "location",
            "role",
            "description1",
            "description2",
            "instagram",
            "github",
            "linkedin",
        ]