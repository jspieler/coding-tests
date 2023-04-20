# Exercise 3: User Analytics with Plotly Dash and Pandas

Your task is to **analyze the user data** in `data.csv` and to **create a dashboard** using Plotly Dash to visualize the data.
We already provided you some template to start with (`task_user_analytics.py`).


## Before you get started
Create a virtual environment or conda environment using `environment.yaml` or `pip_dependencies.txt` respectively.

## What we expect from you

1. Solve the tasks below.
2. Push your solution to a new branch called `solution-user-analytics`. We encourage you to commit and push your changes regularly as it's a good way for you to showcase your thinking process.
3. Once you're finished, create a new pull request, but please **do not merge it**.

## Time estimate
About **0,5-2 hours** depending on your experience level. But don't worry. There is no countdown. The estimate is for you to plan your time.

## Tasks
Please note: the timestamps have millisecond precision.

### Task 1
Read the data from `data.csv` and visualize them as you consider useful. We recommend you to create more than just one graph.

### Task 2
Add a slider to select a time range to filter and visualize the data according to the selected time range.

### Task 3
Assume that the current day is the same as the most recent one in the data.

Calculate and print following statistics about the data:
1. How many different users visited the application within the last 24 hours?
2. How many different teams visited the application within the last 24 hours?
3. How many different users visited the application within the last 7 days?
4. How many different teams visited the application within the last 7 days?
5. How many different users visited the application within the last 30 days?
6. How many different teams visited the application within the last 30 days?
7. How many different users visited the application within the current year?
8. How many different teams visited the application within the current year?