import sys
import time

WIDTH = 50

for i in range(WIDTH):
    left = ' ' * i + '#'
    right = ' ' * (WIDTH - i - 1) + '#'

    print(f"{left:<{WIDTH}}")
    print(f"{right:<{WIDTH}}")

    time.sleep(0.15)

    print('\033[F\033[F', end='')
    sys.stdout.flush()
