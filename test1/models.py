from django.db import models

class Davlat(models.Model):
    nomi=models.CharField(max_length=50)
    poytaxti=models.CharField(max_length=50)
    aholisi=models.IntegerField()
    mustaqillik_yili=models.DateTimeField()
    desc=models.TextField(blank=True,null=True)

    def __str__(self):
        return f'nomi={self.nomi}'
