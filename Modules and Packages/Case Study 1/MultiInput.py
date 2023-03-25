class MultiInput:
    def __init__(self):
        pass

    def input_data_with_space(self):
        self = list(input("Enter the data").split())
        return self

    def input_data_with_comma(self):
        self = list(input("Enter the data").split(","))
        return self

    def input_data_with_lines(self):
        loop_info = int(input("How many number of line you wish to input:"))

        self = []
        for i in range(loop_info):
            try:
                line = input("Enter your input: ")
            except:
                pass
            self.append(line)
        return self

    def input_data_list(self):
        self = list(input("Please enter your sentence: "))
        return self
