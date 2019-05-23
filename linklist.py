class Empty(Exception):
    ''' A custom exception class representing Empty container exception'''
    pass

class SinglyLinkedList:
    '''A simple linkedlist class representing SinglyLinkedList where multiple
       nodes are connected in sequential mannar each node represents a unique
       object in memory'''
    class _Node:
        '''Light weight class representing node objects in memory'''
        __slot__='_next','_data'
        def __init__(self,data,next):
            self._next=next
            self._data=data
    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def add(self,data):
        '''add elements at the front end of the list'''
        self._head=self._Node(data,self._head)
        self._size +=1
    def traverse(self):
        '''traversing the list'''
        if self.is_empty():
            raise Empty('list is empty')
        else:
            temp=self._head
            while(temp):
                print(temp._data)
                temp=temp._next
class LinkedStack:
    '''stack implementation using SinglyLinkedList'''
    class _Node:
        '''Light weight class representing node objects in memory'''
        __slot__='_next','_data'
        def __init__(self,data,next):
            self._next=next
            self._data=data
    def __init__(self):
        self._head=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def push(self,element):
        '''push element at the top of the stack'''
        self._head=self._Node(element,self._head)
        self._size +=1
    def top(self):
        '''return the top element of the stack without deleting
           raise  empty exception if stack is empty'''
        if self.is_empty():
            raise Empty('stack is empty')
        else:
            return self._head._data
    def pop(self):
        '''remove the top element from the stack
           raise empty exception if stack is empty'''
        if self.is_empty():
            raise Empty('stack is empty')
        else:
            result= self._head._data
            self._head=self._head._next
            self._size -=1
            return result
class LiknedQueue:
    ''' queue implementation using linkedlist'''
    class _Node:
        '''Light weight class representing node objects in memory'''
        __slot__='_next','_data'
        def __init__(self,data,next):
            self._next=next
            self._data=data
    def __init__(self):
        self._head=None
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        '''return the first element of the queue but does not remove it'''
        if self.is_empty():
            raise Empty("queue is empty")
        return self._head._data
    def enqueue(self,element):
        ''' add an element in the queue at rare end'''
        newNode=_Node(element,None):
        if self._head is None:
            self._head=newNode
            size +=1
        else:
            self._tail._next=newNode
            self._tail=newNode
            size +=1
     def dequeue(self):
         ''' remove and return the elemnt at the front end of the list
             raise empty exception if queue is empty'''
         if self.is_empty():
             raise Empty('queue is empty')
        else:
            result=self._head._data
            self._head=self._head._next
            size -=1
            if self.is_empty():
                self._tail=None
            return result

class CircularQueue:
    '''class repesenting a circular queue using linkedlist'''
    class _Node:
        '''Light weight class representing node objects in memory'''
        __slot__='_next','_data'
        def __init__(self,data,next):
            self._next=next
            self._data=data
    def __init__(self):
        self._tail=None
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def first(self):
        '''return first element of the queue without removing it'''
        if self.is_empty(self):
            raise Empty('queue is empty')
        firstElement=self._tail._next
        return firstElement._data
    def dequeue(self):
        '''return and remove first element of the queue'''
        if self.is_empty():
            raise Empty('queue is empty')
        head=self._tail._next
        if self._size==1:
            self._tail=None
        else:
            self._tail._next=head._next
            self._size -=1
        return head
    def enqueue(self):
        ''' add an elemnt at the end of queue'''
        newNode=self._Node(data,None)
        if self.is_empty(self):
            newNode._next=newNode
            self._size +=1
        else:
            newNode._next=self._tail._next
            self._tail._next=newNode
        self._tail=newNode
        size +=1
    def rotate(self):
        if self._size >0:
            self._tail=self._tail._next

class  _DoublyLinkedListBase:
    ''' base class representating doubly linked list '''
    def _Node:
        __slot__='_data','_next','_previous'
        def __init__(self,data,next,previous):
            self._data=data
            self._next=next
            self._previous=previous
    def __init__(self):
        self._frontEnd=self._Node(None,None,None)
        self._rareEnd=self._Node(None,None,None)
        self._frontEnd._next=self._rareEnd
        self._rareEnd._previous=self._frontEnd
        self._size=0
    def __len__(self):
        return self._size
    def is_empty(self):
        return self._size==0
    def _insertBetween(self,data,predecessor,successor):
        newNode=self._Node(data,predecessor,successor)
        predecessor._next=newNode
        successor._previous=newNode
        size +=1
        return newNode
    def _deleteNode(self,node):
        predecessor=node._previous
        successor=node._next
        predecessor._next=successor
        successor._previous=predecessor
        element=node._data
        node._previous=Node._next=node._data=None
        size -=1
        return element
''' double ended queue  using linkedlist'''
class Deque(_DoublyLinkedListBase):
    def firstElement(self):
        if self.is_empty():
            raise Empty('deque is empty')
            return self._frontEnd._next._data
    def lastElement(self):
        if self.is_empty():
            raise Empty('deque is empty')
        return self._rareEnd._previous._data
    def addFirst(self,data):
        ''' add element at the front end of the deque'''
        self._insertBetween(data,self._frontEnd,self._frontEnd._next)
    def deleteFirst(self):
        ''' delete a node from the deque and return node data''''
        if self.is_empty():
            raise Empty('deque is empty')
        return self._deleteNode(self._frontEnd._next)
    def deleteLast(self):
        if self.is_empty():
            raise Empty('deque is empty')
        return self._deleteNode(self._rareEnd._previous)










if __name__=='__main__':
    list=SinglyLinkedList()
    list.add(10)
    list.add(20)
    list.add(30)
    list.traverse()
