from django.shortcuts import render
from common.humanize_text import rewrite_text
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import DetectRequestCounter, UnregisteredUserWordCount
from payments.models import WordCountTracker
# Create your views here.
from dashboard.tasks import create_documents_record
from common.detect_ai import detect_and_classify
def index(request):
    return render(request, 'front/index.html')

def pricing(request):
    return render(request, 'front/pricing.html')

@csrf_exempt
def humanizer(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
    
        text = body["text"]
        purpose = body["purpose"]
        readability = body["readability"]
        strength = body["level"]

        word_count = len(text.split())
    

        if not request.user.is_authenticated:
            return JsonResponse({"error": "Word limit exceeded. Sign up for additional words or subscribe for unlimited access."}, status=400)

           

        word_count_tracker = WordCountTracker.objects.filter(subscription__user=request.user).last()
        if word_count > word_count_tracker.words_remaining:
            return JsonResponse({"error": "Limit is over please reset subscrioptions"}, status=400)
        result = rewrite_text(text, purpose=purpose, readability=readability, strength=strength)
        create_documents_record(input_text=text, output_text=result, user_id=request.user.id, purpose=purpose, level=strength, readibility=readability)
        return JsonResponse({"text": result})
        

@csrf_exempt
def detect_text(request):
    if request.user.is_authenticated:
        return handle_request(request)

    # Get or create a RequestCounter object for the user's IP address
    ip_address = get_client_ip(request)
    # TODO make celery task to delete old records and create task for creating new records
    counter, created = DetectRequestCounter.objects.get_or_create(ip_address=ip_address)

    # Limit the usage to 3 times for non-authenticated users
    if counter.request_count >= 100:
        return JsonResponse({'error': 'Limit reached'})

    # Increment the request count
    counter.request_count += 1
    counter.save()

    # Handle the request normally
    return handle_request(request)

def handle_request(request):
    if request.method == "POST":
        # Parse JSON from the request body
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        result = detect_and_classify(body["text"])
        return JsonResponse(result)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def terms_view(request):
    return render(request, 'front/terms_of_use.html')

def privacy_view(request):
    return render(request, 'front/privacy_policy.html')

def contact_view(request):
    return render(request, 'front/contact.html')