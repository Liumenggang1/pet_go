# 中间件处理 有关列表看settings42行
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 排除那些界面不需要登入就能访问
        # process_request_info 获取当前用户请求的URL /login/
        # print(request.path_info)

        if request.path_info.startswith('/admin/'):
            return

        if request.path_info in ["/user/login/", "/user/register/", "/",]:
            return

        #
        # # 若不是 /login 则进行读取session信息来判断是否登入
        #
        # 读取当前访问的用户的session信息，如果能读到，则可继续往后走
        info_dict = request.session.get("user_info")
        if info_dict:
            return

        # 没有读取到session信息，则返回登陆页面
        return redirect("/user/login/")
