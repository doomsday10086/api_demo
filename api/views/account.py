from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Account, UserAuthToken
from django.db.models import Q
from ..utils.baseresponse import BaseResponse
from ..utils.tools import get_verify_code
from django.core.exceptions import ObjectDoesNotExist


# class RegisterView()

class LoginView(APIView):
    """用户登录处理"""
    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        verify_code = get_verify_code()
        print(verify_code)
        request.session['verify_code'] = verify_code
        ret.data = '发送成功'
        return Response(ret.dict)

    def post(self, request, *args, **kwargs):
        # 获取数据
        # 校验数据
        ret = BaseResponse()
        mobile = request.data.get('mobile')
        code = request.data.get('code')
        if request.session['verify_code'] == code:

            try:
                # user_obj = Account.objects.get(Q(mobile=mobile) | Q(email=email))
                user_obj = Account.objects.get(mobile=mobile)
            except ObjectDoesNotExist as e:
                user_obj = Account(mobile=mobile)
                user_obj.save()
        
            # 创建并返回token
            token_obj = UserAuthToken(user=user_obj)
            token_obj.save()
            ret.data = token_obj.token
        else:
            ret.code = 400
            ret.error = '输入有误，请检查后再次输入'

        return Response(ret.dict)

