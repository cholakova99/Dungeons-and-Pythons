allowed_symbols_for_map = ["#","S","T","E",".","G"]
class Dungeon:
    def __init__(self,given_file):
        if type(given_file) is not str:
            raise ValueError('Wrong imput for file')
        self.given_file = given_file
        self.lines = self.create_map()
        self.rows = len(self.lines)
        self.columns = len(self.lines[0])
        self.row_pos = 0
        self.col_pos = 0

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
            for j in range(first_line_len):
                if to_be_lines[i][j] not in allowed_symbols_for_map:
                    return False
        return True

    def print_map(self):
        for i in range(0,len(self.lines)):
            print(self.lines[i])

    def move_hero(self,direction):
        if direction == "up":
            if self.row_pos <= 0:
                return False
            if self.check_next_step(self.row_pos-1,self.col_pos) == "path" or self.check_next_step(row_pos-1,col_pos) == "starting":
                self.row_pos -= 1
            elif self.check_next_step(self.row_pos-1,self.col_pos) == "enemy":
                pass #BAAATTTLEE
            elif self.check_next_step(self.row_pos-1,self.col_pos) == "gateway":
                pass #we will see
            elif self.check_next_step(self.row_pos-1,self.col_pos) == "treasure":
                pass #we will see
            else:
                return False

        elif direction =="down":
            if self.row_pos >= self.rows - 1:
                return False
            if self.check_next_step(self.row_pos+1,self.col_pos) == "path" or self.check_next_step(self.row_pos+1,self.col_pos) == "starting":
                self.row_pos +=1
            elif self.check_next_step(self.row_pos+1,self.col_pos) == "enemy":
                pass #BAAATTTLEE
            elif self.check_next_step(self.row_pos+1,self.col_pos) == "gateway":
                pass #we will see
            elif self.check_next_step(self.row_pos+1,self.col_pos) == "treasure":
                pass #we will see
            else:
                return False

        elif direction == "left":
            if self.col_pos <= 0:
                return False
            if self.check_next_step(self.row_pos,self.col_pos-1) == "path" or self.check_next_step(self.row_pos,self.col_pos-1) == "starting":
                self.col_pos -= 1
            elif self.check_next_step(self.row_pos,self.col_pos-1) == "enemy":
                pass #BAAATTTLEE
            elif self.check_next_step(self.row_pos,self.col_pos-1) == "gateway":
                pass #we will see
            elif self.check_next_step(self.row_pos,self.col_pos-1) == "treasure":
                pass #we will see
            else:
                return False

        elif direction == "right":
            if self.col_pos >= self.columns - 1:
                return False
            if self.check_next_step(self.row_pos,self.col_pos+1) == "path" or self.check_next_step(self.row_pos,self.col_pos+1) == "starting":
                self.col_pos +=1
            elif self.check_next_step(self.row_pos,self.col_pos+1) == "enemy":
                pass #BAAATTTLEE
            elif self.check_next_step(self.row_pos,self.col_pos+1) == "gateway":
                pass #we will see
            elif self.check_next_step(self.row_pos,self.col_pos+1) == "treasure":
                pass #we will see
            else:
                return False
        else:
            return "Wrong direction"


    def check_next_step(self,row_index,col_index,):
        if self.lines[row_index][col_index] == "G":
            return "gateway"
        elif self.lines[row_index][col_index] == "E":
            return "enemy"
        elif self.lines[row_index][col_indx] == "#":
            return "obstacle"
        elif self.lines[row_index][col_index] == ".":
            return "path"
        elif self.lines[row_index][col_index] == "T":
            return "treasure"
        else:
            return "starting"
