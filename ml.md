## Concepts

### Linear Regression
* L2 loss = `\|\|Y - X.beta\|\|^2`
* Closed form solution `beta = (X_T.X)^-1.X_T.Y`
* Runtime = `O((n+d)* d^2)`
* Distributed training - backprop with SGD optimizer

### Logistic Regression
* Loss function
  * single class - [binary cross entropy loss](#https://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_loss_function_and_logistic_regression)
  * multiclass - [cross entropy](#https://www.cs.princeton.edu/courses/archive/spring16/cos495/slides/ML_basics_lecture7_multiclass.pdf) 
* Activation function
  * single class - sigmoid
  * multiclass - softmax

### Decision Trees

### Support Vector Machine

### Random Forests

### Boosted Trees

### KNN

### K-means Clustering

### Naive Bayes

### Expectation Maximization
* Same as MAP (maximum a priori) and maximum likelihood.

### Embeddings


### Backpropagation
* Iterative algorithm to train multilayer neural networks.
* Use optimizers (SGD, Adam etc) for direction training should take based on value of loss function.

### Regularization
* L1 - drives down number of non zero coefficients
* L2 - drives down value of feature coefficients
* Dropout

## Terms
* odds = `p/(1-p)`
* logit = log odds = `log(p/(1-p))`
