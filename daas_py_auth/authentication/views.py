from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.db import connection
from manage import logger, config
import base64

configs = config.get_configs()
DB_FUNC_GET_USER_FACILITY = configs.DB_FUNC_GET_USER_FACILITY

@api_view(["POST"])
def login(request):
    auth_header = request.headers.get("Authorization")
    
    if not auth_header or not auth_header.startswith("Basic "):
        return JsonResponse({"error": "Missing or invalid Authorization header"}, status=401)
    
    # username = request.data.get("username")
    # password = request.data.get("password")
    
    # Decode Base64 credentials
    encoded_credentials = auth_header.split(" ")[1]
    decoded_credentials = base64.b64decode(encoded_credentials).decode("utf-8")
    
    username, password = decoded_credentials.split(":", 1)

    # Authenticate user
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({"error": "Invalid credentials"}, status=400)

    # Call PostgreSQL function to get facilities for the user
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {DB_FUNC_GET_USER_FACILITY}(%s);", [user.id])
        facility = [row[0] for row in cursor.fetchall()]  # Fetch facilities list

    # Generate JWT token
    refresh = RefreshToken.for_user(user)
    refresh["facility"] = facility  # Inject facilities into token

    return Response({
        "access": str(refresh.access_token),
        "refresh": str(refresh),
    })
