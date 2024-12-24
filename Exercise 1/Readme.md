Lab Course Machine Learning

Exercise Sheet 1

Prof. Dr. Dr. Lars Schmidt-Thieme, Shereen Elsayed Information Systems and Machine Learning Lab     University of Hildesheim

November 5th, 2021

Submission on November 12th, 2021 at 12:00 noon, (on learnweb, course code 3116)

Instructions

Please following these instructions for solving and submitting the exercise sheet.

1. You should submit a jupyter notebook detailing your solution or as pdf report + the notebook.
1. Please explain your approach i.e. how you solved a given problem and present your results in form of graphs and tables.
1. Please submit your jupyter notebook to learnweb before the deadline. Please refrain from emailing the solutions except in case of emergencies.
1. Unless explicitly noted, you are not allowed to use scikit, sklearn or any other library for solving any part.
1. Please refrain from plagiarism.

Exercise 1: Python Warmup (10 Points)

Install Anaconda and Jupyter notebooks (latest version; python latest version);[ https://www.anacon da.com/products/individual.](https://www.anaconda.com/products/individual)

Part A: (2 Points): IPython In this task you are required to use IPython (a web version provided by Jupyter nootbook). You have to write a word count program. Your program should read the provided text document on learnweb named "random\_text.txt" and then output the following stats:

- the number of unique Non-stop words. hint\* you can use "nltk" library to get a list of English language stop words.
- the top 5 most frequent words.

Part B: (8 Points): numpy In this exercise, we shall implement an image blurring program using numpy matrices. Numpy is a popular numerical operations library that is widely used in the python machine learning ecosystem. Please familiarize yourself with this library by following the documentation online [numpy.org. The](numpy.org) exact task details include:

1. Install matplotlib library and use the given utilities to read and display the image[ 1.](#_page1_x90.00_y435.93)

2. Initialize an averaging filter as follows:

  1 1 1

F = 1 1 1 1

9 1 1 1

3. Pad the image with 1s on all sides.
3. Convolve the filter over the given image. More concretely:
- Select a 3× 3 region of the image. Since images are stored as matrices, you end up with a 3× 3 matrix S. The center element in this matrix Sij needs to be updated with another entry which is calculated as follows:
- Multiply the filter above with this matrix S element-wise and sum the output (Please refrain from utilizing numpy utilities):

1 11 11 11 224 215 47 



Sij = 9 1 1 1 × 214225 25090 24789 = 177.88

- In the above equation, the second matrix is a subregion from the image. We proceed to replace the original entry in the image Sij = 90 with the newly computed value of 177.88.
- Proceed to convolve this filter over the entire image keeping the stride, s = 1. In summary, every entry(pixel) in the image is now replaced with an average of its 3× 3 neighbors. Padding is necessary to not lose information about the first and last rows/columns.
- Please refer to the website PyImageSearch [(https://bit.ly/3dWll9h) for a more ](https://bit.ly/3dWll9h)detailed description on image convolutions.
5. Plot the original and blurred images side by side.
5. Examine the result of applying the filter multiple times.

<a name="_page1_x90.00_y435.93"></a>Listing 1: Utility functions for images from matplotlib library![](Aspose.Words.4e201132-3a56-460a-b00d-58caccaeb882.001.png)

import matplotlib . image as mpimg

import matplotlib . pyplot as plt

img = mpimg. imread ( ’ lena\_gray . jpg ’ )

plt . imshow(img , cmap=’ gray ’ , vmin=0, vmax=255)![](Aspose.Words.4e201132-3a56-460a-b00d-58caccaeb882.002.png)

Exercise 2: Linear Regression through exact form (10 Points)

In this exercise you will implement linear regression that was introduced in the introduction lecture of Machine learning. Please refer to the slides on the course webpage.

1. Generate a simple data i.e. a matrix X with dimensions 100× 2. Initialize it with normal distribution µ = 2 and σ = 0.01
1. Generate a simple target vector i.e. a matrix Y with dimensions 100 × 1. Initialize it with random uniform distribution.
1. Implement LEARN-SIMPLE-LINREG algorithm and train it using matrix X to learn values of β0 and β1
1. An important aspect of this algorithm is solve the system of linear equations. Instead of solving the system of linear equations, here we ask you to invert the matrix A = X T X. The task hence involves implementing a subroutine for matrix inversion. Although it must be noted that inverting a matrix should always be avoided but as programming practice here we implement matrix inversion nevertheless.

5. Implement PREDICT-SIMPLE-LINREG and calculate the points for each training example in matrix A.
5. Plot the training points from matrix Y and predicted values in the form of scatter graph.
5. In the end use numpy.linalg lstsq to replace step 2 for learning values of β0 and β1.
