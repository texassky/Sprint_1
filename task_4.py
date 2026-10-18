
# Списки задач new_tasks и completed_tasks
new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

# 1. Переносим задачу task_005 из списка new_tasks в список completed_tasks в одно действие
completed_tasks.append(new_tasks.pop(-1))

# 2. Удалякм запрос task_007 из списка new_tasks.
new_tasks.remove('task_007')

# 3. Выводим на экран последнюю задачу из списка new_tasks 
print(new_tasks[-1])