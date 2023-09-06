from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=50)
    website = models.URLField(max_length=100)
    foundation = models.PositiveBigIntegerField()
    
    def __str__(self):
        return self.name
    
class Developer(models.Model):
    name = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name