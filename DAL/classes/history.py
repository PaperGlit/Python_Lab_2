class History:
    @staticmethod
    def clear():
        with open("Sources/history.txt", "w"):
            pass

    @staticmethod
    def read():
        with open("Sources/history.txt", "r") as file:
            history = file.read()
            if not history:
                print("\nYour history is empty!")
            else:
                print("\nYour history:\n" + history)

    @staticmethod
    def write(num1, num2, operator, result):
        with open("Sources/history.txt", "a") as history_file:
            history_file.write(str(num1) + " " + operator + " " + str(num2) + " = " + str(result) + "\n")