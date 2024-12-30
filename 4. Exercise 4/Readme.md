

# Exercise Sheet 4
## Exercise 0: Dataset preprocessing 

In this part, you are required to preprocess the given dataset (’tic-tac-toe.data’) according to the steps below:

1. Convert any non-numeric values to numeric values. For example you can replace a country name
    with an integer value or more appropriately use hot-one encoding. [Hint: use hashmap (dict) or
    pandas.get_dummies]. Please explain your solution.
2. This dataset is unbalanced, (show how we can confirm this). Explain what is stratified sampling
    and Implement a stratified sampler.
3. Split the data into a train(80%) and test(20%).

## Exercise 1: Logistic Regression with Gradient Descent 

In this part you are required to implement linear classification with stochastic gradient ascent algorithm.
Reference lectureml-03-A2-linear-classification.pdf

- 1. A set of training dataDtrain={(x(1),y(1)),(x(2),y(2)),...,(x(N),y(N))}, wherex∈RM,y∈
    { 0 , 1 }N is number of training examples and M is number of features


```
Figure 1: Algorithm: Learn-logreg-GA
```
- Logistic Regression model is given asyˆn=σ(βTxn)whereσis a logistic function1+e−^1 βTxn
- Optimize the loglikelihood functionlog(LcondD )using Gradient Ascent algorithm. Implement(learn-
    logreg-GA). Chooseimaxbetween 100 to 1000.
- You will usebolddriveras the step length controller.
    - In each iteration of the algorithm calculate|f(xi− 1 )−f(xi)|and at the end of learning, plot it
       against iteration number i. Explain the graph.
    - In each iteration step also calculate logloss on test set (see ref:https://www.kaggle.
       com/wiki/LogarithmicLoss), plot it against iteration numberi. Explain the graph.

## Exercise 2: Implement Newton Algorithm for Logistic Regression 

In this task you have to implement Newton Algorithm given in Fig. 3. Use the ’tic-tac-toe’ dataset.

- In each iteration of the algorithm calculate|f(xi− 1 )−f(xi)|and at the end of learning, plot it against
    iteration number i. Explain the graph.
- In each iteration step also calculate logloss on test set (see ref above.), plot it against iteration number
Comment on the rate of convergence in the light of plots from above.
