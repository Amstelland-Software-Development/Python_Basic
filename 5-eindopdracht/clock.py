#! python3
from time import sleep
from datetime import datetime



def main():
    while True:
        # print(datetime.now().strftime(t_format), end="\r")
        print(datetime.now().strftime("%H:%M:%S"))
        sleep(1)


if __name__ == "__main__":
    main()
