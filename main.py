from utils import add_data
from logger import log

def main():
    try:
        data = input("Enter something: ")
        add_data(data)
        log("Data added successfully")
        print("Saved successfully!")
    except Exception as e:
        log("Error occurred: " + str(e))
        print("Something went wrong!")

if __name__ == "__main__":
    main()