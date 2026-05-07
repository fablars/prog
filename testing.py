import random
import concurrent.futures as future
from time import perf_counter as pc
from time import sleep as pause


cords = [[random.uniform(-1, 1) for _ in range(3)] for _ in range(5)]

def runner(n):
    print(f"Performing costly function{n}")
    pause(n)
    return f"Function {n} has completed"

start = pc()
with future.ProcessPoolExecutor() as ex:
    p = [5,4,3,2,1]
    results = ex.map(runner, p)

    for r in results:
        print(r)
        
end = pc()
print(f"Process took {round(end-start, 2)} seconds")

