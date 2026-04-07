class CQueue:

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def appendTail(self, value: int) -> None:
        self.stack_1.append(value)

    def deleteHead(self) -> int:
        if len(self.stack_1) == 0 and len(self.stack_2) == 0:
            return -1

        if len(self.stack_2) == 0:
            while len(self.stack_1):
                self.stack_2.append(self.stack_1.pop(-1))
        return self.stack_2.pop(-1)
