def log(message):
    with open("log.txt", "a") as file:
        file.write(message + "\n")