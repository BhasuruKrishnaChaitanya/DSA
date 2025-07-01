# Data Structures & Algorithms Practice

This repository is a structured collection of my solutions to various coding problems, organized by topic. It includes a custom testing framework to quickly set up new problems and verify solutions.

## How to Use This Framework

This project contains two main Python scripts to streamline the problem-solving process.

### 1. Setting Up a New Problem

To create the necessary files for a new problem, use the `setup_problem.py` script. It will generate a solution file and a test case template in the correct category folders.

**Command:**
```bash
python setup_problem.py <Category> <problem_name>

Example:

# Creates files for a "two_sum" problem in the "Arrays" category
python setup_problem.py Arrays two_sum

This will create:

Arrays/Problems/two_sum.py (Your solution file)

Arrays/Test_Cases/two_sum_tests.json (Your test cases)

2. Running Tests
After writing your solution and defining your test cases in the JSON file, you can run the universal test runner to check your work.

Command:

python test_runner.py <Category> <problem_name>

Example:

python test_runner.py Arrays two_sum

The script will execute your solution against the test cases and report whether they passed or failed.

Directory Structure
The project is organized by topic to keep solutions easy to find.

DSA/
├── Arrays/
│   ├── Problems/
│   │   └── two_sum.py
│   └── Test_Cases/
│       └── two_sum_tests.json
├── Recursion/
│   ├── Problems/
│   │   └── n_to_one_backtracking.py
│   └── Test_Cases/
│       └── n_to_one_backtracking_tests.json
├── setup_problem.py
├── test_runner.py
└── README.md
