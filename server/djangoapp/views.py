from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)

# ------------------- Views -------------------

# ✅ Login view
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data['userName']
            password = data['password']

            user = authenticate(username=username, password=password)
            response_data = {"userName": username}

            if user is not None:
                login(request, user)
                response_data["status"] = "Authenticated"
            else:
                response_data["status"] = "Invalid credentials"

            return JsonResponse(response_data)
        except Exception as e:
            logger.error(f"Error during login: {e}")
            return JsonResponse({"error": "Something went wrong"}, status=500)
    else:
        return JsonResponse({"error": "Only POST method allowed"}, status=405)

# ✅ Logout view
@csrf_exempt
def logout_request(request):
    logout(request)
    data = {"userName": ""}
    return JsonResponse(data)

# ✅ Registration view (Updated)
@csrf_exempt
def registration(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            username = data.get("userName")
            password = data.get("password")
            email = data.get("email")
            first_name = data.get("firstName", "")
            last_name = data.get("lastName", "")

            if User.objects.filter(username=username).exists():
                return JsonResponse({"status": False, "error": "Already Registered"})

            # Create the user
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=first_name,
                last_name=last_name
            )
            user.save()

            # Log in the user
            login(request, user)

            return JsonResponse({"status": True, "userName": username})

        except Exception as e:
            logger.error(f"Error during registration: {e}")
            return JsonResponse({"status": False, "error": "Something went wrong"}, status=500)
    else:
        return JsonResponse({"status": False, "error": "Only POST method allowed"}, status=405)

# ------------------- Future Dealership Views (Template) -------------------

# def get_dealerships(request):
#     ...

# def get_dealer_reviews(request, dealer_id):
#     ...

# def get_dealer_details(request, dealer_id):
#     ...

# def add_review(request):
#     ...
