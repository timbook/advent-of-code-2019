class Program:
    def __init__(self, data, noun, verb):
        self.data = data.copy()
        self.data[1] = noun
        self.data[2] = verb
        self.ptr = 0

    def process(self):
        op = self.data[self.ptr]
        v1 = self.data[self.ptr + 1]
        v2 = self.data[self.ptr + 2]
        dest = self.data[self.ptr + 3]

        if op == 1:
            self.data[dest] = self.data[v1] + self.data[v2]
        elif op == 2:
            self.data[dest] = self.data[v1] * self.data[v2]
        elif op == 99:
            return
        else:
            raise ValueError("Program has broken!")

        self.ptr += 4
        self.process()

    def get_output(self):
        return self.data[0]
