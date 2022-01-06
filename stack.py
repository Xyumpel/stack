class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
     
    def check(self):
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        str = input('Введите комбинацию строк:')
        count = 0
        for i in str:
            if i in brackets.values():
                s.push(i)
                count += 1
            elif i in brackets:
                if s.isEmpty :
                    print('Несбалансировано')
                    break
                elif brackets[i] != s.pop():
                    print('Несбалансировано')
                    break
        if s.isEmpty() == True and count != 0:
            print('Сбалансировано')


s=Stack()
s.check()

    


    
    
