"""Program to create & display N records of cricket player and
display Record with Descending order of Run made by players
(Define Class and Methods in Class as per need)
Create a tuple, store the values, and counts the number of occurrences of item from a tuple."""

class Player:

    def __init__(self, runs, name, wickets):
        self.runs = runs
        self.name = name
        self.wickets = wickets

    def __str__(self):
        return f"runs = {self.runs}, name = {self.name}, wickets = {self.wickets}"

    def __lt__(self, other):
        return self.runs < other.runs

    @staticmethod
    def arrange(player_list: list):
        x = 1
        sorted_player_list = sorted(player_list, reverse=True)
        for player in sorted_player_list:
            print(f"{x}. {player}")
            x +=1

class Solution:
    @staticmethod
    def create():
        listx = []
        num = int(input("Enter the len of list "))
        for i in range(num):
            listx.append(input("enter the value: "))

        return tuple(listx)

    @staticmethod
    def count(tuplex):
        dictx = {}
        for i in tuplex:
            if i in dictx:
                dictx[i] = dictx[i] + 1
            else:
                dictx[i] = 1
        return dictx

if __name__ == "__main__":
    a = Player(1234, "Yash", 32)
    c = Player(9876, "Dave", 67)
    d = Player(11231, "Sachin", 100)
    b = Player(2345, "Kawal", 43)

    Player.arrange([a, b, c, d])
    x = Solution.create()
    dictx = Solution.count(x)
    print(dictx)

