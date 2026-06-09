from rest_framework import serializers

from dietPlan.models import DietPlan



class DietPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietPlan
        fields = "__all__"
        read_only_fields = [ "created_at","updated_at","is_active"]