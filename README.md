前面忘记写更新了，从今天开始记录一下每天都做了什么

------------3.3---------------
----
* 在user表上添加触发器以用于在管理员注册时自动向user添加管理员用户，但目前觉得这个单独的管理员表非常鸡肋，预计在backends中重写管理员登录的认证函数，以区分普通用户和管理员的登录<br>
* 添加了审核记录表的视图函数以及前端界面，以及在同意和拒绝申请的视图函数上添加了记录审核历史的功能<br>
* 使用Paginator函数优化了诸如活动表以及审核记录表在前端的表现，现在可以在活动表进行翻页了，一页十条数据，后续会跟进添加管理员审核时的分布式锁，预计使用redis进行缓存<br>
* 添加了普通用户活动申请的按钮和选项，管理员和普通用户看到的活动选项并不会一致，预计制作一个申请后弹出以提供用户写申请理由的form表单<br>
