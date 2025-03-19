from django.shortcuts import render, redirect
from user import models as user_models
from django.contrib import messages
from pet import models as pet_models


# Create your views here.
def home(request):
    print(request.session)
    context = {
        'active_page': 'home'
    }
    return render(request, 'pet/home.html', context)


def my_pet(request):
    my_pet = user_models.user_pet.objects.filter(user_id=request.session['user_info']['id'])
    context = {
        'active_page': 'my_pet',
        'my_pet': my_pet,
    }
    return render(request, 'pet/my_pet.html', context)


def add(request):
    context = {
        'active_page': 'my_pet'
    }
    if request.method == 'POST':
        user_id = request.session['user_info']['id']
        user = user_models.user.objects.get(id=user_id)
        pet_name = request.POST['pet_name']
        pet_type = request.POST['pet_type']
        pet_text = request.POST['pet_text']
        if pet_name == '' or pet_type == '' or pet_text == '':
            return render(request, 'pet/pet.html', {'error': '数据不可为空'})
        elif user_models.user_pet.objects.filter(pet_name=pet_name).exists():
            return render(request, 'pet/pet.html', {'error': '宠物名称已存在'})
        else:
            user_models.user_pet.objects.create(user=user, pet_name=pet_name, pet_type=pet_type, pet_text=pet_text)
            messages.error(request, "添加完成")
            return redirect("/my_pet")

    return render(request, 'pet/pet.html', context)


def pet_delete(request, pet_id):
    user_models.user_pet.objects.filter(id=pet_id).delete()
    return render(request, 'pet/my_pet.html')


def task_add(request):
    user_id = request.session['user_info']['id']
    pet = user_models.user_pet.objects.filter(user_id=user_id)
    if request.method == 'POST':
        user_pet_id = user_models.user_pet.objects.get(id=request.POST['user_pet'])
        task_text = request.POST['task_text']
        task_address = request.POST['task_address']
        task_reward = request.POST['task_reward']
        if task_text == '' or user_pet_id == '' or task_address == '' or task_reward == '':
            return render(request, 'pet/task_add.html', {'error': '数据不可为空'})
        else:
            pet_models.task.objects.create(user_pet=user_pet_id, task_text=task_text, task_address=task_address, task_reward=task_reward)
            messages.error(request, "成功发布任务")
            return redirect("/task/list")
    context = {
        'active_page': 'task_add',
        'pet': pet,
    }
    return render(request, 'pet/task_add.html', context)


def task_list(request):
    user_id = user_models.user.objects.get(id=request.session['user_info']['id'])
    task_list = pet_models.task.objects.exclude().all()
    context = {
        'active_page': 'task_list',
        'task_list': task_list,
        'user_id': user_id,
    }
    return render(request, 'pet/task_list.html', context)


def task(request, task_id):
    user_id = user_models.user.objects.get(id=request.session['user_info']['id'])
    if pet_models.task.objects.filter(id=task_id, task_status=1):
        messages.error(request, "任务已被其他人领取")
        return redirect("/task/list")
    pet_models.task.objects.filter(id=task_id).update(task_status=1, user_id=user_id)

    messages.error(request, "接受任务")
    return redirect("/task/list")


def my_task_list(request):
    user_id = user_models.user.objects.get(id=request.session['user_info']['id'])
    task_list = pet_models.task.objects.filter(user_id=user_id,).all()
    task_list_user = pet_models.task.objects.filter(user_pet__user__id=request.session['user_info']['id'],).all()
    print(task_list_user)
    context = {
        'active_page': 'my_task',
        'task_list': task_list,
        'task_list_user':task_list_user,
    }
    return render(request, 'pet/my_task.html', context)


def my_task(request, my_task_id):
    pet_models.task.objects.filter(id=my_task_id,).update(task_status=2)
    return redirect("/my_task/list")