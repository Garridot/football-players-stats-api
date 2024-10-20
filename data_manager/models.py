from django.db import models

# Create your models here.

class Players(models.Model):
    name          = models.CharField(max_length=100)
    age           = models.IntegerField() 
    date_of_birth = models.DateField()
    nationality   = models.CharField(max_length=100)
    position      = models.CharField(max_length=50)
    current_club  = models.CharField(max_length=100)       

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
    minutes_played = models.IntegerField()
    season         = models.CharField(max_length=100)   


class Stats_by_Position(models.Model):
    player   = models.ForeignKey(Players, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)    
    games    = models.IntegerField()
    goals    = models.IntegerField()
    assists  = models.IntegerField()
    season   = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.player} - {self.position} - {self.season}"