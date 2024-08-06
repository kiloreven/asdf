from django.db import models



class Component(models.Model):
    name = models.CharField(max_length=256)
    added_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    room = models.CharField(max_length=64)
    bucket = models.PositiveIntegerField()
    component = models.ForeignKey(Component, null=True, on_delete=models.deletion.SET_NULL)

    def __str__(self):
        return f"{self.room}: {self.bucket} (contains {self.component or 'nada'})"
