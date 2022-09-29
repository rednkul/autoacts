from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers
from .models import Type, Act, Project, Material


from django.core.files.base import ContentFile
import base64
import six
import uuid
from mimetypes import guess_extension, guess_type

class Base64FileField(serializers.FileField):
    """
    A Django REST framework field for handling image-uploads through raw post data.
    It uses base64 for encoding and decoding the contents of the file.

    Heavily based on
    https://github.com/tomchristie/django-rest-framework/pull/1268

    Updated for Django REST framework 3.
    """

    def to_internal_value(self, data):


        # Check if this is a base64 string
        if isinstance(data, six.string_types):

            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

                print(header)
                print(guess_extension('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'))

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_file')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            file_extension = guess_extension(header[5:])
            complete_file_name = "%s%s" % (file_name, file_extension,)
            print(complete_file_name)
            data = ContentFile(decoded_file, name=complete_file_name)


        return super(Base64FileField, self).to_internal_value(data)




class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['name', ]


class MaterialSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    passport = Base64FileField(max_length=None, use_url=True)

    class Meta:
        model = Material
        fields = ['id', 'passport', 'name']


class ActSerializer(WritableNestedModelSerializer):

    materials = MaterialSerializer(many=True)

    class Meta:
        model = Act
        fields = ['act_type', 'works', 'number', 'materials', 'order_number', 'date_start', 'date_end']


class ProjectSerializer(WritableNestedModelSerializer):
    acts = ActSerializer(many=True)
    template = Base64FileField(max_length=None, use_url=True)

    class Meta:
        model = Project
        fields = ['name', 'template', 'acts']
