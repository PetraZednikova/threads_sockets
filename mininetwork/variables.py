import threading
import time



def find_largest(numbers):
    largest = max(numbers)
    time.sleep(0.1)
    numbers.pop(0)

    print(f"Largest value: {largest}")


def find_smallest(numbers):
    smallest = min(numbers)
    print(f"Smallest value: {smallest}")


user_values = input("Enter values separated by commas: ")
values_list = [int(x) for x in user_values.split(',')]

thread_largest = threading.Thread(target=find_largest, args=(values_list,))
thread_smallest = threading.Thread(target=find_smallest, args=(values_list,))

thread_largest.start()
thread_smallest.start()

thread_largest.join()
thread_smallest.join()

"""
class C:
    def start(self):
        self.target(self.args)"""