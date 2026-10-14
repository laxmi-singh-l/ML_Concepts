from django.db import models
from django.contrib.auth.models import User


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='progress')
    completed_modules = models.JSONField(default=list)
    current_module = models.IntegerField(default=1)
    badges = models.JSONField(default=list)
    notes = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Module {self.current_module}"

    def is_module_completed(self, module_id):
        return module_id in self.completed_modules

    def complete_module(self, module_id):
        if module_id not in self.completed_modules:
            self.completed_modules.append(module_id)
            if module_id >= self.current_module:
                self.current_module = module_id + 1
            self.save()

    def add_badge(self, badge_name):
        if badge_name not in self.badges:
            self.badges.append(badge_name)
            self.save()


class UserNote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_notes')
    module_slug = models.CharField(max_length=50)
    section = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at']

    def __str__(self):
        return f"{self.user.username} - {self.module_slug}: {self.section}"