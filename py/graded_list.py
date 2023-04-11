def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
      #print(event.user)
      #print(event.date)
      #print(event.type)
      #print(event.machine)
      if event.machine not in machines:
          machines[event.machine] = []
      if event.type == "login":
          machines[event.machine].append(event.user)
      elif event.type == "logout":
          lf = "NF"
          for i, user in enumerate(machines[event.machine]):
             print(user)
             if event.user == user:
                 machines[event.machine].pop(i)
                 lf ="F"
          if lf == "NF":
              print("The user {user} in machine {mac} is not found".format(user=event.user, mac=event.machine))
    return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))


class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user


events = [
    Event('2020-01-01 12:45:56', 'login', 'myworkstation.local', 'herve'),
    Event('2020-01-01 13:45:56', 'login', 'myworkstation.local', 'kha'),
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

generate_report(users)
