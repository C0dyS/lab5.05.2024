import time
import json
import os


def timer():
    filename = 'data_time.json'
    start_time = time.time()

    if os.path.isfile(filename):
        with open(filename) as file1:
            elapsed_time = json.load(file1)
            elapsed_time = float(elapsed_time)
    else:
        elapsed_time = 0

    a = 0

    while a != 15:
        a += 1
        end_time = time.time()

        time.sleep(1)
        print(f'end time = {end_time}')
        print(f'elapsed time = {elapsed_time}')

        if a % 5 == 0:
            elapsed_time += end_time - start_time
            start_time = end_time
            with open('data_time.json', 'w') as file:
                json.dump(elapsed_time, file)

timer()