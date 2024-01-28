from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name="Título")
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(null=False, blank=False,verbose_name="Data de entrega")
    finished_at = models.DateField(null=True)
