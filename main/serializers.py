from rest_framework import serializers

from main.models import Task, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    @staticmethod
    def get_images(obj):
        images = Image.objects.filter(task=obj.id)
        serializer = ImageSerializer(instance=images, many=True)
        return serializer.data

    class Meta:
        model = Task
        fields = "__all__"
