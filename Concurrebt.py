from concurrent import futures
import time


def sample_func(index):
    print('index: %s started.' % index)
    sleep_seconds = random.randint(2, 4)
    time.sleep(sleep_seconds)
    print('index: %s ended.' % index)
    return index*2

future_list = []
with futures.ThreadPoolExecutor(max_workers=4) as executor:
    for i in range(4):
        future = executor.submit(fn=sample_func, index=i)
        future_list.append(future)
for i in futures.as_completed(fs=future_list):
    print(i.result(),"index:",future_list.index(i))

print('completed.')
