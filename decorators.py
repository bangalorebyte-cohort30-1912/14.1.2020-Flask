from datetime import datetime
import time

def timer(func):
    def wrapper():
        before = datetime.now()
        func()
        time_taken = datetime.now() - before
        print(f"time take for function to execute is {time_taken} seconds")
    return wrapper


def say_whee():
    time.sleep(2)
    print("Whee!")

def some_new_function():
    time.sleep(3)
    print("doing some heavy work")

@timer
def say_hello():
    time.sleep(1)
    print("hello")
    return

if __name__ == "__main__":
    say_hello()
