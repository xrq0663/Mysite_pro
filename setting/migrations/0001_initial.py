# Generated by Django 2.0.13 on 2019-08-20 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('statistics', models.TextField(default='统计代码', verbose_name='网站统计代码')),
            ],
            options={
                'verbose_name': '自定义代码',
                'verbose_name_plural': '自定义代码',
            },
        ),
        migrations.CreateModel(
            name='FriendLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='向东的笔记本', max_length=50, verbose_name='网站名称')),
                ('link', models.CharField(default='https://www.eastnotes.com', max_length=200, verbose_name='网站地址')),
            ],
            options={
                'verbose_name': '友情链接',
                'verbose_name_plural': '友情链接',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Seo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='DjangoEast', max_length=100, verbose_name='网站主名称')),
                ('sub_title', models.CharField(default='DjangoEast', max_length=200, verbose_name='网站副名称')),
                ('description', models.CharField(default='DjangoEast', max_length=200, verbose_name='网站描述')),
                ('keywords', models.CharField(default='DjangoEast', max_length=200, verbose_name='关键字')),
            ],
            options={
                'verbose_name': 'SEO设置',
                'verbose_name_plural': 'SEO设置',
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateField(default=django.utils.timezone.now, verbose_name='建站时间')),
                ('record_info', models.CharField(default='备案号', max_length=100, verbose_name='备案信息')),
                ('development_info', models.CharField(default='开发信息', max_length=100, verbose_name='开发信息')),
                ('arrange_info', models.CharField(default='部署信息', max_length=100, verbose_name='部署信息')),
            ],
            options={
                'verbose_name': '站点信息',
                'verbose_name_plural': '站点信息',
            },
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField(default='https://github.com/mxdshr/DjangoEast', verbose_name='Github地址')),
                ('wei_bo', models.URLField(default='https://weibo.com/', verbose_name='微博地址')),
                ('zhi_hu', models.URLField(default='https://www.zhihu.com/people/sylax8/', verbose_name='知乎地址')),
                ('qq', models.CharField(default='783342105', max_length=20, verbose_name='QQ号码')),
                ('wechat', models.CharField(default='reborn0502', max_length=50, verbose_name='微信')),
                ('official_wechat', models.CharField(default='程序员向东', max_length=50, verbose_name='微信公众号')),
            ],
            options={
                'verbose_name': '社交账号',
                'verbose_name_plural': '社交账号',
            },
        ),
    ]