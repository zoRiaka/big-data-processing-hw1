# this is an easy program to test the work with docker containers
from datetime import datetime


def print_date(name):
    now = datetime.now()

    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f'Current time: {current_time} \nName: {name}')


if __name__ == '__main__':
    print_date('Zoryana Herman')
