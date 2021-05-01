from rest_framework.serializers import ModelSerializer

from cars.models import Car


class DynamicFieldsModelSerializer(ModelSerializer):
    """
    Add serializer fields based on query params
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context['request'].method != 'POST':
            fields = self.context['request'].query_params.get('info')
            if fields:
                fields = fields.split(',')
                fields += ['id', 'brand', 'model', 'registration_number', 'production_year', 'max_passenger_capacity']
                allowed = set(fields)  
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)
            else:
                self.fields.pop('car_class')
                self.fields.pop('low_emission')


class CarSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

