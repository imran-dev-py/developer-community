from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.decorators import login_required

def projects(request):
	projects = models.Project.objects.all()
	context = {'projects': projects}
	return render(request, 'projects/projects.html', context=context)

def project(request, pk):
	project = models.Project.objects.get(id=pk)
	tags = project.tags.all()
	reviews = project.reviews.all()
	context = {'project': project, 'tags': tags, 'reviews': reviews}
	return render(request, 'projects/single-project.html', context)

def create_project(request):
	form = forms.ProjectForm()
	# profile = request.user.profile

	if request.method == 'POST':
		form = forms.ProjectForm(request.POST, request.FILES)

		if form.is_valid():
			# project = form.save(commit=False)
			# project.owner = profile 
			# project.save()
			form.save()
			return redirect('projects')

	context = {'form': form}
	return render(request, 'projects/project-form.html', context)

def update_project(request, pk):
	project = models.Project.objects.get(id=pk)
	form = forms.ProjectForm(instance=project)

	if request.method == 'POST':
		form = forms.ProjectForm(request.POST, request.FILES, instance=project)
		if form.is_valid():
			form.save()
			return redirect('projects')

	context = {'form': form}
	return render(request, 'projects/project-form.html', context)

def delete_project(request, pk):
	project = models.Project.objects.get(id=pk)

	if request.method == 'POST':
		project.delete()
		return redirect('projects')
	
	return render(request, 'projects/delete-project.html', context={'object': project})
