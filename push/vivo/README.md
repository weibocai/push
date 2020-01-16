# vivo-push-python
# 业务异常码及更详细信息可参考开发者平台文档
    https://dev.vivo.com.cn/documentCenter/doc/155


一切消息请求都需要进行鉴权操作，即获取authToken,该token有效期一天，一天内皆可用该token鉴权发送个类请求


#单推消息体
message = PushMessage()\
    #应用订阅 PUSH 服务器得到的 id 长度 23 个字符（regId，alias 两者需一个不为空，当两个不为空时，取 regId）
    .reg_id('regId') \
    #别名 长度不超过 40 字符（regId，alias 两者需一个不为空，当两个不为空时，取 regId）
    .ali_as('alias') \
    #通知标题（用于通知栏消息） 最大 20 个汉字（一个汉字等于两个英文字符，即最大不超过 40 个英文字符）
    .title('title')\
    #通知内容（用于通知栏消息） 最大 50 个汉字（一个汉字等于两个英文字符，即最大不超过 100 个英文字符）
    .content('content内容')\
    #通知类型 1:无，2:响铃，3:振动，4:响铃和振动
    .notify_type(1)\
    #网络方式 -1：不限，1：wifi 下发送，不填默认为-1
    .network_type(-1)\
    #点击跳转类型 1：打开 APP 首页 2：打开链接 3：自定义 4:打开 app 内指定页面
    .skip_type(2)\
    #跳转内容 跳转类型为 2 时，跳转内容最大1000 个字符，跳转类型为 3 或 4 时，跳转内容最大 1024 个字符
    .skip_content('www.vivo.com')\
    #消息保留时长 单位：秒，取值至少 60 秒，最长 7 天。当值为空时，默认一天
    .time_to_live(1000)\
    #用户请求唯一标识 最大 64 字符
    .request_id('1234567890123456') \
    #客户端自定义键值对 自定义 key 和 Value 键值对个数不能超过 10 个，且长度不能超过1024 字符, key 和 Value 键值对总长度不能超过 1024 字符。
    .client_custom_map(key1='value1',key2='value2') \
    #高级特性；第一个参数：第三方接收回执的 http 接口，最大长度128 个字符。第二个参数：第三方自定义回执参数，最大长度 64 个字符
    .extra("http://www.vivo.com", "vivo")\
    .message_dict()


#保存群推消息体
save_list_message = PushMessage()\
    #通知标题（用于通知栏消息） 最大 20 个汉字（一个汉字等于两个英文字符，即最大不超过 40 个英文字符）
    .title('title')\
    #通知内容（用于通知栏消息） 最大 50 个汉字（一个汉字等于两个英文字符，即最大不超过 100 个英文字符）
    .content('content内容')\
    #通知类型 1:无，2:响铃，3:振动，4:响铃和振动
    .notify_type(1)\
    #网络方式 -1：不限，1：wifi 下发送，不填默认为-1
    .network_type(-1)\
    #点击跳转类型 1：打开 APP 首页 2：打开链接 3：自定义 4:打开 app 内指定页面
    .skip_type(2)\
    #跳转内容 跳转类型为 2 时，跳转内容最大1000 个字符，跳转类型为 3 或 4 时，跳转内容最大 1024 个字符
    .skip_content('www.vivo.com')\
    #消息保留时长 单位：秒，取值至少 900 秒，最长 7 天。当值为空时，默认一天。
    .time_to_live(1000)\
    #用户请求唯一标识 最大 64 字符
    .request_id('1234567890123456') \
    #客户端自定义键值对 自定义 key 和 Value 键值对个数不能超过 10 个，且长度不能超过1024 字符, key 和 Value 键值对总长度不能超过 1024 字符。
    .client_custom_map(key1='value1',key2='value2') \
    .message_dict()

#群推消息体
reg_ids = ['regId1','regId2']
aliases = ['alias1', alias2]
send_to_list =  TargetMessage()\
    #公共消息任务号，调用保存群推消息接口返回的taskId
    .task_id('taskId')\
    #regId 列表 个数大于等于 2，小于等于 1000，regId 长度 23 个字符（regIds，aliases 两者需一个不为空，两个不为空，取 regIds）
    .reg_ids(reg_ids)\
    #别名列表个数大于等于 2，小于等于 1000，长度不超过 40 字符（regIds，aliases 两者需一个不为空，两个不为空，取 regIds）
    .aliases(aliases)\
    #用户请求唯一标识 最大 64 字符
    .request_id('1234567890123456')\
    .message_dict()

#获取统计数据
task = [taskId1, taskId2]
task_ids = TaskMessage()\
    #查询的任务列表,最多100个
    .task_ids(task)\
    .message_dict()