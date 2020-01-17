''' Function to continually run code in second(s) interval'''
import time
import datetime

def cron(seconds):
    while True:
        d = datetime.datetime.now()
        print(d)
        time.sleep(seconds)

def main():
    cron(10)

if __name__ == '__main__':
    main()