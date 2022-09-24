def judge(users,name,time):
  flag = 0
  for user in users:
    if user['name'] != name and user['time'] == time:
      flag = user['name']
      break
    if user['name'] == name and user['time'] == time:
      flag = 1
      break
  return flag