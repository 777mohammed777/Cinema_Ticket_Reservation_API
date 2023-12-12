from rest_framework import serializers
from .models import Movie,Guest,Resevation


class MovieSerializer(serializers.ModelSerializer):
    class Meta :
        model = Movie
        fields = "__all__"
    
class GuestSerializer(serializers.ModelSerializer):
    class Meta :
        model = Guest
        fields = [ 'pk' , 'reservation' , 'name' , 'mobile' ]
    
class ResevationSerializer(serializers.ModelSerializer):
    class Meta :
        model = Resevation
        fields = "__all__"
