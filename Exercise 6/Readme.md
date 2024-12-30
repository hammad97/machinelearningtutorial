# Exercise Sheet 6

## Exercise 0: Dataset Preprocessing 

Datasets

- 1. Regression Datasets
    (a) Generate a Sample dataset called D1 :
    i. Initialize matrixx∈R^100 ×^1 using Uniform distribution withμ= 1andσ= 0. 05
    ii. Generate targety∈R^100 ×^1 usingy= 1. 3 x^2 + 4. 8 x+ 8 +ψ, whereψ∈R^100 ×^1 randomly
    initialized.
    (b) Wine Quality called D2: (use winequality-red.csv)http://archive.ics.uci.edu/ml/ datasets/Wine+Quality

You are required to pre-process given datasets when applicable using instructions communicated earlier.

## Exercise 1: Generalized Linear Models with Scikit Learn 

In previous labs you have implemented various optimization algorithms to solve linear or logistic regression
problem. In this task you are required to use Scikit Learn to experiment with following linear models
and Stochastic Gradient Descent (SGD) [Hint: useSGDRegressor]. You may use scikit learn for this
question.


1. Ordinary Least Squares
2. Ridge Regression
3. LASSO

Following are required in this task

1. Split your data into Train and Test Splits according to the 80%:20% ratio. Use dataset D
2. For each model, pick three sets of hyperparameters and learn each model (without cross validation).
    Measure Train and Test RMSE and plot it on one plot. Explain the plots and relate it to the theory
    studied in lectures i.e. influence of regularized vs non-regularized models. You have to compare the
    following models and argument should explain underfitting and overfitting.
3. Now tune the hyperparameters using scikit learn GridSearchCV and plot the results of cross valida-
    tion for each model. [Hint: use GridSearchCV object methodcv_resultsto see different metrics]
4. Using the optimal hyperparameter you have to evaluate each model on the Test Set. Report the results
    in a meaningful manner.

## Exercise 2: Higher Order Polynomial Regression 

In this task you are required to use dataset D1. So far we have only looked at 1st degree polynomial,
i.e. linear polynomial and your D1 is also generated using linear polynomial. In this task you have to
use higher degrees of polynomial feature for your data i.e. degrees 1, 2, 7, 10, 16 and 100. [Hint: use
sklearn.preprocessing to generate polynomial features]. You may use scikit learn for this question. Your
tasks are:

1. Task A: Prediction with high degree of polynomials

```
a For each newly created dataset learn LinearRegression.
b Plot the predicted curves for each dataset. Explain the phenomena you observed for different
prediction curves.
```
2. Task B: Effect of Regularization

```
a Fixed the degree of polynomial to 10
b Pick Four values ofλ(regularization constant) and learn Ridge Regression [Hint: use Ridge
and yourλvalues should be far a part i.e. 0, 10 −^6 , 10 −^2 , 1].
c Plot the predicted curves for each dataset. Explain the phenomena you observed for different
prediction curves.
```

## Exercise 3: Implementing Coordinate Descent 

So far we have looked at Gradient Descent, Stochastic Gradient Descent(Ascent). This week the main
task is to implement Coordinate Descent that has been covered in the lecture. To make things a bit more
interesting, we will be implementing Lasso Regression along with the Coordinate Descent. You may NOT
use scikit-learn for this question. We will use the Wine Dataset for this question.
Fig. 1 Shows the implementation for the Coordinate Descent along with its minimization.

1. Coordinate Descent.

```
a Implementing the Coordinate Descent algorithm.
b Maintain a history of yourβvalues. After training plot them against iterations [hint: If you
have 10 features, you should have 11βs (one bias, 10 features)]. Plot them all in a singel plot.
This should show you the progression of your feature values as your train the model.
```
2. Coordinate Descent with L1 Regularization

```
a Implement CD with L1 regularization (Fig. 2). Note that the update step is now including the
L1 term.
b Maintain a history of yourβvalues. After training plot them against iterations.
```
3. Task C: Comparison

```
a Compare the plots of the unregularized and regularized CD
b Highlight the difference. What information can be inferred from these values.
```

### 0.1 ANNEX

- Following lecture is relevant this exercise https://www.ismll.uni-hildesheim.de/lehre/ml-20w/script/ml-
    04-A3-regularization.pdf
- sklearn.model_selection, sklearn.metrics, sklearn.linear_model, sklearn.preprocessing
- Scikit Learn User Guide [http://scikit-learn.org/stable/user_guide.html](http://scikit-learn.org/stable/user_guide.html)
- You can use matplotlib for plotting.
- sklearn.metrics [http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics)


