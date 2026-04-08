def list_all_todos():
    print("List all todos")

def add_new_todo():
    print("add new todo")

def update_todo():
    print("add new todo")

def delete_todo():
    print("Delete Todo ")

def main():
    while(True):
        print("TODO APP | Enter the choice number to start\n")
        print("1. List all todos")
        print("2. Add New Todo")
        print("3. Update Todo")
        print("4. Delete Todo")

        choice=input("Enter your choice: ")
        
        match(choice):
            case "1":
                list_all_todos()
            case "2":
                add_new_todo()
            case "3":
                update_todo()
            case "4":
                delete_todo()
                
if __name__ == "__main__":
    main()