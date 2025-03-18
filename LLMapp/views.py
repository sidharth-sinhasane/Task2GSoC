import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def GenerateCode(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            prompt = data.get("prompt", "")

            if not prompt:
                return JsonResponse({"error": "Prompt is required"}, status=400)

            # Ollama API endpoint
            ollama_url = "http://localhost:11434/api/generate"
            response = requests.post(ollama_url, json={"model": "codellama:7b", "prompt": prompt ,"stream": False})
            # print(response)
            if response.status_code == 200:
                return JsonResponse(response.json())
            else:
                return JsonResponse({"error": "Failed to get response from LLM"}, status=response.status_code)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)

