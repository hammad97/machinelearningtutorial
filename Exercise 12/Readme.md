## Exercise 12

#  Gaussian Processes II 

A. Implement a GP model take can perform regressionwith noise and means(μ,μ∗), (in
python) using the squared exponential kernel (1).
It should be a class with at least 4 functions:

```
init(σf,σy,`): Initialize the model with the given parameters
fit(X,Y): fit the model to the training data
(computeKy=K+σ^2 yIandα=Ky−^1 Y)
predict(X): Compute the prediction( ̃μ∗,Σ ̃∗)
evaluate(X,Y): Compute the empirical lossL=‖Y−Yˆ‖^2
```
B. Perform a GP regression on the data-settutorial2.datprovided via LearnWeb. Use the
parametersσf= 1,σy= 0. 5 ,`= 1. Plot the prediction, including a 2 σuncertainty margin (cf. lecture
slide plots) on the interval[− 3 ,+3].

