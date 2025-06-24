# todo_list.py
def display_menu():
print("\nWelcome to the To-Do List App")
print("Choose an option:")
print("1. Add Task")
print("2. View Tasks")
print("3. Delete Task")
print("4. Quit")

def add_task(tasks):
task = input("Enter the task you want to add: ").strip()
if task:
tasks.append(task)
print(f"✅ Task '{task}' added successfully.")
else:
print("⚠️ Task cannot be empty.")

def view_tasks(tasks):
if not tasks:
print("⚠️ No tasks to show.")
return
print("\n📝 Your Tasks:")
for i, task in enumerate(tasks, 1):
print(f"{i}. {task}")

def delete_task(tasks):
if not tasks:
print("⚠️ No tasks to delete.")
return
try:
view_tasks(tasks)
task_num = int(input("Enter the number of the task to delete: "))
if 1 <= task_num <= len(tasks):
removed = tasks.pop(task_num - 1)
print(f"🗑️ Task '{removed}' deleted successfully.")
else:
print("❌ Task number does not exist.")
except ValueError:
print("❌ Invalid input. Please enter a number.")

def main():
tasks = []
while True:
display_menu()
choice = input("Enter your choice (1–4): ").strip()
try:
if choice == '1':
add_task(tasks)
elif choice == '2':
view_tasks(tasks)
elif choice == '3':
delete_task(tasks)
elif choice == '4':
print("👋 Goodbye!")
break
else:
print("❌ Invalid choice. Please select 1, 2, 3, or 4.")
except Exception as e:
print(f"⚠️ An error occurred: {e}")
finally:
print("-----------")

if __name__ == "__main__":
main()
