import os
import json
import sys
import argparse

def create_solution_file_content(problem_name):
    """Generates the content for the Python solution file."""
    return f'''
def {problem_name}(*args):
    """
    TODO: Write your solution logic here.

    You can change the function signature to accept specific arguments.
    For example, for a problem that takes a list and a number, you could change it to:
    def {problem_name}(my_list, my_number):

    The test runner will automatically pass the arguments from the JSON file.
    The function name ('{problem_name}') must remain the same.
    """
    # Example of how to access args if you keep the `*args` signature:
    # arg1 = args[0]
    # arg2 = args[1]
    # ...
    
    # Replace this with your actual solution
    return None
'''.strip()

def create_json_template_content():
    """Generates the content for the JSON test file template."""
    template = [
        {
            "description": "Example Test Case 1: Single list input",
            "input": [
                [1, 2, 3, 4, 5]
            ],
            "expected": "some_value",
            "actual": None
        },
        {
            "description": "Example Test Case 2: Multiple inputs (e.g., a string and a number)",
            "input": [
                "hello",
                2
            ],
            "expected": "some_other_value",
            "actual": None
        }
    ]
    return json.dumps(template, indent=4)

def main():
    """Main function to drive the script."""
    parser = argparse.ArgumentParser(
        description="Create a categorized Python coding problem setup.",
        epilog="Example: python setup_problem.py Recursion reverse_array"
    )
    parser.add_argument(
        "category",
        type=str,
        help="The category of the problem (e.g., 'Recursion', 'Arrays')."
    )
    parser.add_argument(
        "problem_name",
        type=str,
        help="The name of the problem in snake_case (e.g., 'reverse_array')."
    )
    args = parser.parse_args()
    category = args.category
    problem_name = args.problem_name

    # --- Define Directory Structure ---
    category_dir = category
    problems_dir = os.path.join(category_dir, "Problems")
    test_cases_dir = os.path.join(category_dir, "Test_Cases")

    try:
        os.makedirs(problems_dir, exist_ok=True)
        os.makedirs(test_cases_dir, exist_ok=True)
        # Create __init__.py files to make directories importable packages
        with open(os.path.join(category_dir, "__init__.py"), 'w') as f: pass
        with open(os.path.join(problems_dir, "__init__.py"), 'w') as f: pass
        print(f"📁 Category '{category_dir}/' and its subdirectories are ready.")
    except OSError as e:
        print(f"❌ Error creating directories: {e}")
        sys.exit(1)

    # --- File Paths ---
    solution_file_path = os.path.join(problems_dir, f"{problem_name}.py")
    json_file_path = os.path.join(test_cases_dir, f"{problem_name}_tests.json")

    # --- Create Files ---
    if os.path.exists(solution_file_path) or os.path.exists(json_file_path):
        print(f"⚠️  Warning: Files for '{problem_name}' in category '{category}' may already exist. Aborting.")
        sys.exit(0)

    try:
        with open(solution_file_path, 'w', encoding='utf-8') as f:
            f.write(create_solution_file_content(problem_name))
        print(f"📄 Solution file created at: {solution_file_path}")

        with open(json_file_path, 'w', encoding='utf-8') as f:
            f.write(create_json_template_content())
        print(f"🧪 JSON test template created at: {json_file_path}")

    except IOError as e:
        print(f"❌ Error writing file: {e}")
        sys.exit(1)

    print("\n✨ Setup complete! ✨")
    print("Next steps:")
    print(f"1. Open '{json_file_path}' and define your test cases.")
    print(f"2. Open '{solution_file_path}' and write your solution logic.")
    print(f"3. Run 'python test_runner.py {category} {problem_name}' to test your code.")

if __name__ == "__main__":
    main()
