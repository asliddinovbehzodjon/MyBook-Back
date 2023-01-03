from rest_framework.serializers import ModelSerializer
from .models import BotUsers
class BotSerializer(ModelSerializer):
    class Meta:
        model = BotUsers
        fields = "__all__"
        