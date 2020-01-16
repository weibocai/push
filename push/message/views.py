import logging

from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from django.http import JsonResponse

from .models import QcPush
from .serializers import QcPushSerializers
from message.utils import hw_push, ios_push, xm_push, vo_push

logger = logging.getLogger('django')


# 推送最好由后台管理员发送，或有服务器转发，而不对外曝露接口
class QcPushViewSet(viewsets.ModelViewSet):
    queryset = QcPush.objects.all()
    serializer_class = QcPushSerializers
    permission_classes = (permissions.IsAdmin,)

    @action(methods=['post'], detail=False, permission_classes=(permissions.AllowAny,))
    def wf_ios(self, request):
        data = request.data
        title = data.get('title', '标题')
        push_content = data.get('push_content', '推送内容')
        product_id = data.get('product_id', '商品id')
        product = data.get('product', '商品')
        push_result = ios_push(title, push_content, device_token=data['deviceToken'], product=product,
                               product_id=product_id)
        logger.info(push_result)
        return JsonResponse({'msg': '成功', 'status': 200, 'data': {}})

    @action(methods=['post'], detail=False, permission_classes=(permissions.AllowAny,))
    def wf_android(self, request):
        data = request.data
        title = data.get('title', '标题')
        push_content = data.get('push_content', '推送内容')
        product_id = data.get('product_id', '商品id')
        product = data.get('product', '商品')

        # 推送厂家
        push_type = data.get('push_type', '1')
        try:
            push_fun = {'1': xm_push, '2': hw_push, '3': vo_push}[push_type]
        except KeyError:
            push_fun = xm_push
        push_result = push_fun(title, push_content, device_token=data['deviceToken'], product=product,
                               product_id=product_id)
        logger.info(push_result)
        return JsonResponse({'msg': '成功', 'status': 200, 'data': {}})

    def perform_create(self, serializer):
        serializer.save()

