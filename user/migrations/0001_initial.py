# Generated by Django 4.2.19 on 2025-03-18 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, verbose_name='用户名')),
                ('phone', models.CharField(max_length=100, verbose_name='手机号')),
                ('password', models.CharField(max_length=100, verbose_name='密码')),
                ('role', models.CharField(max_length=100, verbose_name='角色')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'user',
            },
        ),
        migrations.CreateModel(
            name='user_pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.CharField(max_length=100, verbose_name='宠物姓名')),
                ('pet_type', models.CharField(max_length=100, verbose_name='宠物类型')),
                ('pet_text', models.CharField(max_length=100, verbose_name='宠物简介')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user', verbose_name='主人')),
            ],
        ),
    ]
