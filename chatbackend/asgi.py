import os
from django.core.asgi import get_asgi_application
from channels.routing  import ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatbackend.settings')

from chat.jwt_middleware  import JWTAuthMiddleware 

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': 
        JWTAuthMiddleware(
            URLRouter(
                chat.routing.websocket_urlpatterns
            )
        )
    }
)



