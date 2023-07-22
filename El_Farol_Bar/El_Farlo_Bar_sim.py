import matplotlib.pyplot as plt
import random
import json



## Initial input variables for run simulaion

# This var show total number of our society
number_of_people = 100
# This var shows pleasable attendance in bar
attendance = 60
# This var determine distinct number strategy that each person can have 
number_of_strategy = 5
# This var gives number of execusion of model in simulation
ticks = 10000





# Defined each identities
class strategy:
    def __init__(self, strategyId) -> None:
        self.strategyId:int = strategyId





class person:
    def __init__(self, history, strategy, decision, attendance) -> None:
        self.history:list = history
        self.strategy:strategy = strategy
        self.decision:bool = decision
        self.attendance:int = attendance

    def __getStrategy(self)->int:
        if len(self.history) < self.strategy.strategyId:
            return True
        else:
            last_strategy = self.history[-self.strategy.strategyId:]
            predicted = sum(last_strategy) / len(last_strategy)
            return predicted < self.attendance
            
    def putHistory(self, history:list):
        self.history = history
    
    def appendHistory(self, attendanceCount:int):
        self.history.append(attendanceCount)
    
    def updateHistory(self, index:int, value:int):
        self.history[index] = value

    def takeDecision(self):
        forecastAttendance = self.__getStrategy()
        return forecastAttendance
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)





class bar:
    def __init__(self) -> None:
        self.totalCap:int
        self.members:list[person]





if __name__ == '__main__':

    print(f"""Running simualtion with init parameters \nnumber_of_people\t={number_of_people}\nattendency\t\t={attendance}\nnumber_of_strategy\t={number_of_strategy}\nticks\t\t\t={ticks}""")
    people = []
    result_of_sim = []
    i = 0
    while i < number_of_people:
         borned = person(history=[],
                         strategy= strategy(random.randrange(1,
                                                             number_of_strategy + 1,
                                                             1)),
                         attendance = attendance,
                         decision=True)
         people.append(borned)
         i = i + 1
    
    # Start simulation
    init_tick = ticks

    while init_tick-ticks < init_tick:
        history = []

        attendanceCounter = 0
        tempAttendancePersonIndexes = []

        for j, p in enumerate(people):
            if p.takeDecision():
                attendanceCounter = attendanceCounter + 1
                tempAttendancePersonIndexes.append(j)
            else:
                p.appendHistory(0)
        
        for k in tempAttendancePersonIndexes:
            people[k].appendHistory(attendanceCounter)
        
        result  = len(tempAttendancePersonIndexes)
        result_of_sim.append(result)
        # print(result)
        ticks = ticks - 1
    
    plt.plot(result_of_sim)
    plt.show()
    # for p in people:
    #     print(p.toJSON())



