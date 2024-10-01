# Mytheresa

## Instructions 

### Clone the Repository: 
- Need to clone the repository that contains the project:
```git clone git@github.com:vityazverev/mytheresa.git```

### Run the Tests: 
- After cloning the repository, navigate into the project directory and run the following command to install the required dependencies and run all the tests: 
```python run_tests.py```
If you're using Python 3 explicitly, use:
```python3 run_tests.py```
- This command will: It install the required dependencies from `requirements.txt` and run all tests.

### Running Tests on a Specific Environment: 
- To run tests on a specific environment (e.g., production, local, staging), use the --env flag with pytest:
```pytest tests/ --env=production```

### Test case4:
- The result of this case will be in the root folder with name
```open_pull_requests.csv```