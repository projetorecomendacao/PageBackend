from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import esm_program_section.routing

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    # changed
    "websocket": AuthMiddlewareStack(
        URLRouter(
            esm_program_section.routing.websocket_urlpatterns
        )
    ),
})