from rest_framework import serializers

from .models import QcPush


class QcPushSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    language = serializers.ReadOnlyField()
    push_message_type = serializers.ReadOnlyField()
    unreceived_msg = serializers.ReadOnlyField()

    class Meta:
        model = QcPush
        fields = '__all__'
