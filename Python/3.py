def add_todo(todos):
    item = input("Enter to-do item: ").strip()
    if item:
        todos.append(item)
        save_todos(todos)
        print("To-do item added successfully!")
    else:
        print("Item cannot be empty!")

def save_todos(todos):
    try:
        with open("todos.txt", "w") as f:
            for item in todos:
                f.write(item + "\n")
    except IOError:
        print("Error saving to file!")

def read_todos():
    todos = []
    try:
        with open("todos.txt", "r") as f:
            todos = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("No to-do list found. Starting fresh.")
    except IOError:
        print("Error reading file!")
    return todos

def view_todos(todos):
    if not todos:
        print("No to-do items found.")
        return
    print("\nTo-Do List:")
    for i, item in enumerate(todos, 1):
        print(f"{i}. {item}")

def main():
    todos = read_todos()
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add To-Do Item")
        print("2. View To-Do List")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ").strip()
        
        if choice == '1':
            add_todo(todos)
        elif choice == '2':
            view_todos(todos)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()