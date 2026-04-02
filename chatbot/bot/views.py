from django.shortcuts import render

# Create your views here.
from .models import Conversation, Message


def chat_view(request):
    conversation, _ = Conversation.objects.get_or_create(id=1)

    if request.method == 'POST':
        user_message = request.POST.get('message', '').strip()
        if user_message:
            message = Message.objects.create(text=user_message, is_user=True)
            conversation.messages.add(message)

            bot_response = f"Response: {user_message}"
            bot_message = Message.objects.create(text=bot_response, is_user=False)
            conversation.messages.add(bot_message)

    messages = conversation.messages.order_by('timestamp')

    return render(request, 'chat.html', {'conversation': conversation, 'messages': messages})





def chat(request):
    conversation = Conversation.objects.first()
    messages = conversation.messages.order_by('timestamp') if conversation else []
    return render(request, 'chat.html', {'conversation': conversation, 'messages': messages})

