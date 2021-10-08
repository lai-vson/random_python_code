import datetime


def timeConversion(s):
    s = datetime.datetime.strptime(s, '%I:%M:%S%p')
    return s.strftime('%H:%M:%S')

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
