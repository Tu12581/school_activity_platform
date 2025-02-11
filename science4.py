# 汪帅璨Only
# 认准唯一联系方式：337845818，三Q！

# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple yaspy

import tkinter as tk
from tkinter import ttk, messagebox
from db import Database


class ActivityRecruitmentApp:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("校园活动征招平台")
        self.role = None
        self.user_id = None
        self.create_login_page()

    # 登录页面
    def create_login_page(self):
        self.clear_window()
        tk.Label(self.root, text="用户名:", bg='blue', font=('Arial', 12), width=6, height=2).place(x=100, y=10)
        tk.Label(self.root, text="密码:", bg='blue', font=('Arial', 12), width=6, height=2).place(x=100, y=70)
        self.username_entry = tk.Entry(self.root)
        self.password_entry = tk.Entry(self.root, show="*")
        self.username_entry.place(x=200, y=20)
        self.password_entry.place(x=200, y=80)

        tk.Button(self.root, text="登录", command=self.login).place(x=250, y=120)
        tk.Button(self.root, text="注册", command=self.create_register_page).place(x=250, y=160)
    # 注册页面
    def create_register_page(self):
        self.clear_window()
        tk.Label(self.root, text="用户名:", bg='blue').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="密码:", bg='blue').grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.root, text="角色 (admin/participant):", bg='blue').grid(row=2, column=0, padx=10, pady=10)

        self.reg_username = tk.Entry(self.root)
        self.reg_password = tk.Entry(self.root, show="*")
        self.reg_role = tk.Entry(self.root)
        self.reg_username.grid(row=0, column=1)
        self.reg_password.grid(row=1, column=1)
        self.reg_role.grid(row=2, column=1)

        tk.Button(self.root, text="注册", command=self.register).grid(row=3, column=1, columnspan=2, pady=10)
        tk.Button(self.root, text="返回", command=self.create_login_page).grid(row=4, column=1, columnspan=2)

    # 登录功能
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        query = "SELECT user_id, role FROM users WHERE user_name = %s AND password = %s"
        result = self.db.fetch_all(query, (username, password))

        if result:
            self.user_id = result[0]['user_id']  # 确保 user_id 为整数
            self.role = result[0]['role']

            # 打印角色信息以进行调试
            print(f"登录成功！角色: {self.role}, 用户ID: {self.user_id}")

            # messagebox.showinfo("登录成功", f"欢迎, {username}！")

            # 这里根据角色决定进入哪个页面
            if self.role == "admin":
                self.create_admin_page()  # 如果是管理员，跳转到管理员页面
            else:
                self.create_user_page()  # 如果是普通用户，跳转到普通用户页面
        else:
            messagebox.showerror("错误", "用户名或密码错误！")

    # 注册功能
    def register(self):
        username = self.reg_username.get()
        password = self.reg_password.get()
        role = self.reg_role.get()
        print(username, password, role)
        if role not in ["admin", "participant"]:
            messagebox.showerror("错误", "角色必须是 admin 或 participant！")
            return
        # query = "INSERT INTO users (user_name, password, role) VALUES (%s, %s, %s)"
        # self.db.execute_query(query, (username, password, role))
        if role == "admin":
            query = "INSERT INTO administrator (user_name, password) VALUES (%s, %s)"
            self.db.execute_query(query, (username, password))
            messagebox.showinfo("成功", "管理员注册成功！")
        else:
            query = "INSERT INTO normal_user (user_name, password) VALUES (%s, %s)"
            self.db.execute_query(query, (username, password))
            messagebox.showinfo("成功", "普通用户注册成功！")

        self.create_login_page()

    # 管理员页面
    def create_admin_page(self):
        self.clear_window()
        tk.Label(self.root, text="管理员功能", bg='blue', font=("Arial", 14)).place(x=180, y=10)
        tk.Button(self.root, text="新增活动", command=self.add_activity).place(x=200, y=70)
        tk.Button(self.root, text="查看与修改活动", command=self.admin_view_activities).place(x=190, y=130)
        tk.Button(self.root, text="审核申请", command=self.review_applications).place(x=200, y=190)
        tk.Button(self.root, text="审核记录查看", command=self.applications_history).place(x=190, y=250)
        tk.Button(self.root, text="返回登录界面", command=self.create_login_page).place(x=190, y=310)

    # 普通用户页面
    def create_user_page(self):
        self.clear_window()
        tk.Label(self.root, text="普通用户功能", bg='blue', font=("Arial", 14)).place(x=180, y=10)
        tk.Button(self.root, text="浏览活动", command=self.view_activities).place(x=200, y=70)
        tk.Button(self.root, text="申请参加过的活动", command=self.have_activity).place(x=190, y=130)
        tk.Button(self.root, text="返回登录界面", command=self.create_login_page).place(x=190, y=190)

    # 添加活动功能（管理员）
    def add_activity(self):
        self.clear_window()

        # 添加活动名称、地点、描述和时间的输入框
        tk.Label(self.root, text="活动名称:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="地点:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.root, text="活动描述:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.root, text="活动时间:").grid(row=3, column=0, padx=10, pady=10)

        self.activity_name = tk.Entry(self.root)
        self.activity_location = tk.Entry(self.root)
        self.activity_description = tk.Entry(self.root)
        self.activity_time = tk.Entry(self.root)

        self.activity_name.grid(row=0, column=1)
        self.activity_location.grid(row=1, column=1)
        self.activity_description.grid(row=2, column=1)
        self.activity_time.grid(row=3, column=1)

        tk.Button(self.root, text="确认", command=self.save_activity).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="返回", command=self.create_admin_page).grid(row=5, column=0, columnspan=2)

    # 保存新增的活动
    def save_activity(self):
        name = self.activity_name.get()
        location = self.activity_location.get()
        description = self.activity_description.get()
        time = self.activity_time.get()
        if not name:
            messagebox.showwarning("警告", "活动名不能为空！")
            return
        if not location:
            messagebox.showwarning("警告", "活动地点不能为空！")
            return
        if not description:
            messagebox.showwarning("警告", "活动描述不能为空！")
            return
        if not time:
            messagebox.showwarning("警告", "活动时间不能为空！")
            return

        # SQL 插入活动信息（包含名称、地点、描述和时间）
        query = "INSERT INTO activity (ac_require, ac_place, acdesc, ac_time) VALUES (%s, %s, %s, %s)"
        self.db.execute_query(query, (name, location, description, time))

        messagebox.showinfo("成功", "活动添加成功！")
        self.create_admin_page()

    # 管理员查看和修改活动的功能
    def admin_view_activities(self):
        self.clear_window()
        tk.Label(self.root, text="活动列表", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

        # 从数据库获取所有活动
        query = "SELECT ac_id, ac_require, ac_place, acdesc, ac_time FROM Activity"
        activities = self.db.fetch_all(query)

        if activities:
            t = 0
            for idx, activity in enumerate(activities):
                tk.Label(self.root,
                         text=f"{activity['ac_id']} - {activity['ac_require']}- {activity['ac_place']}- {activity['acdesc']}- {activity['ac_time']}").grid(
                    row=idx + 1, column=0,
                    padx=10, pady=5)
                tk.Button(self.root, text="修改活动",
                          command=lambda aid=activity['ac_id']: self.change_activities(aid)).grid(row=idx + 1,
                                                                                                   column=1,
                                                                                                   pady=5)
                t = t + 1
            tk.Button(self.root, text="返回", command=self.create_admin_page).grid(row=t + 1, column=0, columnspan=2)

        else:
            tk.Label(self.root, text="暂时没有活动哦~").grid(row=1, column=0, columnspan=2)
            tk.Button(self.root, text="返回", command=self.create_admin_page).grid(row=2, column=0, columnspan=2)

    # 修改活动界面
    def change_activities(self,ac_id):
        self.clear_window()
        # 查看该活动原先的数据
        query = f"SELECT ac_require, ac_place, acdesc, ac_time FROM Activity WHERE ac_id = {ac_id}"
        activities = self.db.fetch_all(query)
        print('Niubi')
        # 添加活动名称、地点、描述和时间的输入框
        print(activities)
        tk.Label(self.root, text="活动名称:").grid(row=0, column=0, padx=10, pady=10)
        tk.Label(self.root, text="地点:").grid(row=1, column=0, padx=10, pady=10)
        tk.Label(self.root, text="活动描述:").grid(row=2, column=0, padx=10, pady=10)
        tk.Label(self.root, text="活动时间:").grid(row=3, column=0, padx=10, pady=10)

        self.activity_name = tk.Entry(self.root)
        self.activity_location = tk.Entry(self.root)
        self.activity_description = tk.Entry(self.root)
        self.activity_time = tk.Entry(self.root)
        # 填充文本框内容
        self.activity_name.insert(0,activities[0]["ac_require"])
        self.activity_location.insert(0,activities[0]["ac_place"])
        self.activity_description.insert(0,activities[0]["acdesc"])
        self.activity_time.insert(0,activities[0]["ac_time"])

        self.activity_name.grid(row=0, column=1)
        self.activity_location.grid(row=1, column=1)
        self.activity_description.grid(row=2, column=1)
        self.activity_time.grid(row=3, column=1)

        tk.Button(self.root, text="确认修改", command=lambda aid=ac_id: self.change_activity(aid)).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(self.root, text="返回", command=self.admin_view_activities).grid(row=5, column=0, columnspan=2)

    # 修改功能生效
    def change_activity(self,ac_id):
        name = self.activity_name.get()
        location = self.activity_location.get()
        description = self.activity_description.get()
        time = self.activity_time.get()
        if not name:
            messagebox.showwarning("警告", "活动名不能为空！")
            return
        if not location:
            messagebox.showwarning("警告", "活动地点不能为空！")
            return
        if not description:
            messagebox.showwarning("警告", "活动描述不能为空！")
            return
        if not time:
            messagebox.showwarning("警告", "活动时间不能为空！")
            return

        # SQL 插入活动信息（包含名称、地点、描述和时间）
        query = f"UPDATE activity SET ac_require=%s, ac_place=%s, acdesc=%s, ac_time=%s WHERE ac_id={ac_id}"
        self.db.execute_query(query, (name, location, description, time))

        messagebox.showinfo("成功", "活动修改成功！")
        self.create_admin_page()

    # 审核活动申请界面
    def review_applications(self):
        self.clear_window()
        tk.Label(self.root, text="待审核活动申请", font=("Arial", 14)).grid(row=0, column=0, columnspan=3)

        # 获取所有状态为 'pending' 的申请
        query = """
            SELECT a.req_id, ac.ac_require, u.user_name, a.is_req, u.user_id
            FROM ac_req a
            JOIN activity ac ON a.ac_id = ac.ac_id
            JOIN users u ON a.user_id = u.user_id
            WHERE a.is_req = 'pending'
        """
        applications = self.db.fetch_all(query)

        if applications:
            for idx, application in enumerate(applications):
                # 展示申请的信息
                tk.Label(self.root, text=f"申请活动:{application['ac_require']} - 申请人:{application['user_name']}").grid(row=idx + 1,
                                                                                                     column=0, padx=10,
                                                                                                     pady=5)
                tk.Label(self.root, text=f"状态: {application['is_req']}").grid(row=idx + 1, column=1, padx=10, pady=5)

                # 通过按钮和拒绝按钮
                tk.Button(self.root, text="批准",
                          command=lambda aid=application['req_id']: self.approve_application(aid)).grid(
                    row=idx + 1, column=2, pady=5)
                tk.Button(self.root, text="拒绝",
                          command=lambda aid=application['req_id']: self.reject_application(aid)).grid(
                    row=idx + 1, column=3, pady=5)
        else:
            tk.Label(self.root, text="没有待审核的申请").grid(row=1, column=0, columnspan=4)

        # 返回按钮
        tk.Button(self.root, text="返回", command=self.create_admin_page).grid(row=len(applications) + 2, column=0,
                                                                               columnspan=4, pady=10)

    def approve_application(self, req_id):
        # 更新申请状态为 'approved'
        query = "UPDATE ac_req SET is_req = 'approved' WHERE req_id = %s"
        self.db.execute_query(query, (req_id,))
        # 更新审核历史记录表
        query = "SELECT user_name, password FROM users WHERE user_id = %s"
        result = self.db.fetch_all(query, (self.user_id))
        print(result)
        query = "SELECT admin_id FROM administrator WHERE user_name = %s AND password = %s"
        admin_id = self.db.fetch_all(query, (result[0]["user_name"], result[0]["password"]))
        query = "INSERT INTO shenhe_record(admin_id,req_id,exam_exp) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (admin_id[0]["admin_id"], req_id, "批准"))
        messagebox.showinfo("成功", "申请已批准！")
        self.review_applications()  # 刷新待审核申请列表

    def reject_application(self, req_id):
        # 更新申请状态为 'rejected'
        query = "UPDATE ac_req SET is_req = 'rejected' WHERE req_id = %s"
        self.db.execute_query(query, (req_id,))
        # 更新审核历史记录表
        query = "SELECT user_name, password FROM users WHERE user_id = %s"
        result = self.db.fetch_all(query, (self.user_id))
        query = "SELECT admin_id FROM administrator WHERE user_name = %s AND password = %s"
        admin_id = self.db.fetch_all(query, (result[0]["user_name"], result[0]["password"]))
        query = "INSERT INTO shenhe_record(admin_id,req_id,exam_exp) VALUES (%s, %s, %s)"
        self.db.execute_query(query, (admin_id[0]["admin_id"], req_id, "拒绝"))
        messagebox.showinfo("成功", "申请已拒绝！")
        self.review_applications()  # 刷新待审核申请列表

    # 查看审核历史记录表
    def applications_history(self):
        self.clear_window()
        tk.Label(self.root, text="审核记录", font=("Arial", 14)).grid(row=0, column=0, columnspan=3)

        # 获取所有审核历史记录
        query = """
            SELECT s.exam_id,ac.ac_require,ad.user_name,a.user_id,s.exam_date,a.is_req 
            FROM shenhe_record s
            JOIN ac_req a ON s.req_id = a.req_id
            JOIN activity ac ON ac.ac_id = a.ac_id
            JOIN administrator ad ON ad.admin_id = s.admin_id
        """
        records = self.db.fetch_all(query)

        if records:
            t = 0
            for idx, record in enumerate(records[-20:]):  # 取最后二十条
                tk.Label(self.root,
                         text=f"{record['exam_id']}、活动:{record['ac_require']} 申请人id:{record['user_id']} - 批准情况:{record['is_req']} - 审核员:{record['user_name']}- 审核时间:{record['exam_date']}").grid(
                    row=idx + 1, column=0,
                    padx=10, pady=5)
                t = t + 1
            tk.Label(self.root, text="仅展示最新二十条记录").grid(row=t + 1, column=0, columnspan=2)
            tk.Button(self.root, text="返回", command=self.create_admin_page).grid(row=t + 2, column=0, columnspan=2)
        else:
            tk.Label(self.root, text="最近没有审核记录").grid(row=1, column=0, columnspan=2)
            tk.Button(self.root, text="返回", command=self.create_admin_page).grid(row=2, column=0, columnspan=2)


    # 浏览活动功能
    def view_activities(self):
        self.clear_window()
        tk.Label(self.root, text="活动列表", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

        # 从数据库获取所有活动
        query = "SELECT ac_id, ac_require, ac_place, acdesc, ac_time FROM Activity"
        activities = self.db.fetch_all(query)

        if activities:
            t = 0
            for idx, activity in enumerate(activities):
                tk.Label(self.root,
                         text=f"{activity['ac_id']} - {activity['ac_require']}- {activity['ac_place']}- {activity['acdesc']}- {activity['ac_time']}").grid(
                    row=idx + 1, column=0,
                    padx=10, pady=5)
                tk.Button(self.root, text="申请",
                          command=lambda aid=activity['ac_id']: self.apply_for_activity(aid)).grid(row=idx + 1,
                                                                                                         column=1,
                                                                                                         pady=5)
                t = t + 1
            tk.Button(self.root, text="返回", command=self.create_user_page).grid(row=t + 1, column=0, columnspan=2)

        else:
            tk.Label(self.root, text="暂时没有活动哦~").grid(row=1, column=0, columnspan=2)
            tk.Button(self.root, text="返回", command=self.create_user_page).grid(row=2, column=0, columnspan=2)

    def apply_for_activity(self, activity_id=None):
        if not activity_id:
            messagebox.showwarning("警告", "请选择一个活动来申请！")
            return

        # 确保 user_id 是整数
        self.user_id = int(self.user_id)  # 这里确保 user_id 为整数

        # 申请参加活动的代码
        query = "INSERT INTO ac_req (ac_id, user_id, is_req) VALUES (%s, %s, 'pending')"
        self.db.execute_query(query, (activity_id, self.user_id))
        messagebox.showinfo("成功", "活动申请已提交！")
        # self.create_user_page()

    # 查看申请过的活动功能
    def have_activity(self, ac_id=None):
        self.clear_window()
        tk.Label(self.root, text="申请过的活动列表", font=("Arial", 14)).grid(row=0, column=0, columnspan=2)

        # 确保 user_id 是整数
        self.user_id = int(self.user_id)  # 这里确保 user_id 为整数

        # 申请参加活动的代码
        query = f"""
                    SELECT a.req_id, ac.ac_require, ac.ac_place, ac.acdesc, a.is_req,ac.ac_time
                    FROM ac_req a
                    JOIN activity ac ON a.ac_id = ac.ac_id
                    WHERE a.user_id={self.user_id}
                """
        # query = "SELECT a.ac_id, a.user_id, u.user_name from ac_req a join users u on a.user_id = u.user_id where a.user_id=self.user_id"
        activities = self.db.fetch_all(query)
        if activities:
            t=0
            for idx, activity in enumerate(activities[-20:]):
                tk.Label(self.root,
                         text=f"{idx+1}、{activity['ac_require']}- {activity['ac_place']}- {activity['acdesc']}- 时间:{activity['ac_time']}-通过情况:{activity['is_req']}").grid(
                    row=idx + 1, column=0,
                    padx=10, pady=5)
                t = t+1
            tk.Label(self.root, text="仅展示最新二十条记录").grid(row=t+1, column=0, columnspan=2)
            tk.Button(self.root, text="返回", command=self.create_user_page).grid(row=t+2, column=0, columnspan=2)
        else:
            tk.Label(self.root, text="最近没有申请活动哦~").grid(row=1, column=0, columnspan=2)
            tk.Button(self.root, text="返回", command=self.create_user_page).grid(row=2, column=0, columnspan=2)

    # 清理窗口
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# 启动应用
if __name__ == "__main__":
    root = tk.Tk()  # 创建窗口
    root.geometry('500x500')
    app = ActivityRecruitmentApp(root)
    root.mainloop()

