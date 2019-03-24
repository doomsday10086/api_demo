from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from ..models import UserAuthToken


class UserAuthentication(BaseAuthentication):

    def authenticate(self, request):

        request_token = request.data.get('token')
        if not request_token:
            raise AuthenticationFailed("缺少token")
        token_obj = UserAuthToken.objects.filter(token_code=request_token).first()
        if not token_obj:
            raise AuthenticationFailed('无效token')
        return token_obj.user, token_obj




