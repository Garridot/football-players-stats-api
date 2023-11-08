from django.utils.translation import gettext as _
from rest_framework import serializers
from .models import User
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')  
        extra_kwargs={'password':{'write_only':True}}

    def validate_password(self, value):        
        if len(value) < 12: 
            raise serializers.ValidationError(_("The password must be at least 12 characters."))
        
        if not re.search(r'[A-Z]', value) or not re.search(r'[a-z]', value) or not re.search(r'\d', value) or not re.search(r'[!@#\$%\^&\*\(\)_\+\-\.,;?{}|<>~\[\]]', value):
            raise serializers.ValidationError(_("The password must include at least one uppercase letter, one lowercase letter, one number, and one special character."))

        email = self.initial_data.get('email', None)
        if email and value == email:
            raise serializers.ValidationError(_("The password cannot be the same as the email."))
        return value    

    def create(self, validated_data):        
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None: instance.set_password(password)
        instance.save() 
        return instance   




    