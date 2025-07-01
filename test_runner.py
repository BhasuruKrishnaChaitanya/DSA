import os
import json
import sys
import argparse
import importlib

def run_tests(category, problem_name):
    """Dynamically imports a solution function and runs its corresponding tests."""
    all_passed = True
    test_cases = []

    # --- Define paths based on the category and problem name ---
    problems_dir = "Problems"
    test_cases_dir = "Test_Cases"
    
    # Path to the test JSON file (e.g., Recursion/Test_Cases/reverse_array_tests.json)
    test_file_path = os.path.join(category, test_cases_dir, f"{problem_name}_tests.json")
    
    # Module path for dynamic import (e.g., "Recursion.Problems.reverse_array")
    module_path = f"{category}.{problems_dir}.{problem_name}"

    # --- Dynamically import the solution function ---
    try:
        solution_module = importlib.import_module(module_path)
        solution_function = getattr(solution_module, problem_name)
    except ImportError as e:
        print(f"❌ Error: Could not import module at '{module_path}'. Check file and folder names. Details: {e}")
        sys.exit(1)
    except AttributeError:
        print(f"❌ Error: Could not find function '{problem_name}' in '{problem_name}.py'.")
        sys.exit(1)

    # --- Load Test Cases ---
    try:
        with open(test_file_path, 'r', encoding='utf-8') as f:
            test_cases = json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: Test file not found at {test_file_path}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ Error: Could not decode JSON from {test_file_path}. Check for syntax errors.")
        sys.exit(1)

    print(f"--- Running tests for '{category}/{problem_name}' ---")
    
    for i, test in enumerate(test_cases):
        if 'input' not in test or 'expected' not in test:
            print(f"⚠️  Warning: Skipping Test Case #{i+1} due to missing 'input' or 'expected' keys.")
            continue

        input_data = test['input']
        expected_output = test['expected']
        description = test.get('description', f'Test Case #{i+1}')

        print(f"▶️  Running: {description}")

        try:
            actual_output = solution_function(*input_data)
            test['actual'] = actual_output

            if actual_output == expected_output:
                print(f"✅ PASSED")
            else:
                all_passed = False
                print(f"❌ FAILED")
                print(f"   - Input:    {json.dumps(input_data)}")
                print(f"   - Expected: {json.dumps(expected_output)}")
                print(f"   - Got:      {json.dumps(actual_output)}")
        
        except Exception as e:
            all_passed = False
            print(f"💥 ERROR")
            print(f"   - An exception occurred: {e}")
            test['actual'] = f"Error: {e}"
        
        print("-" * 40)

    # --- Write results back and print summary ---
    try:
        with open(test_file_path, 'w', encoding='utf-8') as f:
            json.dump(test_cases, f, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"❌ Error: Could not write results back to test file: {e}")

    print("--- Test Summary ---")
    if all_passed:
        print("🎉🚀 All test cases passed! Great job! 🚀🎉")
    else:
        print("🔥 Some tests failed. Review the output and keep trying! 🔥")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A universal test runner for categorized Python coding problems.",
        epilog="Example: python test_runner.py Recursion reverse_array"
    )
    parser.add_argument("category", type=str, help="The category of the problem.")
    parser.add_argument("problem_name", type=str, help="The name of the problem to test.")
    args = parser.parse_args()
    run_tests(args.category, args.problem_name)
