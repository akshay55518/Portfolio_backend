from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('id')
    serializer_class = ProjectSerializer
    
class PortfolioListView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    
class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all().order_by('id')
    serializer_class = ExperienceSerializer
    
class SkillsAPIView(APIView):
    def get(self, request):
        categories = SkillCategory.objects.all()
        data = {}
        for category in categories:
            skills = category.skills.all()
            data[category.name] = SkillSerializer(skills, many=True).data
        return Response(data)
    
class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

class AboutDetailView(generics.RetrieveAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def get_object(self):
        return About.objects.last()