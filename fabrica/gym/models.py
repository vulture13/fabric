from django.db import models

class Work(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название станка')
    worker = models.CharField(max_length=50, verbose_name='Имя работника')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Станок'
        verbose_name_plural = 'Станки'
        ordering = ['-published']    
