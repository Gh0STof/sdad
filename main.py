"""
    Точка входа в приложение Task Manager
    version 0.0.4
    --- description ---
    проложение может сохранять задачи,
    редактировать, выдает список задач
    и может удалять задачу.
"""

"""функция выводит уведомления в консоль"""
def show_message(message=None):
    if message is not None:
        print(f"Новая задача {message} успешно добавлена!")
    input("Нажмите ENTER для продолжения")


def check_confirm(action: str):
    confirm = input("Вы действительно хотите выйти из приложения? Да/ Нет")
    if (confirm.capitalize().startswith('') == 'Y'
        or confirm.capitalize().startswith('') == 'N'
        or confirm.capitalize().startswith('') == 'Д'
        or confirm.capitalize().startswith('') == 'Н'):
    print(action)
    return False
else:
    print("Не правильный ввод!")
    return True

def show_collection(task_list):
    print("=" * 30)
    for i, j in enumerate(task_list):
        print(i + 1, j)
    print("=" * 30)

is_running = True
collection = ["task 1", "task 2"] # list

print("Добро пожаловать!")
while is_running:
    print("1 - посмотреть задачи \n"
          "2 - добавить задачу \n"
          "3 - редактирование задачи \n"
          "4 - удаление задачи \n"
          "5 - выход")

    choice_user = input("Введите свой выбор")
    match str(choice_user):
        case '1':
            show_collection(collection)
            show_message()
        case '2':
            add_task = input("Введите имя задачи для добавления")
            collection.append(add_task)
            show_message(add_task)
        case '3':
            show_collection(collection)
            select_task = int(input("Введите номер задачи"))
            delete_task = input("Введите новое имя задачи для удаления")
            collection[select_task - 1] = edit_task
            show_message(edit_task)
        case '4':
            show_collection(collection)
            delete_task = int(input("Ведите номер задачи для удаления"))
            if check_confirm("Удаление прошло успешно!"):
                collection.pop(delete_task - 1)
                show_message(delete_task)
        case '5':
           is_running = check_confirm("До свидания!")
        case _:
            print("Такого пункта нет!")
