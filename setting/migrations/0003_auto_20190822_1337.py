# Generated by Django 2.0.13 on 2019-08-22 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_auto_20190821_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendlinks',
            name='link',
            field=models.CharField(default='https://www.zmrenwu.com', max_length=200, verbose_name='网站地址'),
        ),
        migrations.AlterField(
            model_name='friendlinks',
            name='name',
            field=models.CharField(default='追梦人物的博客', max_length=50, verbose_name='网站名称'),
        ),
        migrations.AlterField(
            model_name='seo',
            name='sub_title',
            field=models.CharField(default='(ง •_•)ง', max_length=200, verbose_name='网站副名称'),
        ),
        migrations.AlterField(
            model_name='social',
            name='official_wechat',
            field=models.CharField(default='教你解初中数学题', max_length=50, verbose_name='微信公众号'),
        ),
        migrations.AlterField(
            model_name='social',
            name='zhi_hu',
            field=models.URLField(default='https://www.zhihu.com/people/xiao-hao-56-94/activities', verbose_name='知乎地址'),
        ),
    ]
