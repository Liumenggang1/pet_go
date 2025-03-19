from django.db import models

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=100,verbose_name='用户名')
    phone = models.CharField(max_length=100,verbose_name='手机号')
    password = models.CharField(max_length=100,verbose_name='密码')
    role = models.CharField(max_length=100,verbose_name='角色')
    def __str__(self):
        return self.username
    class Meta:
        db_table = 'user'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name
class user_pet(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE,verbose_name='主人')
    pet_name = models.CharField(max_length=100,verbose_name='宠物姓名')
    pet_type = models.CharField(max_length=100,verbose_name='宠物类型')
    pet_text = models.CharField(max_length=100,verbose_name='宠物简介')
