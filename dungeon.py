class Dungeon:
    def __init__(self,given_file):
        if type(given_file) is not str:
            raise ValueError('Wrong imput for file')
        self.given_file = given_file

    def create_map(self):
        map_game = []
        with open(self.given_file,'r') as file:
            lines = file.readlines()
        for i in range(0,len(lines)):
            lines[i] = lines[i][:-1] 
        return lines
