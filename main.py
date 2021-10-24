#!/usr/bin/env python3
import math

def heapify_up(heap, i):
    if i > 1:
        parent = math.floor(i/2)
        if heap[i] < heap[parent]:
            temp = heap[parent]
            heap[parent] = heap[i]
            heap[i] = temp
            return heapify_up(heap, parent)
    return heap

def heapify_down(heap, i):
    n = len(heap) - 1
    if 2 * i > n:
        return heap
    elif 2 * i < n:
        left = 2 * i
        right = 2 * i + 1
        j = left if heap[left] < heap[right] else right
    elif 2 * i == n:
        j = 2 * i
    if heap[i] > heap[j]:
        temp = heap[i]
        heap[i] = heap[j]
        heap[j] = temp
        return heapify_down(heap, j)
    else:
        return heap

def insert(heap, v):
    heap.append(v) 
    return heapify_up(heap, len(heap) - 1)

def find_min(heap):
    if len(heap) - 1 > 1:
        return heap[1]
    else:
        raise("Heap is empty")

def delete(heap, i):
    if i > len(heap) - 1:
        raise("Out of bound index in Heap")
    else:
        deleted_element = heap[i]
        replaced_element = heap.pop()
        heap[i] = replaced_element
        heap = heapify_up(heap, i)
        heap = heapify_down(heap, i)
        return heap

def extract_min(heap):
    if len(heap) - 1 < 1:
        raise("Heap is empty")
    print("Minimum is {}".format(heap[1]))
    return delete(heap, 1)

heap = []
heap.append('')
heap = insert(heap, 10)
heap = insert(heap, 3)
heap = insert(heap, 5)
heap = insert(heap, 4)
heap = insert(heap, 20)
heap = insert(heap, 2)
print(heap)
heap = delete(heap, 2)
print(heap)
print(find_min(heap))
print(extract_min(heap))
print(extract_min(heap))
