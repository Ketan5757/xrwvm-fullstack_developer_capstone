# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv('sentiment_analyzer_url', default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    request_url = backend_url + endpoint + "?" + params
    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Network exception occurred:", e)
        return None


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    print("Calling sentiment analyzer at:", request_url)
    try:
        response = requests.get(request_url)
        response.raise_for_status()
        result = response.json()
        return result.get("sentiment", "neutral")
    except requests.exceptions.RequestException as e:
        print("Sentiment analysis failed:", e)
        return "neutral"


def post_review(data_dict):
    request_url = backend_url + "postReview"
    print("POST to {} with payload: {}".format(request_url, data_dict))
    try:
        response = requests.post(request_url, json=data_dict)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Failed to post review:", e)
        return None
