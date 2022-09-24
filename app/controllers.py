import responder
import os
from datetime import datetime

from app.store import insert_data, remove_data, select_data, select_filter_data
from app.judge import judge
from app.line import line_bot

api = responder.API(
  templates_dir='app/templates',
  static_dir='app/static',
  secret_key=os.urandom(24)
)

class IndexController:
  async def on_get(self, req, resp): #HTTP method get
    name = req.session.get('Name')
    users = select_data()
    if not name:
      api.redirect(resp,'/')
    resp.content = api.template('index.html',name=name,users=users)

  async def on_post(self, req, resp): #HTTP method post
    users = select_data()
    data = await req.media()
    name = req.session.get('Name')
    time = data.get('time')
    resp.session['Name']=name
    resp.session['Time']=time
    time = datetime.strptime(time, '%Y-%m-%d %H:%M')
    flag = judge(users,name,time)
    if type(flag) == str:
      resp.session['Name2'] = flag
      api.redirect(resp, '/match')
    elif flag == 1:
      api.redirect(resp, '/duplicate')
    else:
      api.redirect(resp, '/insert')

class LoginController:
  async def on_get(self, req, resp): #HTTP method get
    resp.content = api.template('login.html')

  async def on_post(self, req, resp): #HTTP method post
    data = await req.media()
    name = data.get('name')
    resp.session['Name']=name
    api.redirect(resp, '/index')

class InsertController:
  async def on_get(self, req, resp): #HTTP method get
    @api.background.task
    def db_save(name,time):
      insert_data(name,time)
    name = req.session.get('Name')
    time = req.session.get('Time')
    time = datetime.strptime(time, '%Y-%m-%d %H:%M')
    db_save(name,time)
    resp.content = api.template('insert.html',name=name)

class MatchController:
  async def on_get(self, req, resp): #HTTP method get
    @api.background.task
    def line_api(name1,name2,time):
      line_bot(name1,name2,time)
      time = datetime.strptime(time, '%Y-%m-%d %H:%M')
      remove_data(name2,time)
    name1 = req.session.get('Name')
    name2 = req.session.get('Name2')
    time = req.session.get('Time')
    line_api(name1,name2,time)
    resp.content = api.template('match.html')

class DuplicateController:
  async def on_get(self, req, resp): #HTTP method get
    name = req.session.get('Name')
    time = req.session.get('Time')
    resp.content = api.template('duplicate.html',name=name,time=time)

class DetailController:
  async def on_get(self, req, resp, name): #HTTP method get
    times = select_filter_data(name)
    resp.content = api.template('detail.html',name=name,times=times)

class DeleteContoroller:
 async def on_get(self, req, resp, name, time): #HTTP method get
   @api.background.task
   def delete_data(name,time):
     remove_data(name,time)
   time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
   delete_data(name, time)
   resp.content = api.template('delete.html',name=name,time=time)