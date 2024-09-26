from BLL.classes.calculator import Calculator
from DAL.classes.history import History
from BLL.classes.validators import Validators
from GlobalVariables import memory_operations
import GlobalVariables as GlobalVariables

class Console:
    @staticmethod
    def prompt():
        case = input("\n1 - Calculate a number \n"
                     "2 - View history \n"
                     "3 - Additional settings \n"
                     "Your choice: ")
        match case:
            case "1":
                return Console.calculator()
            case "2":
                History.read()
                return False
            case "3":
                Console.settings()
                return False
            case _:
                return True

    @staticmethod
    def calculator():
        num1 = Validators.validate_num("\nEnter first number (or MR / MC): ")

        operator = Validators.validate_operator()
        if operator in memory_operations:
            Validators.validate_memory(operator, num1)
            return False

        num2 = Validators.validate_num("Enter second number (or MR / MC): ")

        if operator == "/" and num2 == 0:
            print("Error: cannot divide by zero")
            return False

        result = Calculator(num1, num2, operator, GlobalVariables.digits)

        print("Result : " + str(result.result))

        try_again = input("\nCalculation has finished successfully! \n"
                          "Current options: \n"
                          "Try again? (Y / N) \n"
                          "Store a value into memory? (MS / M+ / M-) \n"
                          "Your choice: ").lower()
        if try_again in memory_operations:
            Validators.validate_memory(try_again, result.result)
        elif try_again == "y":
            return False
        else:
            return True

    @staticmethod
    def settings():
        settings_prompt = input("\n1 - Change the amount of digits after a decimal point in a number \n"
                                "2 - Clear history\n"
                                "Your choice: ")
        match settings_prompt:
            case "1":
                while True:
                    digits_prompt = input("\nEnter the amount of digits (Current value: " + str(GlobalVariables.digits) + "): ")
                    digits = Validators.validate_digits(digits_prompt)
                    if digits:
                        print("Settings changed successfully\n")
                        break
                    else:
                        print("Invalid input, please enter a valid non-negative integer number")
            case "2":
                History.clear()
                print("History cleared successfully")

            case _:
                print("Invalid input")