from enum import Enum


class Node:
    def __init__(self):
        self.value = None
        self.key = None
        self.FREE = True
        self.DELETED = False
        self.TAKEN = False


def hash(key, n):
    idx = 0
    for ch in key:
        idx += ord(ch) * 37
        idx %= n
    return idx


def insert(arr, val, key, n):
    idx = hash(key, n)
    for i in range(n):
        idx += 37  # 37 i n są względnie pierwsze, bo n jest potega dwojki
        idx %= n
        if arr[idx].FREE or arr[idx].DELETED:
            arr[idx].value = val
            arr[idx].key = key

            arr[idx].TAKEN = True
            arr[idx].FREE = False
            arr[idx].DELETED = False
            return
    print("Tablica jest przepełniona")


def remove(arr, key, n):
    idx = hash(key, n)
    for i in range(n):
        idx += 37
        idx %= n
        if arr[idx].FREE:
            break
        if arr[idx].key == key:
            arr[idx].TAKEN = False
            arr[idx].DELETED = True
            return
    print("Nie znaleziono klucza!")


def find(arr, key, n):
    idx = hash(key, n)
    for i in range(n):
        idx += 37
        idx %= n
        if arr[idx].FREE:
            break
        if arr[idx].key == key and arr[idx].TAKEN:
            print("Val [", key, "]:", arr[idx].value)
            return
    print("Nie znaleziono klucza!")


def pow2(n):
    l = 1
    while l < n:
        l *= 2
    return l


while True:

    n = int(input("How big table?"))
    n = pow2(n)
    to_add = int(input("How many add?"))
    to_remove = int(input("How many remove?"))
    to_find = int(input("How many find"))

    array = [Node() for _ in range(n)]

    for i in range(to_add):
        key = input("Enter the key to add:")
        val = int(input("Enter the value to add:"))
        insert(array, val, key, n)

    for i in range(to_remove):
        key = input("Enter the key to remove:")
        remove(array, key, n)

    for i in range(to_find):
        key = input("Enter the key to find: ")
        find(array, key, n)
    break

