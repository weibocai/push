# Generated by Django 2.1.8 on 2020-01-12 07:26

import django.contrib.auth.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='QcUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('username', models.CharField(default='', max_length=255)),
                ('login_type', models.CharField(choices=[('1', '手机'), ('2', '微信'), ('3', 'QQ'), ('4', '微博')], default='1', max_length=1, verbose_name='login type')),
                ('mobile', models.CharField(max_length=255, unique=True)),
                ('wei_id', models.CharField(blank=True, max_length=255, null=True)),
                ('qq_id', models.CharField(blank=True, max_length=255, null=True)),
                ('user_pic', models.CharField(max_length=255, null=True)),
                ('user_soft', models.IntegerField(choices=[(0, '普通用户'), (1, '导师'), (2, 'vip'), (3, '管理员')], default=0)),
                ('online', models.BooleanField(default=False, help_text='是否在线')),
                ('strike', models.BooleanField(default=False, help_text='0未删除，用于逻辑删除')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'db_table': 'qc_user',
                'ordering': ['-date_joined'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='QcPush',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('sender', models.CharField(help_text='发送者id', max_length=64)),
                ('sender_name', models.CharField(help_text='发送者名称', max_length=32)),
                ('target', models.CharField(default='', help_text='目标id', max_length=32)),
                ('target_name', models.CharField(help_text='目标名称', max_length=32)),
                ('con_type', models.SmallIntegerField(choices=[(1, '标识点击行为用户自定义'), (2, '标识打开特定URL'), (3, '标识打开本业务的APP')], help_text='发送类型：自定义发送，普通发送')),
                ('server_time', models.IntegerField(help_text='时间戳')),
                ('push_message_type', models.SmallIntegerField(choices=[(0, 'normal'), (1, '透传')], default=0, help_text='普通消息；透传。')),
                ('push_type', models.SmallIntegerField(choices=[(0, 'iOS'), (1, 'xm'), (2, 'hw'), (3, 'mz'), (4, 'vivo'), (5, 'os all')], help_text='推送类型，android推送分为小米/华为/魅族/vivo等。ios')),
                ('push_content', models.CharField(help_text='内容', max_length=124)),
                ('unreceived_msg', models.CharField(default='', help_text='失败回馈信息，只有管理员推送才会接受回馈', max_length=256)),
                ('device_token', models.CharField(help_text='device token', max_length=124)),
                ('is_all', models.SmallIntegerField(choices=[(0, '单个'), (1, '全部'), (2, '部分')], default=0, help_text='是否推送所有用户')),
                ('language', models.CharField(default='zh-Hans-CN', help_text='device token', max_length=16)),
            ],
            options={
                'db_table': 'qc_push',
            },
        ),
    ]
