""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc

def approximate_pi(n): # Ex1
    #n is the number of points
    # Write your code here
    cords = [[random.uniform(-1, 1), random.uniform(-1, 1)] for _ in range(n)]
    x = [p[0] for p in cords]
    y = [p[1] for p in cords]
    plt.figure(figsize=(5,5))
    plt.scatter(x, y, s=5)
    plt.title(f"Cords (n = {n})")
    plt.axis("Equal")
    plt.show()
    ns = [elem for elem in cords if elem[0]**2 + elem[1]**2 >= 1]
    nc = [elem for elem in cords if elem[0]**2 + elem[1]**2 < 1]
    pi = 4*(len(nc)/(len(nc)+len(ns)))
    print(pi)
    return pi

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere
    cords = [[random.uniform(-1, 1) for _ in range(d)] for _ in range(n)]
    ns = [elem for elem in cords if sum([elemm**2 for elemm in elem]) >= 1]
    nc = [elem for elem in cords if sum([elemm**2 for elemm in elem]) < 1]
    pi = 4*(len(nc)/(len(nc)+len(ns)))
    v = (m.pi**(d/2)) / m.gamma((d/2) + 1)
    return v

def hypersphere_exact(n,d): #Ex2, real value
     #n is the number of points
    # d is the number of dimensions of the sphere 
    v = (m.pi**(d/2)) / m.gamma((d/2) + 1)
    return v

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np=10):
      #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    with future.ProcessPoolExecutor() as ex:
        futures = [ex.submit(sphere_volume, n, d) for _ in range(np)]
        results = [f.result() for f in futures]
    return mean(results)

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    chunk = n // np
    with future.ProcessPoolExecutor() as ex:
        futures = [ex.submit(sphere_volume, chunk, d) for _ in range(np)]
        results = [f.result() for f in futures]
    return mean(results)
    
def main():
    #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    #Ex2
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(n,d)}")
 
    #Ex3
    n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")

    start = pc()
    r = sphere_volume_parallel1(n, d)
    print(r)
    stop = pc()
    print(f"Ex3: Parallel time of {d} and {n}: {stop-start}")

    #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")
    start = pc()
    sphere_volume_parallel2(n, d)
    stop = pc()
    print(f"Ex4: Parallel time of {d} and {n}: {stop-start}")

if __name__ == '__main__':
	main()
