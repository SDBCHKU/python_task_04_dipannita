def add_data(data):
    with open("data.txt", "a") as file:
        file.write(data + "\n")