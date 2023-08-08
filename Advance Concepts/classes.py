
# blueprint for an object --> variables and methods --> can be adopted by a class of objects with similar behaviour
class Player1:
    
    # default constructor with static values
    def __init__(self) -> None:
        print("Default constructor called!!")
        self.name = "Messi"
        self.club = "Inter Miami"
        self.height = 152
    
    # to delete the created object 
    def __del__(self) -> None:
        print("object deleted for default constructor") 
    
    # non-paramaterized function
    def helloWorld(self):
        print("Hello World to you {}".format(self.name))
        
class Player2:    
    
    # paramtertized con structor
    def __init__(self, name, club, height) -> None:
        print("Parameterized constructor called")
        self.name = name
        self.height = height
        self.club = club
        
    def __del__(self) -> None:
        print("object deleted for paramterized constructor") 
        
    # default method for string print calls.
    def __str__(self) -> str:
        return ("Name: {}, Club : {}, Height: {}".format(self.name, self.club, self.height))

    
    def height_increase(self, height):
        
        if self.height < 170:
            self.height += 10
        else:
            self.height = height
            self.height -= 10
        # return self.height

# Child Class to inherit the Player2 class        
class AcadPlayer(Player2):
    
    # Parameterized constructor to inherit the Parent Class - Player2
    def __init__(self, name, club, height, academy) -> None:
        super().__init__(name, club, height) # Super keyword to inherit the methods and properties from parent class
        
        # adding additonal child class properties
        self.academy = academy
    
    
    # default method for string print calls.
    def __str__(self) -> str:
        # str function local to this class
        # return ("Name: {}, Club : {}, Height: {}, Academy: {}".format(self.name, self.club, self.height, self.academy))

        # overwriting the parent class funtion to add more properties
        text = super().__str__()
        text += ", Academy : {}".format(self.academy)
        return text
        
    
def main():
    
    # dafault constructor object creation
    player1 = Player1()
    # obj attributes access
    print(player1.name, player1.club, player1.height)
    # obj funtion access
    player1.helloWorld()
    
    
    # parameterized constructor oject call with input supplied
    player2 = Player2("Pratty", "Real Madrid", 150)
    # str funtion callled on the object
    print(player2)
    # paramterized funtion called
    player2.height_increase(200)
    print(player2)

    # deleting objs to free space
    del player1
    del player2
    
    
    # defining an object for an inherited class
    acadplayer= AcadPlayer("Pratty", "Chelsea", 123, "Real Madrid")
    print(acadplayer)
    
    # calling an inherited funtion
    acadplayer.height_increase(100)
    print(acadplayer)
    
    # deleting obj to free space
    del acadplayer
     
if __name__ == '__main__':
    main()