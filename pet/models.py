from django.db import models
from user.models import user_pet,user
# Create your models here.
class task(models.Model):
    user_pet = models.ForeignKey(user_pet, on_delete=models.CASCADE)
    task_time = models.DateTimeField(auto_now_add=True,verbose_name="发布时间")
    task_text = models.TextField(verbose_name="任务内容")
    task_status_choices = {
    (0, '已发布任务,暂时未被领取'),
    (1, '已被领取,任务正在进行中'),
    (2, '已完成任务,祝您生活愉快'),
    }

    task_status = models.IntegerField(choices=task_status_choices,default=0,verbose_name="任务状态")
    user = models.ForeignKey(user, on_delete=models.CASCADE,verbose_name="任务用户",null=True,blank=True)
    task_address = models.TextField(verbose_name="任务地点",null=True,blank=True)
    task_reward = models.IntegerField(verbose_name="任务赏金",null=True,blank=True)
    class Meta:
        verbose_name = "任务"
        verbose_name_plural = verbose_name
