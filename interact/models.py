from django.db import models

# Create your models here.
class Interaction(models.Model):
    id = models.IntegerField(primary_key=True)
    protein1 = models.CharField(max_length=25, default="NA")
    protein2 = models.CharField(max_length=25,default="NA")
    neighborhood = models.IntegerField(default=0)
    fusion = models.IntegerField(default=0)
    cooccurance = models.IntegerField(default=0)
    coexpression = models.IntegerField(default=0)
    experimental = models.IntegerField(default=0)
    database = models.IntegerField(default=0)
    textmining = models.IntegerField(default=0)
    combined_score = models.IntegerField(default=0)
    
    def __int__(self):
        return self.protein1  