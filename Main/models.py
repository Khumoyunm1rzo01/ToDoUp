from tabnanny import verbose
from django.db import models

# Create your models here.

class ToDo(models.Model):
    task = models.CharField(max_length=255, verbose_name="Ma'lumot")
    date = models.DateField(verbose_name="Sana")
    status = models.BooleanField(default=False,verbose_name="Holati")

    class Meta:
        verbose_name_plural = "Qilinishi kerak bo'lgan ishlar!"
    
    def __str__(self):
        return self.task

class DeletedTodo(models.Model):
    task = models.CharField(max_length=255, verbose_name="Ma'lumot")
    date = models.DateField(verbose_name="Sana")
    status = models.BooleanField(default=False, verbose_name="Holati")
    deleted_time = models.DateTimeField(auto_now_add=True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      