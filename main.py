import pickle
import datetime
import tkinter as tk

data = [[1950, 2, "Test"]]

time = datetime.datetime.now()

print("To-do things")

def get_done():
    data = load()
    for i in range(len(data)):
        if time.day >= data[i][1] and (time.hour*100 + time.minute) >= data[i][0]:
            print(data[i][2])


def new_todo():
    day = input("day: ")
    hour = input("hour: ")
    min = input("minute: ")
    desc = input("desc: ")
    data.append([int(hour)*100 + int(min), int(day), desc])
    save()

def save():
    file = open("data.todo", 'wb')
    pickle.dump(data, file)
    file.close()

def load():
    file = open("data.todo", 'rb')
    new_data = pickle.load(file)
    file.close()
    return new_data

def del_exp():
    for i in reversed(range(len(data))):
        if time.day >= data[i][1] and (time.hour*100 + time.minute) >= data[i][0]:
            data.remove(data[i])
    save()

def main():
    action = input("Chose between New / expired / all: ").lower()

    if action == "new":
        new_todo()
    elif action == "all":
        data = load()
        print(data)
    else:
        get_done()

        if input("Delete expired? ").lower() == "yes":
            del_exp()

    if input("Need something else? ").lower() == "yes":
        main()

main()