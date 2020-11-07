class bf:
    def __init__(self):
        self.current_data_point = 32766
        self.hm = {self.current_data_point: 0}

    def bfeval(self, statement):
        for operation in [
            operation
            for operation in list(map(str, statement))
            if operation in [">", "<", "+", "-", ".", ",", "["]
        ]:
            self.current_data_point = int(self.current_data_point)
            switch_case = {
                ">": self.incrementdp,
                "<": self.decrementdp,
                "+": self.incrementbyte,
                "-": self.decrementbyte,
                ".": self.output,
                ",": self.input,
                "[": self.whilestart,
            }
            switch_case[operation]()

    def incrementdp(self):
        self.current_data_point = int(self.current_data_point)
        self.current_data_point += 1
        try:
            self.hm[self.current_data_point]
        except KeyError:
            self.hm[self.current_data_point] = 0

    def decrementdp(self):
        self.current_data_point = int(self.current_data_point)
        self.current_data_point -= 1
        try:
            self.hm[self.current_data_point]
        except KeyError:
            self.hm[self.current_data_point] = 0

    def incrementbyte(self):
        self.hm[self.current_data_point] = self.hm[self.current_data_point] + 1

    def decrementbyte(self):
        self.hm[self.current_data_point] = self.hm[self.current_data_point] - 1

    def output(self):
        print("bf> {}".format(self.hm[self.current_data_point]))

    def input(self):
        self.hm[self.current_data_point] = int(input("bf<<< "))

    def whilestart(self):
        try:
            self.hm[self.current_data_point]
        except TypeError:
            self.hm[self.current_data_point] = 0
        result = ""
        while "]" not in map(str, result):
            result += input("bf<< ")
        buffer = result.split("]")
        commands = buffer[0]
        while self.hm[self.current_data_point]:
            self.bfeval(commands)


bf_runtime = bf()
while True:
    bf_runtime.bfeval(input("bf< "))
