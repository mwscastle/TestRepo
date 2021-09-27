import pathlib

CENTER_INTERVAL_LENGTH = 5
MAJOR_UNIT_TICK_LENGTH = CENTER_INTERVAL_LENGTH + 1
TICK_CHAR = '-'
NUM_MAJOR_UNITS = 4

def print_tick(length):
    tick_string = TICK_CHAR * length
    print(tick_string)


def print_interval(center_interval):
    if not center_interval:
        return
    print_interval(center_interval - 1)
    print_tick(center_interval)
    print_interval(center_interval - 1)


def print_ruler():
    print('\n\n')
    print_tick(MAJOR_UNIT_TICK_LENGTH)
    for major_unit in range(NUM_MAJOR_UNITS):
        print_interval(CENTER_INTERVAL_LENGTH)
        print_tick(MAJOR_UNIT_TICK_LENGTH)
    print('\n\n')


def main():
    print_ruler()


if __name__ == '__main__':
    main()
