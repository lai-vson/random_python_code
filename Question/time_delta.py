# You are given a date. Your task is to find difference in between to date. Format:Day dd Mon yyyy hh:mm:ss +xxxx

from datetime import datetime

if __name__ == '__main__':
    time_list = []
    for _ in range(int(input())):
        t1 = input()
        t1 = datetime.strptime(t1, '%a %d %b %Y %H:%M:%S %z')
        t1_d = datetime(year=t1.year, month=t1.month, day=t1.day, hour=t1.hour, minute=t1.minute,
                         second=t1.second)
        t2 = input()
        t2 = datetime.strptime(t2, '%a %d %b %Y %H:%M:%S %z')
        t2_d = datetime(year=t2.year, month=t2.month, day=t2.day, hour=t2.hour, minute=t2.minute,
                                  second=t2.second)
        t3 = abs((t1-t2).total_seconds())
        time_list.append('{0:.0f}'.format(t3))

    for x in range(len(time_list)):
        print(time_list[x], end="\n")

