import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from tensorflow.keras.models import load_model

from ChatBotAPI.utils import constants
from ChatBotAPI.utils.chatbot_service import ChatBotService
from ChatBotAPI.utils.chatbot_factory import ChatBotFactory
from ChatBotAPI import models

from transformers import OpenAIGPTTokenizer

tokenizer = OpenAIGPTTokenizer.from_pretrained('openai-gpt')
cbf = ChatBotFactory()

# Create your views here.
def index(request):
    """index

    Args:
        request (request): api request
    """
    return JsonResponse({"data": "theres nothing at this endpoint"})


def get_chatbot_response(request):
    # data = request.GET.get('prompt')
    persona = models.Persona.objects.get(name='Primary')
    statements = [s.format_to_tokens(tokenizer) for s in persona.statements.all()]
    return JsonResponse({"answer": statements})


def build_chatbot(request):
    persona_statements, history_statements, reply = cbf.build_input() 
    return JsonResponse({
                            "persona_statements": persona_statements,
                            "history_statements": history_statements,
                            "reply": reply
                            })


def test(request):
    return JsonResponse({"value": "hmmm"})