# 上下文处理器，用于避免每次都需要将userid传递到前端
# 处理器需要添加到setting的TEMPLATE的context_processors中
# context_processors.py
def user_info(request):
    # 如果用户已登录，返回用户信息
    if request.user.is_authenticated:
        return {
            'user_id': request.user.user_id,
            'user_name': request.user.user_name,
            'user_role': request.user.role, # 用户身份，用于前端是否显示删除按钮
        }
    # 如果用户未登录，返回空字典
    return {}