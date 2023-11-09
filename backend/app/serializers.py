from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import (
    Amenity,
    AmenityType,
    Booking,
    Photo,
    Property,
    PropertyType,
    Review,
    Room,
    RoomBooking,
    User,
)


class CustomRegisterSerializer(RegisterSerializer):
    is_host = serializers.BooleanField(required=False)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            "username": self.validated_data.get("username", ""),
            "password1": self.validated_data.get("password1", ""),
            "email": self.validated_data.get("email", ""),
            "is_host": self.validated_data.get("is_host", ""),
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "is_host")


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"


class RoomBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomBooking
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"


class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = "__all__"


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"


class AmenityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AmenityType
        fields = "__all__"


class PropertySerializer(serializers.ModelSerializer):
    host = UserSerializer()

    class Meta:
        model = Property
        fields = "__all__"
        depth = 1
