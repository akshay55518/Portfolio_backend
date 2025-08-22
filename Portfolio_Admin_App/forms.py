from django import forms
from Portfolio_App.models import Project, Experience, SkillCategory, Skill,Portfolio, ContactMessage

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'problem', 'approach', 'techStack', 'results', 'link']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ExperienceForm(forms.ModelForm):
    work_done = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        help_text="Enter one task per line"
    )

    class Meta:
        model = Experience
        fields = ['company', 'role', 'time', 'work_done']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Apply form-control to all fields
        for field_name, field in self.fields.items():
            if field_name != 'work_done':  # work_done already styled above
                field.widget.attrs['class'] = 'form-control'

        # Pre-fill work_done as plain text (tasks per line)
        if self.instance and isinstance(self.instance.work_done, dict):
            tasks = self.instance.work_done.get("tasks", [])
            self.initial['work_done'] = "\n".join(tasks)

    def clean_work_done(self):
        data = self.cleaned_data['work_done']
        tasks = [line.strip() for line in data.splitlines() if line.strip()]
        return {"tasks": tasks}


class SkillCategoryForm(forms.ModelForm):
    class Meta:
        model = SkillCategory
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(SkillCategoryForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['category', 'name', 'level']

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            
class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'category', 'description', 'link']

    def __init__(self, *args, **kwargs):
        super(PortfolioForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'