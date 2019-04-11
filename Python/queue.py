#!/usr/bin/env python                                                           
# -*- coding: latin-1 -*-                                                       
import os, sys

#Implementation of a queue using nodes

class Node():
    def __init__(self, val, next=None): #Constructor
        self.item = val
        self.next = next
        
class Queue():
    def __init__(self): #Constructor, empty list
        self.length = 0
        self.front = None
        self.back = None

    #Add object to the queue
    def enqueue(self,val): 
        if self.length == 0: 
            self.front = self.back = Node(val) 
            self.length = 1 
        else: #om det finns objekt i kön redan
            newNode = Node(val)
            self.back.next = newNode
            self.back = newNode
            self.length += 1 

    #Check if empty list
    def isempty(self): 
        return self.front == None
    
    #Get the object in front of the queue
    def dequeue(self):
        if not self.front: #Empty queue
            print("Nothing in the line")
            return None
        else:
            v = self.front.item 
            self.front = self.front.next
            self.length -= 1
            return v

    #Print the queue in order
    def print(self):
        if not self.front:
            print("Empty queue")
            return None
        else:
            current = self.front
            l = self.length
            while l > 0:
                print(current.item)
                current = current.next
                l -= 1
