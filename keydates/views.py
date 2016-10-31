# Create your views here.
import json
import os
from rest_framework.response import Response
from rest_framework.views import APIView


class KeydatesList(APIView):
    def get(self, request, format=None):
        with open('keydates' + os.sep + 'keydates.json', 'r', encoding='utf-8') as f:
            content = json.loads(f.read())
        return Response(content)


class KeydatesVersion(APIView):
    def get(self, request, format=None):
        return Response({
            "v": 1,
            "f": False
        })
