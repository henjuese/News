# *_* coding: utf-8 *_*
__author__ = 'Xsoda'

from app.controller.Base import BaseHandler
from core.web.encrypt import check_password, encrypt_password
from core.db.database import OperationalError, IntegrityError

class Login(BaseHandler):
    def get(self):
        self.write(self.serve_template("login.html", **{'xsrf': self.xsrf_form_html()}))
        self.flush()

    def post(self):
        user_name = self.get_argument("user_name", None)
        user_password = self.get_argument("user_password", None)
        if user_name and user_password:
            userinfo = self.db.get("select id, name, password, salt, salt, email from usr where name='%s';" % user_name)
            if userinfo and check_password(user_password, userinfo['password'], userinfo['salt']):
                self.session['user'] = userinfo
                self.session.save()
                self.write('done')
            else:
                self.write('user name or password error!')
        else:
            self.write('user name or password is empty!')
        self.flush()

class Register(BaseHandler):
    def get(self):
        self.write(self.serve_template("register.html", **{'xsrf': self.xsrf_form_html()}))
        self.flush()
        
    def post(self):
        user_name = self.get_argument("user_name", None)
        user_password = self.get_argument("user_password", None)
        repeat_password = self.get_argument("repeat_password", None)
        email = self.get_argument('email', None)
        if user_password == repeat_password:
            enc_pwd, salt = encrypt_password(user_password)
            if enc_pwd is not 'error':
                try:
                    self.db.execute("insert into usr(name, password, salt, email, grade) values(%s, %s, %s, %s, 0);", *(user_name, enc_pwd, salt, email))
                    self.write('done')
                except IntegrityError:
                    self.write('db error')
            else:
                self.write('operational error')
        else:
            self.write('pwd error')
        self.flush()
                    