import GlobalVariables as GlobalVariables
from DAL.classes.history import History


class Validators:
    @staticmethod
    def validate_digits(digits_prompt):
        try:
            digits = int(digits_prompt)
            if digits >= 0:
                GlobalVariables.digits = digits
                return True
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def validate_memory(operation, num):
        match operation:
            case "ms":
                GlobalVariables.memory = num
                print("Memory value stored! Current value: " + str(GlobalVariables.memory))
            case "m+":
                num_sum = GlobalVariables.memory + num
                History.write(str(GlobalVariables.memory), str(num), "+", str(num_sum))
                GlobalVariables.memory += num
                print("Memory value updated and saved into history! Current value: " + str(GlobalVariables.memory))
            case "m-":
                num_diff = GlobalVariables.memory - num
                History.write(str(GlobalVariables.memory), str(num), "-", str(num_diff))
                GlobalVariables.memory -= num
                print("Memory value updated and saved into history! Current value: " + str(GlobalVariables.memory))
            case _:
                print("Error occurred during memory validation")

    @staticmethod
    def validate_num(num_prompt="Enter the number (or MR / MC)"):
        while True:
            value = (input(num_prompt)).lower()

            if value.lower() == "mr":
                recovered_value = round(GlobalVariables.memory)
                print("Recovered value: " + str(recovered_value))
                return round(GlobalVariables.memory, recovered_value)
            elif value.lower() == "mc":
                GlobalVariables.memory = 0.0
                print("Memory cleared!")
            else:
                try:
                    return round(float(value), GlobalVariables.digits)
                except ValueError:
                    print("Please enter a valid number / memory operation")

    @staticmethod
    def validate_operator():
        while True:
            operator = (input("Enter operator (or MS / M+ / M-): ")).lower()
            if operator in GlobalVariables.operands or operator in GlobalVariables.memory_operations:
                return operator
            else:
                print("Please enter a valid operator")