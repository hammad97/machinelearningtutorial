
## Exercise Sheet 3

## Exercise 1: Gradient Descent on Rosenbrock function 

In this part, you are required to optimize theRosenbrock function. This function serves to benchmark all
optimization algorithms alike. The function can be stated mathematically as follows:

f(x,y) = (a−x)^2 +b(y−x^2 )^2 (1)
The function is known to be challenging for optimization. The global minimum is however known to
be at:
(a,a^2 )

where the function value is:
f(x,y) = 0

For the purpose of this exercise, leta= 1andb= 100

1. Implement a 3D plot to visualize the function (Use Matplotlib’s 3D utilities)
2. Derive the partial gradients. (Please look into how to typeset latex in Jupyter notebooks)
3. Convert the function and gradient of this function into equivalent code representation.
4. Optimize the function with Gradient Descent. Set the appropriate hyperparameters like initial valus
    of (x,y) and the steplengthαthrough trial and error.
5. Visualize the trajectory on the same 3D plot. This trajectory should ideally lead to the function
    minimum, starting off with(x= 10,y= 10)for example.


## Exercise 2: Linear Regression with Gradient Descent

### Part A: (Datasets)

Airfare and demand: target−>price
Wine Quality: target−>quality
Parkisons Dataset: target−>total_UPDRS

```
You are required to pre-process the datasets by following these steps:
```
1. Convert any non-numeric values to numeric values. For example you can replace a country name
    with an integer value or more appropriately use hot-one encoding. [Hint: use pandas.get_dummies].
    Please explain your solution.
2. If required drop out the rows with missing values or NA. In next lectures we will handle sparse data,
    which will allow us to use records with missing values.
3. Split the dataset into 80% Train set and 20% Test set.
4. Are there any columns that can be dropped? if so, which ones are why.

### Part B: Linear Regression with Real-World Data 

In this part you are required to implement linear regression algorithm with gradient descent al-
gorithm. Reference lecture https://www.ismll.uni-hildesheim.de/lehre/ml-20w/
script/ml-02-A1-linear-regression.pdf
For each dataset given above:

- 1. A set of training dataDtrain={(x(1),y(1)),(x(2),y(2)),...,(x(N),y(N))}, wherex∈RM,y∈
    R,whereNis number of training examples andMis number of features
- Linear Regression model is given asˆyn=

#### PM

```
m=1βmx
```
```
n
m
```
- Least square loss function is given asl(x,y) =

#### PN

```
n=1(y
n−yˆn) 2
```
- Minimize the loss functionl(x,y)using Gradient Descent algorithm. Implement (learn-linregGD
    and minimize-GD algorithms given in the lecture slides). Chooseimaxbetween 100 to 1000. Explain
    your choice [hint: the following plots might be useful in your choice.]
- You can choose three suitable values of step lengthα > 0. For each value of step length perform the
    learning and record
       - In each iteration of the minimize-GD algorithm calculate|f(xi− 1 )−f(xi)|and (whenimaxis
          reached), plot it against iteration number i. Explain the graph.
       - In each iteration step also calculate RMSE on test setRMSE=

```
qPT
q=1(y
qtest−yˆq) 2
T and plot
it against iteration number i. Explain the graph.
```
## Exercise 3: Steplength Control for Gradient Descent (2+2+3)

This task is based on the Gradient Descent algorithm above. You have to implement the following step-
length controlling algorithms:

1. steplength-backtrackingas given in lecture slides
2. steplength-bolddriveras given in lecture slides

#### 2


3. Look-ahead optimizerplease refer to publication here: https://arxiv.org/pdf/1907.
    08610.pdf

For each step length algorithm and for each dataset in Exercise 2:

- In each iteration of the minimize-GD algorithm calculate|f(xi− 1 )−f(xi)|and plot it against itera-
    tion number i. Explain the graph.
- In each iteration step also calculate RMSE on test setRMSE=

```
qPT
q=1(y
q
test−ˆyq)^2
T , plot it against
iteration number i. Explain the graph.
```
Declare a winning step-length controller based on the metric RMSE. You should tune the associated
hyperparameters of the step-length controller(s).



