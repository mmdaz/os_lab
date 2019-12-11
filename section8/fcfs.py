from section8.process import Process


def first_come_first_serve(task_list: list):
    ticks = 0
    for i, task in enumerate(task_list):
        task.run(task.cbt)
        ticks += task.cbt
        print("Current process : {}".format(i))
        task.set_end_time(ticks)

    for i, t in enumerate(tasks):
        print("task {} ends in {}".format(i, t.end_time))


if __name__ == "__main__":
    tasks = [Process(int(cbt), 0, 0) for cbt in input().split()]
    first_come_first_serve(tasks)
