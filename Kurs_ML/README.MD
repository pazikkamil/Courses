# Machine learning cheat-sheets

## Supervised learning 
We know the structure and outcome.
We have bunch of examples and we know the correct answer.
Key features are known, labels are also known.
We split data into training and test data.

### Features
We can represent features as x axis

| Object | Features |
|:------:|:--------:|
| **Music** | tempo, genre, gender of voice |
| **If meditate** | focus, calmness |

### Labels
It can be Y axis 


| Supervised learning |                             |
|:---------------------:|:---------------------------|
| **Methods**             |classification, regression, svm|
| **Validation methods**  |cross validation                |
| **Algorithms**          |Decision tree, C4.5, K-NN, Naive Bayes|

### Classification
Classify labeled data


#### Naive Bayes

##### Bayes rule
Thomas Bayes - he wanted to prove that God exists.

* Sensitivity
* Specificity

#### Decisoin tree

| What       | Description      |
|:----------:|:-----------------|
| **Root**   |                  |
| **Leaf**   |                  |
| **Node**   |                  |

#### K-Nearest Neighbors - > A classification model

> K-Nearest Neighbors - A classification model
> -- <cite>[Big Data University][1]</cite>

![Knn method]
(http://mars.wiwi.hu-berlin.de/mediawiki/teachwiki/images/e/e2/Hl_knn.JPG)

[1]:https://courses.bigdatauniversity.com

Examples of classifications
![Image of classification]
(http://3.bp.blogspot.com/-HFPsQbmRQZQ/UGNvH_t06jI/AAAAAAAAD_Y/G7XYOTVa2mM/s1600/Screen+Shot+2012-09-26+at+2.08.25+PM.png)

### Regression
Predicting trends using previous labeled data
Examples of regression
![Image of regression]
(https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Linear_regression.svg/640px-Linear_regression.svg.png)

To do

- [X] images
- [ ] codes
- [ ] app

### Examples of svm (Support vector machine)
Look at skulls_epoch

## Unsupervised learning
We don't know much about our data, don't know the outcomes

* Deals with unlabeled data
* More complex algorithms than supervised learning
* Fewer tests than supervised
* algorithms utilizes centroids

| Unsupervised learning |           |
|:---------------------:|:----------|
| **Methods**           |clustering, K-means,Hierarchical clust., Density based clust  |

### Clustering
Finding patterns and groups in unlabeled data

## Outliers

### Removing outliers

## Error types

| Error type | Description |
|:----------:|:------------|
| **Type 1** |             |

## Over-fitting data
If we use 100% percent of our data, to test model it would be 100% accurate.
Which is wrong. We should use 10% data as a test set

## Visualization of data

### Scatter plot