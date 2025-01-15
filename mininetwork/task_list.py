import threading


result = 0


def list_sum(values):
    global result
    local_sum = sum(values)  # Calculate the sum of a subset of the list
    with result_lock:  # Ensure thread-safe access to the shared variable
        result += local_sum


values_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

mid_index = len(values_list) // 2
list1 = values_list[:mid_index]
list2 = values_list[mid_index:]

thread1 = threading.Thread(target=list_sum, args=())
thread2 = threading.Thread(target=list_sum, args=())

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(result)