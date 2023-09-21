
from django.shortcuts import render, redirect
from .forms import ResumeForm

def generate_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume:thank_you')
    else:
        form = ResumeForm()
    return render(request, 'resume_generator/generate_resume.html', {'form': form})

def thank_you(request):
    return render(request, 'resume_generator/thank_you.html')
