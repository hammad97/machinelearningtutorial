
## Exercise Sheet 5

## Exercise 1: Backward search for variable selection 

In this part, you are required implement a backward search procedure with regard to the AIC metric covered
in the lecture. The AIC metric is stated for reference as follows:

```
minAIC=− 2 logL+ 2p (1)
```
WhereLis the log-likelihood andpthe number of parameters.

The classification dataset that we would be using is named the Bank marketing dataset where the task
is to predict whether a customer shall subscribe to a ’term deposit’. Hence, a binary classification task.
Please follow the steps below:

```
1 Convert any non-numeric values to numeric values. For example you can replace a country name
with an integer value or more appropriately use hot-one encoding. [Hint: use hashmap (dict) or
pandas.get_dummies]. Please explain your solution.
```
```
2 If required drop out the rows with missing values or NA. (hope) in next lectures we will handle sparse
data, which will allow us to use records with missing values.
```
```
3 Split the data into a train/test splits according to the ratios 80%:20%.
```

```
4 Normalize (Standardize) the data withxi−σμ
```
```
5 Implement logistic regression and mini-batch Gradient Ascent.
```
```
6 Keep the hyperparameters of learning rate and batch size fixed (good guesses) and iteratively do
backward selection keeping track of the AIC metric.
```
```
7 Report the final error on Test set.
```
## Exercise 2: Regularization for Logistic Regression 

In this section you will implementgrid searchwithk-fold cross-validationfor model selection i.e. choosing
best hyperparameters. Additionally, you will extend the logistic regression model from Exercise 1 to
incorporate regularization. The tasks stated descriptively:

1. Pick a range ofα 0 andλdefined on grid. You can choose fixedbatchsize= 50.
2. Implement k-fold cross-validation protocol for grid search. For each combination ofα 0 andλyou
    will perform k-fold cross-validation. Letk= 5in this case.
3. Keep track of mean performance (i.e. Classification Accuracy value) acrossk−foldsfor each set
    of hyperparameters. Plot on the gridα 0 vsλthe Classification Accuracy score for all combinations.
    [Hint: you can use a 3D plot with axes=α 0 ,λ, Acc.]
4. Finally, for the optimal value ofalpha 0 andλ, train your model on complete training data and
    evaluate on Test data. Report one single Accuracy and Log-likelihood for Test data.
5. Plot Train and Validation Accuracy and Log-likelihood metrics perk−folditeration.

## Exercise 3: Implementing Hyperband for Logistic Regression 

In this section you will implement a state-of-the-art Hyperparameter Optimization algorithm for tuning
the hyperparametersα 0 ,λ,stepsize-controllerandbatch_sizefor the logistic regression model above.
Firstly, re-split the dataset into train/validation/test splits according to ratios:70% : 15% : 15%. Secondly
look at the following resources to understand the algorithm. Note these resources also contain descriptive
comparisons to other hyperparameter optimization algorithms and also lists pros and cons for each, but for
the most part, the algorithm simply runs different configurations defined with (α 0 ,λ,stepsize-controller,
batch_size) selected randomly at the very start of a so-called "Successive Halving iteration" and then runs
these in growing "budgets" (epochs) churning out sub-optimal configurations along the way.
However, not even the Hyperparameter Optimizer is free of hyperparameters itself. Hence, you have the
liberty of tuning the associated top-level hyperparametersmaxiter, downsampling rate:ηand the total
trials.
Please take extra care of doing all associated hyperparameter optimization on the validation split and report
the test accuracy once by re-training the model with the best found hyperparameters. Also, make sure to
recheck if you have fixed all seeds to 3116 as highlighted in the instructions at the beginning.

1. Hyperband published @ ICLR:https://openreview.net/pdf?id=ry18Ww5ee
2. Extended version @ JMLR:https://jmlr.org/papers/volume18/16-558/16-558.
    pdf
3. Blog post from author(s):https://homes.cs.washington.edu/~jamieson/hyperband.
    html


