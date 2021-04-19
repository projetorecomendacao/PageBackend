import os
from django.conf.urls import url
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "recommendation_system.settings")
django_asgi_app = get_asgi_application()


from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from esm_program_section.consumers import ChatConsumer

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r'ws/chat/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
        ])
    ),
})