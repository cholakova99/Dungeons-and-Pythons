class Dungeon:
    def __init__(self,given_file):
        if type(given_file) is not str:
            raise ValueError('Wrong imput for file')
        self.given_file = given_file
        self.lines = self.create_map()

    def create_map(self):
        map_game = []
        with open(self.given_file,'r') as file:
            to_be_lines = file.readlines()
        for i in range(0,len(to_be_lines)):
            to_be_lines[i] = to_be_lines[i][:-1]
        if self.correct_form(to_be_lines) is False:
            raise ValueError('Text format cannot be parsed to map')
        return to_be_lines  

    def correct_form(self, to_be_lines):
        first_line_len = len(to_be_lines[0])
        for i in range(1,len(to_be_lines)-1):
            if len(to_be_lines[i]) != first_line_len:
                return False
        return True

    def print_map(self):
        for i in range(0,len(self.lines)):
            print(self.lines[i])
