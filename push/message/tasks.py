from celery import shared_task

from message.models import PushModel
from message.utils import hw_push, ios_push, xm_push, vo_push


@shared_task
def order_push(title, push_content, device_token, product, product_id, push_obj_id, push_type='0'):
    """
    选择推送
    :param title: 标题
    :param push_content: 内容
    :param device_token: 目标，苹果暂时不支持多目标推送
    :param product: 商品
    :param product_id: 商品id
    :param push_type: 推送类型
    :param push_obj_id: 推送记录id
    :return:
    """
    try:
        push_fun = {'0': ios_push, '1': xm_push, '2': hw_push, '3': vo_push}[push_type]
    except KeyError:
        push_fun = xm_push

    push_result = push_fun(title, push_content, device_token=device_token, product=product, product_id=product_id)
    obj = PushModel.objects.get(id=push_obj_id)
    obj.unreceived_msg = push_result
    obj.save()
