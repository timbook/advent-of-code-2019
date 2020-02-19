class IntcodeComputer:
    def __init__(self, data, input_, copy=True):
        self.data = data.copy() if copy else data
        self.input = input_
        self.outputs = []
        self.ptr = 0

    def add_phase(self, phase_setting):
        self.input.appendleft(phase_setting)

    def add_input(self, more_input):
        self.input.extend(more_input)

    def process(self):
        instruction = str(self.data[self.ptr]).rjust(5, "0")
        op = int(instruction[-2:])
        mode1 = int(instruction[2])
        mode2 = int(instruction[1])
        mode3 = int(instruction[0])

        if op in [1, 2, 7, 8]:
            assert mode3 == 0, "Invalid output mode!"

            par1 = self.data[self.ptr + 1]
            par2 = self.data[self.ptr + 2]

            # 0 = Position mode
            # 1 = Immediate mode
            v1 = par1 if mode1 == 1 else self.data[par1]
            v2 = par2 if mode2 == 1 else self.data[par2]

            dest = self.data[self.ptr + 3]

            if op == 1:   # Addition
                self.data[dest] = v1 + v2
            elif op == 2: # Multiplication
                self.data[dest] = v1 * v2
            elif op == 7: # Less than
                self.data[dest] = int(v1 < v2)
            elif op == 8: # Equals
                self.data[dest] = int(v1 == v2)

            self.ptr += 4

        elif op == 3:
            par = self.data[self.ptr + 1]
            self.data[par] = self.input.popleft()
            self.ptr += 2

        elif op == 4:
            par = self.data[self.ptr + 1]
            val = par if mode1 == 1 else self.data[par]
            self.outputs.append(val)
            self.ptr += 2

        elif op in [5, 6]: # Jump if true/Jump if false
            par1 = self.data[self.ptr + 1]
            par2 = self.data[self.ptr + 2]

            # 0 = Position mode
            # 1 = Immediate mode
            val = par1 if mode1 == 1 else self.data[par1]
            dest = par2 if mode2 == 1 else self.data[par2]

            if op == 5:
                self.ptr = dest if val != 0 else (self.ptr + 3)
            elif op == 6:
                self.ptr = dest if val == 0 else (self.ptr + 3)

        elif op == 99:
            return

        else:
            raise ValueError(f"Received invalid opcode: {op}")

        self.process()
