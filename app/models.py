# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# 配置完setting后使用python manage.py inspectdb > models.py建立数据库对应的model

class AcClass(models.Model):
    class_id = models.AutoField(primary_key=True)
    ac = models.ForeignKey('Activity', models.DO_NOTHING, blank=True, null=True)
    class_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False    # 用于开关数据库
        app_label = 'app'  # 用于确定该model属于哪个app
        db_table = 'ac_class'


class AcReq(models.Model):
    req_id = models.AutoField(primary_key=True)
    exam = models.ForeignKey('ShenheRecord', models.DO_NOTHING, blank=True, null=True)
    ac = models.ForeignKey('Activity', models.DO_NOTHING, blank=True, null=True)
    is_req = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'ac_req'


class Accounts2022155006(models.Model):
    loanno = models.IntegerField(db_column='LOANNO', primary_key=True)  # Field name made lowercase.
    empno = models.DecimalField(db_column='EMPNO', max_digits=4, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    amnt = models.DecimalField(db_column='AMNT', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'accounts2022155006'


class Activity(models.Model):
    ac_id = models.AutoField(primary_key=True)
    ac_time = models.DateTimeField(blank=True, null=True)
    ac_place = models.TextField(blank=True, null=True)
    ac_pe = models.IntegerField(blank=True, null=True)
    ac_require = models.TextField(blank=True, null=True)
    acdesc = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        app_label = 'app'
        db_table = 'activity'


class ActivityEdit(models.Model):
    ac = models.OneToOneField(Activity, models.DO_NOTHING, primary_key=True)  # The composite primary key (ac_id, admin_id) found, that is not supported. The first column is selected.
    admin_id = models.IntegerField()
    ac_time = models.DateTimeField(blank=True, null=True)
    ac_pe = models.IntegerField(blank=True, null=True)
    ac_require = models.TextField(blank=True, null=True)
    modifytime = models.DateTimeField(blank=True, null=True)
    acdesc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_edit'
        app_label = 'app'
        unique_together = (('ac', 'admin_id'),)


class AddActivity(models.Model):
    admin_id = models.AutoField(primary_key=True)  # The composite primary key (admin_id, ac_id) found, that is not supported. The first column is selected.
    ac = models.ForeignKey(Activity, models.DO_NOTHING)
    ac_time = models.DateTimeField(blank=True, null=True)
    ac_pe = models.IntegerField(blank=True, null=True)
    ac_require = models.TextField(blank=True, null=True)
    modifytime = models.DateTimeField(blank=True, null=True)
    acdesc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'add_activity'
        app_label = 'app'
        unique_together = (('admin_id', 'ac'),)


class Administrator(models.Model):
    admin_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administrator'
        app_label = 'app'


class DelActivety(models.Model):
    ac = models.OneToOneField(Activity, models.DO_NOTHING, primary_key=True)  # The composite primary key (ac_id, admin_id) found, that is not supported. The first column is selected.
    admin_id = models.IntegerField()
    deletime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'del_activety'
        unique_together = (('ac', 'admin_id'),)


class Dept2022155006(models.Model):
    deptno = models.IntegerField(db_column='DEPTNO', primary_key=True)  # Field name made lowercase.
    dname = models.CharField(db_column='DNAME', max_length=15, blank=True, null=True)  # Field name made lowercase.
    loc = models.CharField(db_column='LOC', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'dept2022155006'


class Emp2022155006(models.Model):
    empno = models.IntegerField(db_column='EMPNO', primary_key=True)  # Field name made lowercase.
    ename = models.CharField(db_column='ENAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    mgr = models.IntegerField(db_column='MGR', blank=True, null=True)  # Field name made lowercase.
    hiredate = models.DateField(db_column='HIREDATE', blank=True, null=True)  # Field name made lowercase.
    sal = models.IntegerField(db_column='SAL', blank=True, null=True)  # Field name made lowercase.
    comm = models.IntegerField(db_column='COMM', blank=True, null=True)  # Field name made lowercase.
    deptno = models.ForeignKey(Dept2022155006, models.DO_NOTHING, db_column='DEPTNO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'emp2022155006'


class ExamReq(models.Model):
    exam_id = models.IntegerField(primary_key=True)  # The composite primary key (exam_id, req_id) found, that is not supported. The first column is selected.
    req = models.ForeignKey(AcReq, models.DO_NOTHING)
    exam_date = models.DateTimeField(blank=True, null=True)
    exam_exp = models.TextField(blank=True, null=True)
    is_req = models.TextField(blank=True, null=True)
    admin_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'exam_req'
        unique_together = (('exam_id', 'req'),)


class NormalUser(models.Model):
    normal_user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'normal_user'


class ReqActivity(models.Model):
    normal_user_id = models.IntegerField(primary_key=True)  # The composite primary key (normal_user_id, ac_id) found, that is not supported. The first column is selected.
    ac = models.ForeignKey(Activity, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'req_activity'
        app_label = 'app'
        unique_together = (('normal_user_id', 'ac'),)


class ShenheRecord(models.Model):
    exam_id = models.AutoField(primary_key=True)
    admin = models.ForeignKey(Administrator, models.DO_NOTHING, blank=True, null=True)
    req_id = models.IntegerField(blank=True, null=True)
    exam_date = models.DateTimeField(blank=True, null=True)
    exam_exp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'shenhe_record'


class SysConfig(models.Model):
    variable = models.CharField(primary_key=True, max_length=128)
    value = models.CharField(max_length=128, blank=True, null=True)
    set_time = models.DateTimeField(blank=True, null=True)
    set_by = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'sys_config'


class Users(AbstractBaseUser):  # 从django的AbstractBaseUser继承登录状况词条
    # AbstractBaseUser：只包含最基础的字段（如 password 和 last_login），需要手动定义其他字段。
    user_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.TextField(blank=True, null=True)
    # 后续添加，用于使用django的持久化登录login功能
    # auto_now使字段每次在登陆时更新
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        app_label = 'app'
        db_table = 'users'


class UsersReq(models.Model):
    normal_user_id = models.IntegerField(primary_key=True)  # The composite primary key (normal_user_id, req_id) found, that is not supported. The first column is selected.
    req = models.ForeignKey(AcReq, models.DO_NOTHING)
    ac_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    is_req = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'app'
        db_table = 'users_req'
        unique_together = (('normal_user_id', 'req'),)
