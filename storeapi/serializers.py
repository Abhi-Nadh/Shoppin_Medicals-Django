from rest_framework import serializers

from medical_store.models import MedicineData

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineData
        fields = ['id', 'medicine_name','company', 'price', 'medicine_description', 'medicine_add_date']