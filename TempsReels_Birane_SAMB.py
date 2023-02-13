import threading
import time
import datetime
import random

Tank = []
motors =0
wheels=0

class my_task():
    name = None
    period = -1
    execution_time = -1
    job = ""
    production = None

    ############################################################################
    def __init__(self, name, period, execution_time, job, Tank=False):
        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.job = job
        self.Tank = Tank

    ############################################################################
    def run(self):

        # Update last_execution_time

        global Tank
        global motors, wheels

        # print(self.name + " : Starting task (" + self.last_execution_time.strftime( "%H:%M:%S") + ") : execution time = " + str(execution_time))
        print("\n")
        print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : Starting task ")
        print("\t \t \tJob: " + self.job)

        # FIFO DATA

        if (self.Tank == True):
            if self.name == "Pump2":
                Tank.append(20)
            if self.name == "Pump1":
                Tank.append(10)
        # if not data in fifo_data :
        #    fifo_data.append(data)

        if self.Tank == False:
            while (len(Tank) > 0):
                print("read FIFO")#datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + ":" + fifo_data[0])

        time.sleep(self.execution_time)
        print(datetime.datetime.now().strftime("%H:%M:%S") + "\t" + self.name + " : Ending task ")

if __name__ == '__main__':

    last_execution = datetime.datetime.now()

    # Instanciation of task objects

    task_list = []
    task_list.append(my_task(name="Pump2", period=15, execution_time=3, job="Produce 20 Oil", Tank=True))
    task_list.append(my_task(name="Pump1", period=5, execution_time=2, job="Produce 10 Oil", Tank=True))
    task_list.append(my_task(name="Pump2", period=15, execution_time=3, job="Produce 20 Oil", Tank=True))
    task_list.append(my_task(name="Machine 1", period=5, execution_time=5, job="Produce 1 Motore", Tank=True))
    task_list.append(my_task(name="Machine 2", period=5, execution_time=3, job="Produce 1 wheel", Tank=True))
    task_list.append(my_task(name="Machine 2", period=5, execution_time=3, job="Produce 1 wheel", Tank=True))
    task_list.append(my_task(name="Machine 2", period=5, execution_time=3, job="Produce 1 wheel", Tank=True))
    task_list.append(my_task(name="Machine 2", period=5, execution_time=3, job="Produce 1 wheel", Tank=True))

    while (1):
        time_now = datetime.datetime.now()
        print("\nScheduler tick : " + time_now.strftime("%H:%M:%S"))
        for current_task in task_list[:3]:
            if sum(Tank) < 55:
                current_task.run()

        Tank_total = sum(Tank)

        for current_task in task_list[3:9]:

            if Tank_total > 0 :
                if current_task.name =="Machine 1" :
                    current_task.run()
                    Tank_total -= 25
                    motors += 1



                if current_task.name == "Machine 2":
                    current_task.run()
                    Tank_total -= 5
                    wheels += 1

        print(datetime.datetime.now().strftime("%H:%M:%S"), ": Stock 1 has {}  wheels and Stock2 has {} motors .".format(wheels, motors))

        Tank =[]

