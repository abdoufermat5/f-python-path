import datetime
if __name__ == "__main__":
    print(format(45, 'b'))  # binary
    print(format(45, 'x'))  # hex
    print(format(45, 'o'))  # octal
    print(format(45, 'd'))  # decimal

    print(format(2/3, '.1%'))  # percentage
    print(format(2/3, '.1f'))  # float
    print(format(15000000, '.2e'))  # scientific notation

    now = datetime.datetime.now()
    print(format(now, '%H:%M:%S'))
    print(format(now, '%Y-%m-%d %H:%M:%S'))
    print(format(now, '%c'))
    print(format(now, '%x'))
    print(format(now, '%X %p'))
