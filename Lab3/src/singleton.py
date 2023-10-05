class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __init__(self):
        if Logger._instance != None:
            print("logger already created")
        else:
            Logger._instance = self
            print("Logger created exactly once")
            self.messages = []

    def add_message(self, message):
        self.messages.append(message)
    
    def create_instance():
        if Logger._instance == None:
            Logger._instance = Logger()
        return Logger._instance
    


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        # logger = Logger()
        # The reason I comment out this is becoz Logger() does not create any instance,
        # since everytime the Logger() init start from None but there is no return function
        # to create this instance
        logger = Logger.create_instance()
        logger.add_message(f"Adding message number: {i}")
    print(logger.messages)


if __name__ == "__main__":
    main()
