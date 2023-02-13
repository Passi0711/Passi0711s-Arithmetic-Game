import time
import random as rd
import numpy as np



"""Exception classes"""
class Yes_No_Error(Exception):
    pass

class Name_Error(Exception):
    def __init__(self, message):
        self.message = message


class Player():
    def __init__(self):
        self.amount_of_right_answers = 0
        self.amount_of_time_taken = []
    def data_sheet(self):
        
        """Save data and errors"""
        while True:
            try:
                self.save_data = input("Do you want to save your game stats?(Yes/No)\n")
                if self.save_data == "No":
                    break
                elif self.save_data == "Yes":
                    self.name = input("What is your name?\n") 
                    break
                else:
                    raise Yes_No_Error()
                break
            except Yes_No_Error:
                print("Please type 'Yes' or 'No'")

        """Maximum time and errors"""
        while True:
            try:
                self.available_time = int(input("What is your maximum time for an operation?\n"))
                break   
            except ValueError:
                print("Please type a number")
                
        
        """Name of file and errors"""
        while True:
            try:
                if self.save_data == "Yes":
                    self.file_name = str(input("What do you want to call the file with your game stats?\n"))
                    if self.file_name == "":
                        raise Name_Error("You need to give a name for the file!")
                    elif self.file_name.endswith(".txt"):
                        pass
                    elif not self.file_name.endswith(".txt"):
                        self.file_name = f"{self.file_name}.txt"
                    with open(f"{self.file_name}", "w") as file:
                        file.write(f"Your Name: {self.name}\n"\
                                f"Your maximum time: {self.available_time} seconds\n"\
                                +("_ ")*30)

                elif self.save_data == "No":
                    pass
                break
            except Name_Error as e:
                print(e.message)
    def save_averages(self):
        if self.save_data == "Yes":
            self.amount_of_right_answers = 0
            self.amount_of_time_taken = [] 
        elif self.save_data == "No":
            pass
    def pop_from_list(self):
        new_list = self.amount_of_time_taken.pop()
        return new_list

    def given_time(self):
        self.maximum_time = data_sheet.available_time
        return self.maximum_time



class Numbers():
    def __init__(self):
        self.numbers = np.arange(1,11)

    def number_picker(self):
        self.first_number = np.random.choice(self.numbers)
        self.second_number = np.random.choice(self.numbers)
        return(self.first_number, self.second_number)

class Operation(Numbers):
    def __init__(self, first_number, second_number):
        super().__init__()
        self.first_number = first_number
        self.second_number = second_number
        
    def multiplication(self):
        value = self.first_number * self.second_number
        return value
    def addition(self):
        value = self.first_number + self.second_number
        return value

    def subtraction(self):
        value = self.first_number - self.second_number
        return value

    def division(self):
        value = self.first_number // self.second_number
        return value 

class Game(Operation):
    def __init__(self, first_number, second_number):
        super().__init__(first_number, second_number)
        self.numbers = numbers

    def operation_randomiser(self):
        self.operations = ["multiplication",
                      "division",
                      "addition",
                      "subtraction"]
        self.to_calculate = rd.choice(self.operations)
        
        if self.to_calculate == "multiplication":
            answer = self.multiplication()
            return answer
        elif self.to_calculate == "division":
            answer = self.division()
            return answer
            
        elif self.to_calculate == "addition":
            answer = self.addition()
            return answer

        elif self.to_calculate == "subtraction":
            answer = self.subtraction()
            return answer

    def give_answer(self, player):
        self.time_limit = player.available_time
        reaction = rd.choice(["Correct", "Great", "Keep going", "Let's GOO!"])
        self.correct_answer = self.operation_randomiser()
        to_calculate = self.to_calculate
        initial_time = time.time()
        
        while True:
            elapsed_time = time.time() - initial_time
            if elapsed_time > self.time_limit:
                return "\033[31m\033[1m\033[4mGAME OVER!!!\033[0m You took too much time to answer."
                break


            if to_calculate == "multiplication":
                self.answer = input(f"What's the result of: \033[34m\033[1m\n{self.first_number} * {self.second_number}  =\033[0m  ")
                if int(self.answer) == self.multiplication():
                    self.answer = True
                    print(reaction)
                else:
                    
                    self.answer = False
                break

            if to_calculate == "division":
                self.answer = input(f"What's the result of: \033[34m\033[1m\n{self.first_number} // {self.second_number}  =\033[0m  ")
                if int(self.answer) == self.division():
                    self.answer = True
                    print(reaction)
                else:
                    self.answer = False
                break

            if to_calculate == "addition":
                self.answer = input(f"What's the result of: \033[34m\033[1m\n{self.first_number} + {self.second_number}  =\033[0m  ")
                if int(self.answer) == self.addition():
                    print(reaction)
                    
                else:
                    return False
                break


            if to_calculate == "subtraction":
                self.answer = input(f"What's the result of: \033[34m\033[1m\n{self.first_number} - {self.second_number}  =\033[0m  ")
                if int(self.answer) == self.subtraction():
                    self.answer = True
                    print(reaction)
                    
                else:
                    self.answer =  False
                break


    def start_game(self):
        while True:
            try:
                self.start_game = input("Press ENTER when you are ready to start the game...") 
                if not self.start_game == "":
                    raise Name_Error("")
                else:
                    countdown = [3, 2, 1, "GO!!"]
                    for count in countdown:
                        print(count)
                        if not count == "GO!!":
                            time.sleep(1)
                break
            except Name_Error as e:
                print(e.message)







player = Player()
player.data_sheet()
player.save_averages()
numbers = Numbers()
a,b = numbers.number_picker()
operation = Operation(a,b)
game = Game(a,b)

game.start_game()
game_started = True
while game_started == True:
    initial_time = time.time()
    numbers = Numbers()
    a, b = numbers.number_picker()
    operation = Operation(a,b)
    game = Game(a,b)
    game.operation_randomiser()
    game.give_answer(player)
    elapsed_time = time.time() - initial_time
    player.amount_of_right_answers += 1
    player.amount_of_time_taken.append(elapsed_time)
    if game.answer == False:
        print("\033[31m\033[1m\033[4mGAME OVER!!!\033[0m You gave the wrong answer.")
        game_started = False
        player.pop_from_list()
        player.amount_of_right_answers -= 1
        break
    elif elapsed_time >= player.available_time:
        print("\033[31m\033[1m\033[4mGAME OVER!!!\033[0m You took too much time to answer.")
        player.pop_from_list()
        player.amount_of_right_answers -= 1
        break

if player.save_data == "Yes":
    if not player.amount_of_right_answers == 0:
        with open(f"{player.file_name}", "a") as file:
            file.write(f"\nYou answered {player.amount_of_right_answers} questions right and on time.\n"\
                    f"You answered your questions in {sum(player.amount_of_time_taken)/player.amount_of_right_answers} seconds on average.")
    else:
        with open(f"{player.file_name}","a") as file:
            file.write("You gave no right answers.")
else:
    pass
