[![pipeline status](../../../badges/master/pipeline.svg)](../../../-/pipelines)
[![pipeline status](../../../badges/master/coverage.svg)](../../../-/pipelines)

# PCL 2 Exercise 4

## Introduction
In this exercise, you will work with principles from functional programming. Your goal is to pass all tests in `test_ex4.py` by editing `ex4.py`.

## Self-Evaluation
This exercise is **optional** and will not be graded; however, we encourage you to solve these non-mandatory exercises yourself to ensure you stay on track and review the key points of the lectures.

You do not need to submit anything; your progress will be automatically evaluated through the Continuous Integration (CI) pipeline.
Everytime you make changes to your code and push them to GitLab, you can navigate to the **"Build -> Pipelines"** section and see the pipline running. Once the pipeline completes, you can check the pipeline status and coverage report badges in the README file to assess whether your code passes the tests and the code coverage achieved by your tests.

To run your own tests locally, please follow the instructions below using pytest.

## Feedback
If you want to get feedback from us, you can submit your code through Gitlab before **March 26th at 23:59**. Submissions after this deadline will not receive feedback.
* Please start by forking this project, which will create a personal copy of the exercise repository. 
* Add your name and matriculation number to every file you submit. 
* Ensure your account is set up and ready to work with.
* Ensure you add all tutors as 'Reporters' to your project and create a release.
* Refer to the instructions in `OLAT > Material > Tutorial > instructions.pdf` if you're unsure how to submit your work.

### Notes:
* Do not change the module’s directory structure.
* Do not change `test_ex4.py`.


## Task: Practicing what you've learned during the lecture this week.
List comprehensions, generators, higher-order functions... There are many topics to cover, so let's go!

- [ ] `repeat_string()`: Something went wrong in this function. Can you make it right? It's only a minimal change.

- [ ] `remove_long_tokens()`: Careful, using this function leads to side effects. Make sure it's safe to use.

- [ ] `filter_punctuation()`: Use the built-in `filter()` function.

- [ ] `lowercase()`: For this one you have to use `map()`, but it's up to you how you want to implement it.

- [ ] `length_sort()`: Sort the tokens list by length.

- [ ] `uppercase()`: This decorator should return a new function that calls the original function and then uppercases the result. The original function returns a list of strings.

- [ ] `alphabetical_sort()`: This function returns the input list, sorted alphabetically. As it uses the decorator `@uppercase`, you need to implement that first.

- [ ] `Alphabet()`: This class stores a set of characters, ordered alphabetically. Implement the `__iter__()` or `__getitem__()` method to make it iterable.



### Running Tests and Checking Coverage
To verify the correctness of your implementation and assess the coverage of your tests, you can use pytest with coverage. Ensure you have pytest and coverage installed in your Python environment. You can install them using pip:
```
pip install pytest pytest-cov
```
To run pytest with coverage and display lines without coverage, you can run the following command:
```
pytest --cov-report term-missing --cov
```
This command executes your tests and generates a coverage report, highlighting lines of code that are not covered by your tests. Aim for achieving 100% coverage!


