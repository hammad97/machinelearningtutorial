
## Exercise Sheet 8

## Exercise 1: Optical Character Recognition via Neural Networks 

The task for this exercise is to develop a Neural Network model that can classify human-written digits into
either of the first 10. We shall be using concepts from the previous exercise sheets such as hyperparameter
optimization and k-cross fold validation as well. Please use the Sklearn library for implementing your
solution. The tasks involve:

1. Loading the MNIST digits dataset via sklearn provided built-in utility function(s).
2. Importing the necessary classes to do k-cross fold validation. You are free to choose k, depend-
    ing upon your computational budget and task complexity but for most purposes ’k=5’ suffices fine.
    Please set aside 20% of the images fortesting.
3. Defining a hyperparameter grid for the ’MLPClassifier’ that is the Neural Network model imple-
    mentation from Sklearn. You need to read the documentation page to find out the hyperparameters
    supported.
4. Defining aRandom Searchprocedure over the ranges you chose above, and then train the model by
    calling the’.fit’method for the search object.
5. Reporting one test accuracy and the best hyperparameters found.


## Exercise 2: End-to-End Self-Driving via Convolutional Neural Networks

For this exercise there are a few background steps that need to be done before jumping to the main tasks.

```
1 Sign up on Kaggle.com and visit the page https://www.kaggle.com/asrsaiteja/
car-steering-angle-predictionto see the dataset for this exercise.
```
```
2 Introduce yourself to the PyTorch library, python library for auto-differentiation and neural network
modeling. The examples page can be accessed here:https://pytorch.org/tutorials/
beginner/pytorch_with_examples.html, and the Linear layers, Convolutional layers,
SGD Optimizer, Backward Gradient Calculation for Loss functions are relevant for the purpose of
this exercise and should be understood.
```
```
3 Resources for understanding ConvNets:
```
```
a.https://www.ismll.uni-hildesheim.de/lehre/dl-20s/script/
dl-05-cnn.pdf
b.https://cs231n.github.io/convolutional-networks/
```
```
2 Create a new notebook on the platform Kaggle.com (there should be button, to create such on the link
from 1.), and once the data is loaded/downloaded to this notebook, follow the code snippet provided
here to read/show images.
```
```
3 Divide these resulting arrays into corresponding train/validation/test splits. Leave the last 10k images
for testing (images are id’ed). You are free to define the length of the validation split.
```
```
4 Implement the Convolutional Neural Network Architecture proposed in the paper titled,"End to End
Learning for Self-Driving Cars". The paper can be accessed here:https://arxiv.org/abs/
1604.
```
```
5 Report one test RMSE for the test set of images.
```


