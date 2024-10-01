import subprocess
import time

programs = [
    'python3 ray-cast.py',
    './out',
    'java RayCasting',
    'java RayCasting2'
]

for program in programs:
    start = time.time()
    i = 0

    while time.time() - start < 30: # run for 30 seconds
        subprocess.run(program, shell=True, stdout=subprocess.PIPE)
        i += 1

    print(f'done: {program} ({i} executions)')

    time.sleep(10)