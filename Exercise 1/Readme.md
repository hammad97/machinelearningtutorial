
## Exercise 1: Python Warmup (10 Points)  

### Part A: IPython (2 Points)  
1. Write a **word count program** using IPython (a web version provided by Jupyter Notebook).  
2. The program should:  
   - Read the text document (`random_text.txt`) .  
   - Output the following:  
     - The number of **unique non-stop words**.  
       *Hint:* Use the `nltk` library to retrieve a list of English stop words.  
     - The **top 5 most frequent words**.  

---

### Part B: Numpy (8 Points)  
Implement an **image blurring program** using Numpy matrices.  

#### Task Details:  
1. Install the `matplotlib` library and use it to read and display the image.  
2. Initialize an averaging filter.
3. Pad the image with 1s on all sides.
4. Convolve the filter over the given image. More concretely:
- Select a 3× 3 region of the image. Since images are stored as matrices, you end up with a 3× 3 matrix S. The center element in this matrix Sij needs to be updated with another entry which is calculated as follows:
- Multiply the filter above with this matrix S element-wise and sum the output (Please refrain from utilizing numpy utilities):
- Proceed to convolve this filter over the entire image keeping the stride, s = 1. In summary, every entry(pixel) in the image is now replaced with an average of its 3× 3 neighbors. Padding is necessary to not lose information about the first and last rows/columns.
- Please refer to the website PyImageSearch [(https://bit.ly/3dWll9h) for a more ](https://bit.ly/3dWll9h)detailed description on image convolutions.
5. Plot the original and blurred images side by side.
6. Examine the result of applying the filter multiple times.

## Exercise 2: Linear Regression through exact form (10 Points)

In this exercise you will implement linear regression that was introduced in the introduction lecture of Machine learning. Please refer to the slides on the course webpage.

1. Generate a simple data i.e. a matrix X with dimensions 100× 2. Initialize it with normal distribution µ = 2 and σ = 0.01
2. Generate a simple target vector i.e. a matrix Y with dimensions 100 × 1. Initialize it with random uniform distribution.
3. Implement LEARN-SIMPLE-LINREG algorithm and train it using matrix X to learn values of β0 and β1
4. An important aspect of this algorithm is solve the system of linear equations. Instead of solving the system of linear equations, here we ask you to invert the matrix A = X T X. The task hence involves implementing a subroutine for matrix inversion. Although it must be noted that inverting a matrix should always be avoided but as programming practice here we implement matrix inversion nevertheless.
5. Implement PREDICT-SIMPLE-LINREG and calculate the points for each training example in matrix A.
6. Plot the training points from matrix Y and predicted values in the form of scatter graph.
7. In the end use numpy.linalg lstsq to replace step 2 for learning values of β0 and β1.
