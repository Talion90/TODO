from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="task_author")
    executors = models.ManyToManyField(User, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_TYPE = (
        (0, 'TODO'),
        (1, 'IN PROGRESS'),
        (2, 'DONE'),
        (3, 'BLOCKED')
    )
    status = models.IntegerField(
        choices=STATUS_TYPE,
        default=0
    )

    def __str__(self):
        return f"task {self.title}"

    class Meta:
        get_latest_by = "created_at"


class Image(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task_image')
    image = models.ImageField(upload_to='task_images')
