from django.db import models

# Create your models here.

def location_media(instance,filename):
    return f"players/{instance.name}/{filename}" 

class Players(models.Model):
    name          = models.CharField(max_length=100)
    age           = models.IntegerField() 
    date_of_birth = models.DateField()
    nationality   = models.CharField(max_length=100)
    position      = models.CharField(max_length=50)
    current_club  = models.CharField(max_length=100)
    picture       = models.ImageField(blank=True,null=True, upload_to=location_media)     

    def __str__(self):
        return self.name



class Player_Stats(models.Model):
    player         = models.ForeignKey(Players,on_delete=models.CASCADE)
    team           = models.CharField(max_length=100)    
    competition    = models.CharField(max_length=100)    
    goals          = models.IntegerField()
    assists        = models.IntegerField()
    games          = models.IntegerField()    
    wins           = models.IntegerField()    
    draws          = models.IntegerField()
    defeats        = models.IntegerField()  
    team_goals     = models.IntegerField()  
    season         = models.CharField(max_length=100)   