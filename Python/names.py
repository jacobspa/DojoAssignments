#Part 1
# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# def concate(names):
#     for key in students:
#         print key["first_name"] + " " + key["last_name"]
#
# concate(students)

#Part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def partTwo(userList):
    for key, data in users.items():
        counter = 0;
        for value in data:
            counter += 1
            amount = len(value["first_name"])+ len(value["last_name"])
            print counter,value["first_name"] + " " + value["last_name"],amount

partTwo(users)
