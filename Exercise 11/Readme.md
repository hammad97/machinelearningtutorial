
## Exercise Sheet 11


## Exercise 0: Preprocessing Text Data 

In this exercise, you are tasked with implementing a Text Classifiers to categorize news items. The dataset
name and link:

- 20newsgroups dataset (A collection of 20,000 news items across 20 categories)
- Available via Scikit-Learn Datasets API.
- Subset the dataset to only the following two categories named as ’sci.med’ and ’comp.graphics’

The preprocessing tasks are as follows:

```
1) Preprocessing textual data to remove punctuation, stop-words (list available via external libraries
such as NLTK and spaCy).
```
```
2) Implementing a bag-of-words feature representation for each text sample
```
```
3) Implementing a TF-IDF feature representation for each text sample
4) Split the dataset randomly into train/validation/test splits according to ratios 80%:10%:10%
```

## Exercise 1: Implementing Naive Bayes Classifier for Text Data 

In this exercise, you are tasked with implementing a Naive Bayes Classifier to categorize news items. The
Naive Bayes assumption is conditional independence of the features when modeling for the label.

```
1) For both preprocessing types train and validate the Naive Bayes Classifier to classify each news item
to the two categories named above.
```
```
2) Report the test set accuracy.
```
## Exercise 2: Implementing SVM Classifier via Scikit-Learn 

Please refer to the Scikit-Learn library for implementation of SVM classifiers. You are required to replace
the classifier in Exercise 1 with SVMs.

```
1) Tune the different SVM kernel choices provided by Scikit-Learn, and other associated hyperparam-
eters for validation set.
```
```
2) Report the test-set accuracy.
```
