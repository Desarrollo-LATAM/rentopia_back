from rest_framework import serializers

from apps.users.models import User


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "id")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")

        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data["password"])
            user.save()
            return user

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                "La contraseña debe tener al menos 8 caracteres"
            )
        return value


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

        def to_representation(self, instance):
            return {
                "id": instance["id"],
                "username": instance["username"],
                "email": instance["email"],
            }


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email",)


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2", "is_owner"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        """
        Ensure the passwords are the same and meet any other validation criteria.
        """
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"password2": "Las contraseñas no coinciden."}
            )
        return data

    def save(self, request):
        """
        Create a new user instance.
        """
        user = User(
            username=self.validated_data["username"],
            email=self.validated_data["email"],
            is_owner=self.validated_data.get("is_owner", False),
        )
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user
