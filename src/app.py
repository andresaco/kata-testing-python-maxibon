import random
import time

class Developer:

    def __init__(self, name, maxibonCount):
        """
        Constructor
        """
        self.__name = name
        self.__maxibon = max(0, maxibonCount)

    def pick_maxibon(self, fridge):
        """
        Get some maxibons from the fridge
        """
        if fridge.pick(self.__maxibon) <= 2:
            print("Hi guys, I'm  %s. We need more maxibons!" % self.__name)
            fridge.refill()
        return fridge.remaining()

    def maxibon_requests(self):
        """
        Get the number of maxibon this developer requests each time he visits the kitchen
        """
        return self.__maxibon

class Kitchen:
    """
    Kitchen models the number of remaining maxibons there are
    """

    def __init__(self):
        self.__maxibonCount = 10

    def pick(self, count):
        self.__maxibonCount = self.__maxibonCount - count
        return self.__maxibonCount

    def refill(self):
        self.__maxibonCount = 10

    def remaining(self):
        """
        Get the remaining maxibons
        """
        return self.__maxibonCount

class Headquarter:
    """
    BreakTime models how developers visit the kitchen
    """

    def __init__(self, team):
        """
        Constructor
        """
        self.__developers = team
        self.__fridge = Kitchen()

    def whos_in_for_a_maxibon(self):
        """
        Get a list of developers who are visiting the kitchen
        """
        return random.sample(self.__developers, random.randint(0, len(self.__developers)))

    def maxibon_time(self):
        """
        Perform a Maxibon time
        """
        for d in self.whos_in_for_a_maxibon():
            d.pickMaxibon(self.__fridge)

if __name__== "__main__":
    """
    App. entrypoint
    """

    team = [Developer("Pedro", 3),
            Developer("Davide" , 0),
            Developer("Alberto", 1),
            Developer("Jorge", 1),
            Developer("Jorge", 2),
            Developer("Sergio", 1)]

    hq = Headquarter(team)

    while True:
        hq.maxibon_time()
        time.sleep(5)