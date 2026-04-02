from django.urls import path


from .views import chat_view, chat


urlpatterns = [
    path('', chat_view, name='chat'),
    path('conversations/', chat, name='conversations'),
]