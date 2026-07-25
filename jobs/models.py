from django.db import models
from django.urls import reverse


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('Applied', 'Applied'),
        ('Interview', 'Interview'),
        ('Offer', 'Offer'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    ]

    company_name = models.CharField(max_length=150)
    position = models.CharField(max_length=150)
    job_location = models.CharField(max_length=150)
    salary = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='Applied'
    )
    application_date = models.DateField()
    deadline = models.DateField()
    notes = models.TextField(blank=True, max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.company_name} - {self.position}"

    def get_absolute_url(self):
        return reverse('job_detail', kwargs={'pk': self.pk})
