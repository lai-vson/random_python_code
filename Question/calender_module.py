# You are given a date. Your task is to find what the day is on that date.

import datetime

if __name__ == '__main__':
    date_ = map(int, input().split())
    date_ =list(date_)
    if date_[2] in range(2000, 3001):
        date_1 = datetime.datetime(date_[2], date_[0], date_[1])
        print(date_1.strftime("%A").upper())
