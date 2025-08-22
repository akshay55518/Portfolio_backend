from django.shortcuts import render,redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from Portfolio_App.models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
# Admin Login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:  
            login(request, user)
            return redirect("projects")  
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, "login.html")


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect("login")


# Project Management
@csrf_exempt
@login_required(login_url='login')
def project_dashboard(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

@login_required(login_url='login')
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form, 'title': 'Add Project'})

@login_required(login_url='login')
def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form, 'title': 'Edit Project'})

@login_required(login_url='login')
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    project.delete()
    return redirect('projects')

# Experience Management
@csrf_exempt
@login_required(login_url='login')
def experience_dashboard(request):
    experiences = Experience.objects.all()
    return render(request, 'experience.html', {'experiences': experiences})

@login_required(login_url='login')
def experience_create(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('experience')
    else:
        form = ExperienceForm()
    return render(request, 'experience_form.html', {'form': form, 'title': 'Add Experience'})

@login_required(login_url='login')
def experience_edit(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    if request.method == 'POST':
        form = ExperienceForm(request.POST, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('experience')
    else:
        form = ExperienceForm(instance=exp)
    return render(request, 'experience_form.html', {'form': form, 'title': 'Edit Experience'})

@login_required(login_url='login')
def experience_delete(request, pk):
    exp = get_object_or_404(Experience, pk=pk)
    exp.delete()
    return redirect('experience')


# Skills Management
@csrf_exempt
@login_required(login_url='login')
def skills_dashboard(request):
    categories = SkillCategory.objects.prefetch_related("skills").all()

    # Forms for adding
    category_form = SkillCategoryForm()
    skill_form = SkillForm()

    if request.method == "POST":
        if "category_submit" in request.POST:
            category_form = SkillCategoryForm(request.POST)
            if category_form.is_valid():
                category_form.save()
                return redirect('skills')

        elif "skill_submit" in request.POST:
            skill_form = SkillForm(request.POST)
            if skill_form.is_valid():
                skill_form.save()
                return redirect('skills')

    return render(request, "skills.html", {
        "categories": categories,
        "category_form": category_form,
        "skill_form": skill_form,
    })

@login_required(login_url='login')
def skill_edit(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = SkillForm(instance=skill)
    return render(request, "skill_form.html", {"form": form, "title": "Edit Skill"})

@login_required(login_url='login')
def skill_delete(request, pk):
    skill = get_object_or_404(Skill, pk=pk)
    skill.delete()
    return redirect('skills')

@login_required(login_url='login')
def skill_category_edit(request, pk):
    category = get_object_or_404(SkillCategory, pk=pk)
    if request.method == "POST":
        form = SkillCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('skills')
    else:
        form = SkillCategoryForm(instance=category)
    return render(request, "skill_form.html", {"form": form, "title": "Edit Category"})

@login_required(login_url='login')
def skill_category_delete(request, pk):
    category = get_object_or_404(SkillCategory, pk=pk)
    category.delete()
    return redirect('skills')

# Portfolio Management
@csrf_exempt
@login_required(login_url='login')
def portfolio_dashboard(request):
    portfolios = Portfolio.objects.all()
    return render(request, "portfolio.html", {"portfolios": portfolios})

# Create
@login_required(login_url='login')
def portfolio_create(request):
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("portfolio")
    else:
        form = PortfolioForm()
    return render(request, "portfolio_form.html", {"form": form, "title": "Add Portfolio"})

# Edit
@login_required(login_url='login')
def portfolio_edit(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == "POST":
        form = PortfolioForm(request.POST, instance=portfolio)
        if form.is_valid():
            form.save()
            return redirect("portfolio")
    else:
        form = PortfolioForm(instance=portfolio)
    return render(request, "portfolio_form.html", {"form": form, "title": "Edit Portfolio"})

# Delete
@login_required(login_url='login')
def portfolio_delete(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    if request.method == "POST":
        portfolio.delete()
        return redirect("portfolio")
    return render(request, "confirm_delete.html", {"object": portfolio, "title": "Delete Portfolio"})

# Contact Management
@login_required(login_url='login')
def contact_message_list(request):
    if request.method == "POST":
        msg_id = request.POST.get("delete_id")
        if msg_id:
            ContactMessage.objects.filter(id=msg_id).delete()
            return redirect("contact")

    messages = ContactMessage.objects.all().order_by("-created_at")
    return render(request, "contact.html", {"messages": messages})



