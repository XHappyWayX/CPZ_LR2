from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
import requests
from .models import SavedRequests


class CheckRequestInDB(APIView):
    def post(self, request, *args, **kwargs):
        post_url = request.data.get('url')
        if not post_url:
            return Response({"message": "Invalid data"}, status=404)

        existing_request = SavedRequests.objects.filter(request_url=post_url).first()
        if existing_request:
            return Response({"description": "Old data", 'data': existing_request.request_data}, status=200)
        else:
            url = "https://www.virustotal.com/api/v3/urls"
            payload = {"url": f"{post_url}"}
            headers = {
                "accept": "application/json",
                "x-apikey": "fe7a5b71e7bfcdffa3a19ce2104a5732a7c43140a913d43f9fa5ddf88c84ebbc",
                "content-type": "application/x-www-form-urlencoded"
            }
            response = requests.post(url, data=payload, headers=headers)
            json_response = response.json()
            saved_request = SavedRequests.objects.create(request_url=post_url, request_data=json_response)
            saved_request.save()
            return Response({"description": "New data", 'data': json_response},status=200)
