from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Task


@receiver(post_save, sender=Task)
def send_notification(sender, instance, created, **kwargs):
    if created:
        if instance.executors:
            subject = f"You get a new task {instance.title}!"
            body = f"Task id: {instance.id}, author: {instance.author} created at: {instance.created_at}"
            for executor in list(instance.executors.values()):
                user = User.objects.get(id=executor['id'])
                if user.email:
                    user.email_user(subject, body, fail_silently=False)
