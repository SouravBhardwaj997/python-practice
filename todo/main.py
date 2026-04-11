from add_todo import add_todo
from list_all_todos import list_all_todos
from update_todo import update_todo
from delete_todo import delete_todo
def main():
    while(True):
        print("\n\nTODO APP | Enter the choice number to start")
        print("1. List all todos")
        print("2. Add New Todo")
        print("3. Update Todo")
        print("4. Delete Todo")

        choice=input("Enter your choice: ")
        
        match(choice):
            case "1":
                list_all_todos()
            case "2":
                add_todo()
            case "3":
                update_todo()
            case "4":
                delete_todo()
                
if __name__ == "__main__":
    main()