class LineNode(object):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.next = None

class Line(object):
    def __init__(self):
        self.head = LineNode(None, None) #两个参数要有两个None

    def CreatLine(self):
        print('创建方阵人员目录')
        Element = input('姓名，性别 请使用空格隔开：')
        cNode = self.head
        while Element != '#':
            Name = Element.split(' ')[0]#获取多个信息
            Sex = Element.split(' ')[1]
            nNode = LineNode(Name, Sex)
            cNode.next = nNode
            cNode = cNode.next
            Element = input('姓名，性别 请使用空格隔开：')

    def DivideList(self, LineM, LineF):
        a = self.head
        b = LineM.head
        c = LineF.head
        num = 0
        while a.next != None:
            num += 1
            a = a.next
            mid = a
            if num%2 == 1:#注意求余结果
                b.next = mid
                b = b.next
            else:
                c.next = mid
                c = c.next
        b.next = None
        """注意需要将最后的节点置空"""
        c.next = None

    def TravelElement(self):
        cNode = self.head.next
        while cNode.next != None:
            print(cNode.name, end='')
            cNode = cNode.next
        print(cNode.name)

    def PrintLine(self):
        cNode = self.head.next
        if cNode.sex == '男':
            print('男队列:')
            self.TravelElement()
        else:
            print('女队列:', self.TravelElement())

def main():
    LineAll = Line()
    LineM = Line()
    LineF = Line()
    LineAll.CreatLine()
    LineAll.DivideList(LineM, LineF)
    LineM.PrintLine()

if __name__ == '__main__':
    main()



