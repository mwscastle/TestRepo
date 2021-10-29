import pathlib

CENTER_INTERVAL_LENGTH = 4
MAJOR_UNIT_TICK_LENGTH = CENTER_INTERVAL_LENGTH + 1
TICK_CHAR = '-'
NUM_MAJOR_UNITS = 2

def print_tick(length, label=''):
    tick_string = f'{TICK_CHAR * length}\t{label}'
    print(tick_string)


def generate_label(center_interval, major_tick_num):
    label_length = 1 / 2**(MAJOR_UNIT_TICK_LENGTH - center_interval)
    if label_length == 1:
        label_length *= major_tick_num
    return f'{label_length:0.02f}'


def print_interval(center_interval, major_tick_num):
    if not center_interval:
        return
    print_interval(center_interval - 1, major_tick_num)
    print_tick(center_interval, generate_label(center_interval, major_tick_num))
    print_interval(center_interval - 1, major_tick_num)


def print_ruler():
    print('\n\n')
    print_tick(MAJOR_UNIT_TICK_LENGTH, 0)
    for major_unit in range(NUM_MAJOR_UNITS):
        print_interval(CENTER_INTERVAL_LENGTH, major_unit)
        print_tick(MAJOR_UNIT_TICK_LENGTH, f'{major_unit+1:0.02f}')
    print('\n\n')


def main():
    print_ruler()


if __name__ == '__main__':
    main()
