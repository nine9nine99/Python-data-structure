class StackNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkStack(object):
    def __init__(self):
        self.top = StackNode(None)

    def PushStack(self, data):
        tNode = StackNode(None)
        tNode.data = data
        tNode.next = self.top.next
        self.top.next = tNode

    def CreatStack(self):
        Element = input('输入字符')
        while Element != '#':
            self.PushStack(Element)
            Element = input('输入字符')

    def Is_empty(self):
        if self.top.next == None:
            iTop = True
        else:
            iTop = False
        return iTop

    def PopStack(self):
        if self.Is_empty():
            print('链表为空')
            return
        else:
            tStackNode = StackNode(None)
            tStackNode = self.top.next
            self.top.next = tStackNode.next
            return tStackNode.data

class ReadFile(object):
    def ReadNum(self, filename):
        f = open(filename)
        str = f.read()
        L = str.lower().split() #已经转换为字符组并全为小写
        N = len(L)
        return N #获得字节总数

    def Get_Percentage(self, sameword, totalword):
        percentage = sameword/totalword
        print('回文字符所占百分比为%f' % percentage)

    def plalindrome(self, str):
        ss1 = LinkStack()
        ss2 = LinkStack()
        i = 0
        # 单词从前往后进入一个栈
        while i < len(str):
            ss1.PushStack(str[i])
            i = i + 1

        i -= 1
        # 单词从后往前
        while i < len(str) and i >= 0:
            ss2.PushStack(str[i])
            i -= 1

        # 检查两个栈中的元素是否都一样
        while ss1.Is_empty() != True:
            if ss1.PopStack() != ss2.PopStack():
                return False
            else:
                return True

    def calculate(self,filename):
        i, j = 0, 0
        f = open(filename)
        str = f.read()
        L = str.lower().split()
        n = self.ReadNum(filename) #读取所有数据
        for i in range(n):
            if self.plalindrome(L[i]):
                #print(L[i])
                j += 1
            else:
                continue
        print('共有%d个回文英文字符' % j)
        self.Get_Percentage(j, n)


def main():
    num = ReadFile()
    num.calculate('file.txt')

if __name__ == '__main__':
    main()