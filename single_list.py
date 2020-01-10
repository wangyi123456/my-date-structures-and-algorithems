class Node(object):
        self.next = None
    def __init__(self, elem):
        self.element = elem

class SingleLinkList(object):
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head == None

    def length(self):
        cul = self.head
        account = 0
        while cul != None:
            account += 1
            cul = cul.next
        return account

    def travel(self):
        cul = self.head
        while cul != None:
            print(cul.element,end=' ')
            cul = cul.next

    def append(self, item):
        node = Node(item)
        cul = self.head
        if self.is_empty():
            self.head = node
        else:
            while cul.next != None:
                cul = cul.next
            cul.next = node


    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def insert(self, pos, item):
        node = Node(item)
        count = 1
        cur = self.head
        while count < pos-1:  # 找到插入位置的前一位
            cur = cur.next
            count += 1
        node.next = cur.next
        cur.next = node


    def remove(self,item):
        cur = self.head
        pre = None
        while cur.element != item :
            pre = cur
            cur = cur.next
            if cur == None:
                break     # 若删除尾结点，循环结束前 cur 为空，无法比较，会出错，因此需主动退出循环 #
        if cur == None:
            print("error")
        elif pre == None: # 若删除头结点，需将 head 直接指向cur的next（此时pre未与链表建立联系）#
            self.head = cur.next
        else:
            pre.next = cur.next



    def search (self,item):
        node = Node(item)
        count = 0
        ini = self.head
        while node.element != ini.element:
            count += 1
            ini = ini.next
        return (count)



if __name__ == "__main__":
    li = SingleLinkList()
    print(li.is_empty())
    print(li.length())
    li.append(1)
    li.append(2)
    li.append(3)
    li.append(4)
    li.append(5)
    print(li.is_empty())
    print(li.length())
    li.add(10)
    li.travel()
    print('*******')
   # print (li.search(10))
    #print (li.search(2))
    li.insert(1,3)
    li.travel()