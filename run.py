# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import json  # External library for file handling

# File path to the JSON file in the 'assets' directory
TASKS_FILE = "assets/tasks.json"

# Utility functions
def load_tasks(file_name=TASKS_FILE):
    """Load tasks from the assets directory."""
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Handle empty or invalid data

def save_tasks(file_name=TASKS_FILE, tasks=[]):
    """Save tasks to the assets directory."""
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)

# Test the setup
if __name__ == "__main__":
    # Initialize with an empty task list
    tasks = load_tasks()
    print("Task Manager initialized.")
    print(f"Loaded tasks: {tasks}")
    save_tasks(tasks=tasks)
