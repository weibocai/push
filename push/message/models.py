from django.db import models

# Create your models here.

PUSH_MESSAGE_TYPE = (
    (0, 'normal'),
    (1, '透传')
)
OS_TYPE = (
    (0, 'iOS'),
    (1, 'xm'),
    (2, 'hw'),
    (3, 'mz'),
    (4, 'vivo'),
    (5, 'os all'),
)
CONTENT_TYPE = (
    (1, '标识点击行为用户自定义'),
    (2, '标识打开特定URL'),
    (3, '标识打开本业务的APP'),
    # (4, '标识打开富媒体信息'), 暂时不提供
)
IS_ALL = (
    (0, '单个'),
    (1, '全部'),
    (2, '部分'),
)


class PushModel(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    sender = models.CharField(max_length=64, help_text='发送者id')
    sender_name = models.CharField(max_length=32, help_text='发送者名称')
    target = models.CharField(max_length=32, help_text='目标id', default='')
    target_name = models.CharField(max_length=32, help_text='目标名称')
    con_type = models.SmallIntegerField(choices=CONTENT_TYPE, help_text='发送类型：自定义发送，普通发送')
    server_time = models.IntegerField(help_text='时间戳')
    push_message_type = models.SmallIntegerField(choices=PUSH_MESSAGE_TYPE, default=0, help_text='普通消息；透传。')
    push_type = models.SmallIntegerField(choices=OS_TYPE, help_text='推送类型，android推送分为小米/华为/魅族/vivo等。ios')
    push_content = models.CharField(max_length=124, help_text='内容')
    unreceived_msg = models.CharField(help_text='失败回馈信息，只有管理员推送才会接受回馈', default='', max_length=512)
    device_token = models.CharField(max_length=124, help_text='device token')
    is_all = models.SmallIntegerField(choices=IS_ALL, default=0, help_text='是否推送所有用户')
    language = models.CharField(max_length=16, default='zh-Hans-CN', help_text='device token')

    class Meta:
        db_table = 'qc_push'
