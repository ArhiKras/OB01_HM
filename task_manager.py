# Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

# Класс Task - Задача
# Конструктор класса Task
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False
        
    # Метод для отметки задачи как выполненной
    def mark_completed(self):
        self.completed = True    
        
    # Строковое представление задачи
    def info(self):
        status = "Выполнено" 
        if self.completed:
            status = "Выполнено"
        else:
            status = "Не выполнено"
        return (f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}")
    
# Класс TaskManager - Менеджер задач
# Конструктор класса TaskManager
class TaskManager:
    def __init__(self):
        self.tasks = []
        
    # Метод для добавления новой задачи
    def add_task(self, description, deadline):
        # Создает новый объект Task с переданными параметрами
        task = Task(description, deadline)
        # Добавляет созданную задачу в список задач
        self.tasks.append(task)
        
    # Метод для отметки задачи как выполненной по индексу
    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index-1].mark_completed()
        else:
            print("Некорректный номер задачи.")
    
    # Метод для получения списка невыполненных задач
    def get_pending_tasks(self):
        return [task for task in self.tasks if not task.completed]
    
# Основная программа    
task_manager = TaskManager()

while True:
    # Меню
    print("\nМенеджер задач")
    print("1. Добавить задачу")
    print("2. Отметить задачу как выполненную")
    print("3. Показать текущие задачи")
    print("4. Выйти")
    
    choice = input("Выберите действие (1-4): ")
    
    # Выбор 1 - Добавить задачу
    if choice == "1":
        description = input("Введите описание задачи: ")
        deadline = input("Введите срок выполнения (например, 31-12-2025): ")
        task_manager.add_task(description, deadline)
        print("Задача добавлена.")
        
    # Выбор 2 - Отметить задачу как выполненную
    elif choice == "2":
        index = int(input("Введите номер задачи для отметки как выполненной (начинается с 1): "))
        task_manager.mark_task_completed(index)
        print("Задача отмечена как выполненная.")
        
    # Выбор 3 - Показать текущие задачи
    elif choice == "3":
        pending_tasks = task_manager.get_pending_tasks()
        if pending_tasks:
            print("\nТекущие задачи:")
            for task in pending_tasks:
                print(task.info())
        else:
            print("\nНет текущих задач.")
            
    # Выбор 4 - Выход
    elif choice == "4":
        print("Программа завершена.")
        break