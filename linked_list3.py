class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_begining(self,data):      #insertion in linked list from end     
        node=Node(data,self.head)
        self.head=node   

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

    def insert_element(self,index,data):                 #inser value in the ll at give index 
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")
        if index==0:
             self.insert_at_begining(data)
             return

        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break

            itr=itr.next
            count+=1
             
    def remove_element(self,index):                      #remove element of given index
        if index<0 or index>=self.get_length():
            raise Exception("Invalid index")

        if index==0:
            self.head=self.head.next
            return    
        
        count=0
        itr=self.head
        while itr:
            if count == index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

if __name__=='__main__':
    ll=LinkedList()
    
    ll.insertValues(["banana","Mango","Grapes","Orange"])
    ll.print() 
    print(ll.get_length())  
    ll.remove_element(2) #removes element at index 2
    ll.print()        
    print(ll.get_length())
    ll.insert_element(2,"Cheeku")
    ll.print()
    print(ll.get_length())