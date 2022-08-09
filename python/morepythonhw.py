# n = int(input('Please enter a number: '))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
# print(fact)
#------------------------------------------------
toDo = input('''
Press 1 to add a task
Press 2 to delete task
Press 3 to view tasks
Press q to quit''')

toDo_list=[]
for entry in toDo:
    if entry=='1':
        new_toDo=input('Please enter your new to-do item and the priority: ')
        toDo_list.append(new_toDo)
    elif entry=='2':
        print(toDo_list)
        delete_toDo = input('Enter the index of the task you want to delete: ')
        toDo_list.pop(int(delete_toDo))
    elif entry=='3':
        print(toDo_list)
    elif entry=='q':
        print('Goodbye')



