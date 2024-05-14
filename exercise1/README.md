[![pipeline status](../../../badges/master/pipeline.svg)](../../../-/pipelines)
[![pipeline status](../../../badges/master/coverage.svg)](../../../-/pipelines)

# PCL 2 Exercise 1

## Introduction
This exercise focuses on Test-driven development (TDD) and pytest. You'll be working on a naive sentiment analysis task using a collection of quotes. The goal is to determine the overall sentiment of a quote as more positive or negative by counting the occurrences of positive and negative words it contains. Specifically, you'll practice (1) writing code for given tests, and (2) writing tests for given code using pytest. Please refer to the provided code in `sentiment_analysis.py` and `test_sentiment_analysis.py`.

## Self-Evaluation
This exercise is **optional** and will not be graded; however, we encourage you to solve these non-mandatory exercises yourself to ensure you stay on track and review the key points of the lectures.

You do not need to submit anything; your progress will be automatically evaluated through the Continuous Integration(CI) pipeline.
Everytime you make changes to your code and push them to GitLab, you can navigate to the **"Build -> Pipelines"** section and see the pipline running. Once the pipeline completes, you can check the pipeline status and coverage report badges in the README file to assess whether your code passes the tests and the code coverage achieved by your tests.

To run your own tests locally, please follow the instructions below in Task 2 using pytest.

## Feedback
If you want to get feedback from us, you can submit your code through Gitlab before **March 5th at 23:59**. Submissions after this deadline will not receive feedback.
* Please start by forking this project, which will create a personal copy of the exercise repository. 
* Add your name and matriculation number to every file you submit. 
* Ensure your account is set up and ready to work with.
* Ensure you add all tutors as 'Reporters' to your project and create a release.
* Refer to the instructions in `OLAT > Material > Tutorial > instructions.pdf` if you're unsure how to submit your work.

### Notes:
* Do not change the module’s directory structure and the provided functions.
* Do not change function signatures. The signature is given by the header of the function definition, e.g. ```def x(a: str, b: int) -> List[str]```. 
* Adding comments and docstrings for clarity is always helpful.


## Task 1: Implement the Sentiment Analysis Function
Several functions are already provided in `sentiment_analysis.py`. These functions are responsible for different aspects of the task, including tokenization, stopwords removal, sentiment analysis, and result presentation.

Your first task is to implement the function `analyse_sentiment`, following the structure of the previous functions. This function should compare the tokens in a list with the collections of positive and negative words in the `Sentiment words dataset`. Upon identifying a word as positive or negative, it counts the occurrences of positive and negative words, organizing them into two lists, respectively. You can find the corresponding files in the `sentiment_words` folder and read in them.

The unit tests are already given in `test_sentiment_analysis.py`. Review them closely to help you write your code. Your implementation must pass all tests to be considered successful.


## Task 2: Write Tests for Functions
To make sure your code catches corner cases, writing unit tests is a common practice. Your second task is to write tests for `tokenize(sentences_str: str) -> List[str]` and `remove_stopwords(tokens: List[str]) -> List[str]` functions. Provide three test cases for each function, considering edge cases that need testing rather than adding random tests.

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





## Data Sources
```Good_Reads_Quotes.txt``` is adapted from : https://www.kaggle.com/datasets/khushipitroda/good-reads-quotes-with-3000-rows

```sentiment words```: https://www.kaggle.com/datasets/syhens/sentiment-words
