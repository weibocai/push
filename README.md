## 本项目，利用Django集成国内几家大的手机厂商的推送，包括apple，华为，小米，vivo，魅族

### apple推送证书
1. apple直接导入的证书是：*.p12格式，我在python中未找到直接解析这个格式文件的方法
2. 可以直接将*.p12格式转成*.pem格式的密钥

### 在setting中配置各个厂商推送所需的密匙
IOS_CONF = {
    'cer_path': os.path.join(BASE_DIR, 'conf/dev_certificates.pem'),
    'cer_pwd': '123456',
}

HW_CONF = {
    'app_id': '',
    'client_secret': '',
}

XM_CONF = {
    'package_name': '',
    'app_id': '',
    'client_secret': '',
}
VO_CONF = {
    'app_secret': ''
}

### 目前只支持自定义推送事件，对于国内安卓厂商来说