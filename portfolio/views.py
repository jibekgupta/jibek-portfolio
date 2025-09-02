# portfolio/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Project, Skill, Contact, Experience, Education

def home(request):
    """Home page view with all sections"""
    
    # Handle contact form submission
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if name and email and subject and message:
            # Save to database
            contact = Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            
            # Send email (optional)
            try:
                send_mail(
                    subject=f"Portfolio Contact: {subject}",
                    message=f"From: {name} ({email})\n\n{message}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=['jibekgupta059@gmail.com'],
                    fail_silently=False,
                )
            except Exception as e:
                print(f"Email sending failed: {e}")
            
            messages.success(request, 'Thank you for your message! I\'ll get back to you soon.')
            return redirect('home')
        else:
            messages.error(request, 'Please fill in all fields.')
    
    # Get data for the page
    projects = Project.objects.filter(featured=True)[:6]
    skills = Skill.objects.all()
    experiences = Experience.objects.all()[:3]
    education = Education.objects.all()
    
    # Organize skills by category
    skills_by_category = {}
    for skill in skills:
        category = skill.get_category_display()
        if category not in skills_by_category:
            skills_by_category[category] = []
        skills_by_category[category].append(skill)
    
    context = {
        'projects': projects,
        'skills_by_category': skills_by_category,
        'experiences': experiences,
        'education': education,
    }
    
    return render(request, 'portfolio/home.html', context)

def project_detail(request, pk):
    """Individual project detail view"""
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})