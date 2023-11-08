from rest_framework import serializers
from .models import Players, Player_Stats
from rest_framework import status
from datetime import datetime
import re

def required(value):
    if value is None:  raise serializers.ValidationError('This field is required',code=status.HTTP_400_BAD_REQUEST)

def validate_number(value):        
        if not isinstance(value, int) or value < 0:
            raise serializers.ValidationError("This field must be a valid number.",code=status.HTTP_400_BAD_REQUEST)

class PlayerSerializer(serializers.ModelSerializer): 
    name          = serializers.CharField(validators=[required])
    age           = serializers.IntegerField(validators=[required,validate_number])    
    date_of_birth = serializers.DateField(validators=[required])
    nationality   = serializers.CharField(validators=[required])
    position      = serializers.CharField(validators=[required])
    current_club  = serializers.CharField(validators=[required])

    class Meta:
        model  = Players
        fields =  ('__all__')

    def validate(self, attrs): 
        return super().validate(attrs) 


    def validate_date_of_birth(self, value): 

        date_format = "%Y-%m-%d"  

        if isinstance(value, str):
            try:                
                value = datetime.strptime(value, date_format).date()
                return value
            except ValueError:
                raise serializers.ValidationError("Please ensure that the 'date of birth' field is entered in the format 'YYYY-MM-DD'.")
        
        return value
        
    def create(self, validated_data):       
        return Players.objects.create(**validated_data) 

    def update(self, instance, validated_data):       
        instance.name          = validated_data.get('name', instance.name)
        instance.age           = validated_data.get('age', instance.age)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.nationality   = validated_data.get('nationality', instance.nationality)
        instance.position      = validated_data.get('position', instance.position)
        instance.current_club  = validated_data.get('current_club', instance.current_club)
        instance.save()
        return instance    


def validate_season(value):                
        pattern = r'^\d{4}-\d{4}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError("The field should follow the 'year-year' format, such as '2001-2002'.")

class PlayerStatsSerializer(serializers.ModelSerializer):     
    team           = serializers.CharField(validators=[required])    
    competition    = serializers.CharField(validators=[required])    
    goals          = serializers.IntegerField(validators=[required,validate_number]) 
    assists        = serializers.IntegerField(validators=[required,validate_number]) 
    games          = serializers.IntegerField(validators=[required,validate_number])     
    wins           = serializers.IntegerField(validators=[required,validate_number])    
    draws          = serializers.IntegerField(validators=[required,validate_number]) 
    defeats        = serializers.IntegerField(validators=[required,validate_number])   
    team_goals     = serializers.IntegerField(validators=[required,validate_number])   
    season         = serializers.CharField(validators=[required,validate_season])   

    class Meta:
        model  = Player_Stats
        fields =  ('__all__')

    def create(self, validated_data):       
        return Player_Stats.objects.create(**validated_data) 

    def validate(self, attrs): 
        return super().validate(attrs)  

        

