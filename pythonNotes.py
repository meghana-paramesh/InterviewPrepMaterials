import math
from collections import deque
import heapq
import copy
import requests


def main():
    print(math.ceil(3 / 2))
    print(math.floor(3 / 2))
    print(math.fmod(-10, 3))
    print(math.sqrt(4))
    print(math.pow(4, 2))

    print(float("inf") < math.pow(200, 2))

    arr = [1, 12, 10, 9, 2, 3, 4, 5]
    arr10 = copy.copy(arr)
    arr11 = copy.deepcopy(arr)

    arr.append(100)
    arr.insert(0, 200)
    arr[1] = 9
    print(arr)
    print(arr[-1])
    print(arr[1:5])
    arr[0] = 500
    print("original: ", arr)
    print("shallow cops: ", arr10)
    print("deep copy ", arr11)

    # initialize an array of vaiable size
    arr1 = [1] * 3
    print(arr1)
    a, b, c = [1, 2, 3]

    for i in range(1, 5):
        print(i, end=" ")
    print()

    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]

    for n1, n2 in zip(nums1, nums2):
        print(n1, n2)

    arr.reverse()
    print(arr)
    arr.sort()
    print(arr)
    arr.sort(reverse=True)
    print(arr)

    for i in range(len(arr)):
        print(i, arr[i])

    for i, n in enumerate(arr):
        print(i, n)
    str_arr = ["meg", "chandu", "hubby", "ammu"]
    str_arr.sort()
    print(str_arr)
    str_arr.sort(key=lambda x: len(x))
    print(str_arr)

    arr2 = [i * i for i in range(5)]
    print(arr2)

    arr3 = [[0] * 4 for i in range(4)]
    print(arr3)

    # strings are immutable in python as well. Whenever we modify a string a new string is created. We can't modify a charcter at an index in a string (example: s[0]='c' is not supported)
    s = "meghana"
    print(s[0:6])

    # string can be converted to intergers and integers can be converted into strings
    print(int("123") + int("123"))
    print(str(123) + str(123))

    # ascii value of the characters can be obtained using the function ord
    print(ord("a"))
    print(ord("b"))

    # we can concate the string using a delimeter
    strings = ["ab", "cd", "ef"]
    print(" ".join(strings))

    # queues in python are double ended queues by default. Right append=append. Left append=appendLeft. Right pop=pop, Left pop=popLeft
    queue = deque()
    queue.append(1)
    queue.appendleft(2)
    queue.appendleft(3)
    print(queue)
    queue.popleft()
    print(queue)

    # hashset. Similar to java they provide constant time add and remove operation
    mySet = set()
    mySet.add(1)
    mySet.add(2)
    mySet.add(5)
    mySet.add(9)

    print(1 in mySet)
    print(9 in mySet)
    print(4 in mySet)
    print(len(mySet))
    mySet.remove(1)
    print(mySet)

    # hashmap aka dictionary. {} is saved for this
    myMap = {}
    myMap["alice"] = 88
    myMap["bob"] = 90
    print(myMap)
    myMap["alice"] = 80
    print(myMap["alice"])

    print("alice" in myMap)
    myMap.pop("alice")
    print("alice" in myMap)
    myMap1 = {"alice": 1, "bob": 2}
    print(myMap1)
    myMap["alice"] = 80

    # Fancy way dict comprehension
    myMapFancy = {i: 2 * i for i in range(5)}
    print(myMapFancy)

    # looping through the map
    for key in myMap:
        print(key, myMap[key])

    for val in myMap.values():
        print(val)

    for key, val in myMap.items():
        print(key, val)

    # tuples are similar to arrays but they are initialized using () instead of [] in arrays. They are immutable as well
    tup = (1, 2, 3)

    # can't do tup[0]=0 won't work

    # but on a brigher side tupes are useful as the hashable key for map. Note that this is specifically useful because list can't be used as keys in the map
    # instead of (1,2) we can't use [1,2]
    myMap3 = {(1, 2): 3}
    print(myMap3[(1, 2)])

    mySet3 = set()
    mySet3.add((1, 2))

    print((1, 2) in mySet3)

    # under the hood heaps are implemented using arrays. By default heaps in python are minHeaps similar to Java
    minHeap = []
    heapq.heappush(minHeap, 3)
    heapq.heappush(minHeap, 2)
    heapq.heappush(minHeap, 5)

    while len(minHeap):
        print(heapq.heappop(minHeap))

    # to get maxHeap just multiply by -1 while pushing and once retrieved from the heap again multiply by -1 to get the original value
    maxHeap = []
    heapq.heappush(maxHeap, -3)
    heapq.heappush(maxHeap, -4)
    heapq.heappush(maxHeap, -8)
    print(-1 * maxHeap[0])

    print("------------------------------------------------------------")
    arr4 = [3, 4, 2, 1]
    heapq.heapify(arr4)

    while len(arr4):
        print(heapq.heappop(arr4))

    # inner function will have all the access to the values of the outer function by default


# Can modify object but can't reassign unless we use a nonlocal keyword
def outer(a, b):
    c = "c"

    def inner():
        return str(a) + str(b) + c

    print(inner())


def double(arr, val):
    def helper():
        for i, n in enumerate(arr):
            arr[i] *= 2

        nonlocal val
        val *= 2

    helper()
    print(arr, val)


class MyClass:
    # constructor
    def __init__(self, nums):
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size

    def doubleNums(self):
        for i in range(self.size):
            self.nums[i] *= 2


if __name__ == "__main__":
    print("Hello")
    main()
    print(
        "========================starting functions====================================="
    )
    outer(1, 2)
    double([1, 2, 3], 3)
    myClass = MyClass([5, 6, 7])
    myClass.doubleNums()
    print(myClass.nums)
