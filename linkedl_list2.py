class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)    
    def print(self):
        if self.head is None:
            print("Linked List is Emplty ")
            return         

        itr=self.head
        llstr=''

        while itr:
            llstr += str(itr.data) + "-->"
            itr=itr.next
        print(llstr)    

    def insertValues(self,data_list):      #inseting value of list types in linked list
        self.head=None
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):                 #getting length of the linked list
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count

if __name__=='__main__':
    ll=LinkedList()
    
    ll.insertValues(["banana","Mango","Grapes","Orange"])
    ll.print()            
    print(ll.get_length())