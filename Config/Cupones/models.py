from django.db import models

class Cupones(models.Model):
    code = models.CharField(max_length=60,unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField()
    active = models.BooleanField()


    def str(self):
        return self.code
        