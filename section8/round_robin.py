from section8.process import Process


def task_exist(tasks_list, quantum):
    for task in tasks_list:
        if not task.is_finished(quantum=quantum):
            return True

    return False


def round_robin(task_list: list, quantum: int):
    ticks = 0

    while task_exist(tasks_list=task_list, quantum=quantum):
        for i, task in enumerate(task_list):
            task.run(quantum)
            ticks += quantum
            print("Current process : {}".format(i))
            task.set_end_time(ticks)

        for i, t in enumerate(task_list):
            print("task {} ends in {}".format(i, t.end_time))


if __name__ == '__main__':
    tasks = [Process(int(cbt), 0, 0) for cbt in input().split()]
    round_robin(tasks, int(input("enter quantum: \n")))
