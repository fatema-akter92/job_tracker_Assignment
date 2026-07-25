from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import JobApplication
from .forms import JobApplicationForm


def home(request):
    total = JobApplication.objects.count()
    status_counts = {
        status_key: JobApplication.objects.filter(status=status_key).count()
        for status_key, _ in JobApplication.STATUS_CHOICES
    }
    context = {
        'total': total,
        'status_counts': status_counts,
    }
    return render(request, 'home.html', context)


def job_list(request):
    jobs = JobApplication.objects.all()
    return render(request, 'jobs/list.html', {'jobs': jobs})


def job_create(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job application added successfully!')
            return redirect('job_list')
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/create.html', {'form': form})


def job_update(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(request, 'Job application updated successfully!')
            return redirect('job_list')
    else:
        form = JobApplicationForm(instance=job)
    return render(request, 'jobs/update.html', {'form': form, 'job': job})


def job_delete(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    if request.method == 'POST':
        job.delete()
        messages.success(request, 'Job application deleted successfully!')
        return redirect('job_list')
    return render(request, 'jobs/delete.html', {'job': job})


def job_detail(request, pk):
    job = get_object_or_404(JobApplication, pk=pk)
    return render(request, 'jobs/detail.html', {'job': job})
