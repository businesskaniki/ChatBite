from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import UserProfile
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'password2')
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError("Invalid email or password.")
        if not user.is_active:
            raise serializers.ValidationError(
                "This user has been deactivated.")

        attrs['user'] = user
        return attrs


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'email', 'username', 'date_joined', 'last_seen', 'profile_image',
                  'background_image', 'profile_frmae', 'bite_credit', 'about', 'phone_number', 'tire', 'blocked']
        read_only_fields = ['id', 'date_joined', 'last_seen', 'bite_credit']

    def patch(self, instance, validated_data):
        # Update the UserProfile instance with the validated data
        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.profile_image = validated_data.get(
            'profile_image', instance.profile_image)
        instance.background_image = validated_data.get(
            'background_image', instance.background_image)
        instance.profile_frmae = validated_data.get(
            'profile_frmae', instance.profile_frmae)
        instance.about = validated_data.get('about', instance.about)
        instance.phone_number = validated_data.get(
            'phone_number', instance.phone_number)
        instance.tire = validated_data.get('tire', instance.tire)
        instance.blocked = validated_data.get('blocked', instance.blocked)

        instance.save()
        return instance

    def delete(self, instance):
        # Delete the UserProfile instance
        instance.delete()
