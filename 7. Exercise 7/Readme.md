
## Exercise Sheet 7
## Exercise 0: Dataset Preprocessing 

Time Series Classification Datasets
For this exercise sheet we shall be working with the University of California, Riverside’s Time Series
Classification Dataset Repository.

1. There are multiple datasets in this repository, you need to proceed to the page:https://www.
    cs.ucr.edu/~eamonn/time_series_data_2018/and download the archive ( 260MB).
2. Preprocess the datasets in the following way:
    - Merge train and test splits and then re-split into train/validation/test splits according to ratios:
       70%/15%/15%. Please take care that you do stratified splits.
    - If there are any datasets that do not have equal length samples, then pad the samples with 0s on
       the left. (This comes in useful for later distance calculations)
    - Standardize the datasets, by removing the mean and scaling to unit-variance (x−σμ)
    - Ignore multivariate datasets (if any)
3. Plot interesting statistics:
    - A plot indicating the total the length of samples (across all datasets)
    - Similar to above show number of classes and number of samples.


## Exercise 1: Dataset Imputation with KNN 

We have been in the past ignoring missing values from the datasets, but for this lab, we shall try to imple-
ment imputation withK-Nearest Neighbor algorithm. The idea is to replace the missing value in a column
by an average of itsK-Nearest Neighbors whereKacts as a hyperparameter.

1. List the datasets having missing values.
2. For each dataset with missing values, and for each feature (timestep) of it that has missing values
    impute the value by calculating the mean of its nearestKneighbors. You need to tune the hyperpa-
    rameterKvia grid search. If in case there are multiple feature values missing, use the sameKfor all
    during such tuning.
3. Next, train aK-Nearest Neighbour classifier (pseudo-code given in slides) with majority voting and
    euclidean distance to maximize accuracy on the validation split by tuningKvia grid search.
4. Report the final test accuracy for each dataset by using the optimalKfound for imputation and the
    optimalKfound for classification. Please jointly tune the twoKs.

## Exercise 2: Time Series Classification with Various Distance Measures

For this exercise, we shall be looking at various distance measures provided with thescipylibrary. The
idea is to declare a single most optimal distance measure across all time series datasets. The tasks are the
following:

1. For each distance measure on the page:https://docs.scipy.org/doc/scipy/reference/
    generated/scipy.spatial.distance.pdist.htmland for each dataset in the reposi-
    tory, use the validation samples to tune the parameterKand selecting one distance measure. With
    this optimal distance and value ofK, compute the test accuracy.
2. Aggregate the results across all datasets, and rank all distance metrics according to the test accuracy.
3. Note: If you are not able to work through all datasets, please downscale the number of datasets.

## Exercise 3: Accelerating K-Nearest Neighbour Classifier 

The task for this exercise is to implement the following two speedup strategies covered in the lecture.
Please refer to the lecture for pseudo-code and more details.

1. Partial Distances/Lower Bounding

Please use the Euclidean distance and the dataset with the largest number of samples for this exercise.
Justify the choice of associated hyperparameters of the above two strategies accordingly.



