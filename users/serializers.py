from rest_framework import serializers


from django.contrib.auth import get_user_model, authenticate, password_validation
from .models import User, Role

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )
    role = serializers.PrimaryKeyRelatedField(
        queryset = Role.objects.all()
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'username','name','surname','phone','role', 'password', )
        read_only_fields = ('token', )


    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance



class RegistrationSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ['email', 'username','name','surname','phone','role', 'password', 'token']

    def create(self, validated_data):
        user = get_user_model().user_manager.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            role = validated_data['role'],
            name=validated_data['name'],
            surname=validated_data['surname'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    '''def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
        user.save()

        return user'''
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'name')




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255, write_only=True)
    password = serializers.CharField(max_length=128, write_only=True, style = {'input_type': 'password'})
   
    role = serializers.IntegerField(source='role.id', read_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'A username is required to log in.'
            )

        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )


        user = authenticate(request=self.context.get('request'), username=username, password=password)

        if not user:
            raise serializers.ValidationError(
                'A user with this username and password was not found.'
            )

        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )

        
        return {
            'role': user.role,
            'token': user.token
        }



