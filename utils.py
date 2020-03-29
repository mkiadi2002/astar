# coding=utf-8
import heapq
from collections import deque
import random
try:
    from itertools import izip
except ImportError:
    izip = zip


class LifoList(deque):
    '''List that pops from the end.'''

    def sorted(self):
        return list(self)[::-1]


class FifoList(deque):
    '''List that pops from the beginning.'''
    def pop(self):
        return super(FifoList, self).popleft()

    def sorted(self):
        return list(self)


class BoundedPriorityQueue(object): # Heaps are lists for which heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2] for all k, counting elements from zero. 
    def __init__(self, limit=None, *args):
        self.limit = limit
        self.queue = list() # This is where the list is created 

    def __getitem__(self, val):
        return self.queue[val]

    def __len__(self):
        return len(self.queue)

    def append(self, x): # this method is called from the traditional
        print (f"||From utils.append() method: we push the {x} to OPEN list in the queue now||")
        print ("")
        heapq.heappush(self.queue, x)  #Push the value item onto the heap, maintaining the heap invariant. Maybe the __lt__ functon is called now?
        print ("This is the OPEN list in the utils:")
        print (*self.queue)
        print ("")
        if self.limit and len(self.queue) > self.limit:
            self.queue.remove(heapq.nlargest(1, self.queue)[0])

    def pop(self):
        print ("")
        print (f"||From utils.pop() method: we pop() {self.queue[0]} from the queue now. Returns the node to traditional.||")
        print ("")
        #print (*self.queue)  
        return heapq.heappop(self.queue)#Pop and return the smallest item from the heap, maintaining the heap invariant.

    def extend(self, iterable):
        for x in iterable:
            self.append(x)

    def clear(self):
        for x in self:
            self.queue.remove(x)

    def remove(self, x):
        self.queue.remove(x)

    def sorted(self):
        return heapq.nsmallest(len(self.queue), self.queue)


class InverseTransformSampler(object):
    def __init__(self, weights, objects):
        assert weights and objects and len(weights) == len(objects)
        self.objects = objects
        tot = float(sum(weights))
        if tot == 0:
            tot = len(weights)
            weights = [1 for x in weights]
        accumulated = 0
        self.probs = []
        for w, x in izip(weights, objects):
            p = w / tot
            accumulated += p
            self.probs.append(accumulated)

    def sample(self):
        target = random.random()
        i = 0
        while i + 1 != len(self.probs) and target > self.probs[i]:
            i += 1
        return self.objects[i]


def _generic_arg(iterable, function, better_function):
    values = [function(x) for x in iterable]
    better_value = better_function(values)
    candidates = [x for x, value in zip(iterable, values) if value == better_value]
    return random.choice(candidates)


def argmin(iterable, function):
    return _generic_arg(iterable, function, min)


def argmax(iterable, function):
    return _generic_arg(iterable, function, max)