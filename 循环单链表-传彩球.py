import random

class CLNode(object):
    def __init__(self, num, data):
        self.next = None
        self.data = data
        self.num = num

class CSL(object):
#链表初始化
    def __init__(self):
        self.head = CLNode(None, None)

    def CreatCSL(self):
        print('创建循环单链表\n*************')
        Element = input('请输入编号和姓名，用空格隔开:')
        cNode = self.head
        while Element != '#':
            Num = Element.split(' ')[0]
            Data = Element.split(' ')[1]
            nNode = CLNode(Num, Data)
            cNode.next = nNode
            nNode.next = self.head
            cNode = cNode.next
            Element = input('请输入编号和姓名，用空格隔开:')

#遍历部分
    def TravelCSL(self):
        print('开始遍历人员列表')
        #初始化指针
        cNode = self.head
        if cNode.next == None:
            print('链表为空')
            return
        #对整个链表进行遍历
        while cNode.next != self.head:
            print(cNode.next.num, cNode.next.data, end='\n')#注意cNode指针开始的位置
            cNode = cNode.next

#获取链表长度
    def GetLength(self):
        cNode = self.head
        count = 0
        while cNode.next != self.head:
            count += 1
            cNode = cNode.next
        return count

#抽奖部分
    def Lottery(self):
        pNode = self.head
        qNode = self.head.next
        count = self.GetLength()
        total = self.GetLength()
        while count != 1:
            randomNum = random.randint(0, 100)
            print('第%d轮随机数为%d'%(total-count, randomNum))
            transNum = randomNum%count
            #调整位置
            while transNum != 0:
                pNode = pNode.next
                qNode = qNode.next
                transNum -= 1
            #假如循环至头部
            if qNode == self.head:
                qNode = qNode.next
                pNode = pNode.next
            #非头部情况
            print('淘汰人员为', qNode.data)
            pNode.next = qNode.next
            del qNode
            qNode = pNode.next
            count = self.GetLength()
        pNode = self.head.next
        print('************')
        print('获奖者', pNode.data)

def main():
    csl = CSL()
    csl.CreatCSL()
    csl.TravelCSL()
    csl.Lottery()

if __name__ == '__main__':
    main()