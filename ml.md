# Models

### Linear Regression
* L2 loss = `||Y - X.beta||^2`
* Closed form solution `beta = (X_T.X)^-1.X_T.Y`
* Runtime = `O((n+d)* d^2)`
* Distributed training - backprop with SGD optimizer

### Logistic Regression
* Loss function
  * single class - [binary cross entropy / log loss](http://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_loss_function_and_logistic_regression) = `-Σ(𝑦log(𝑝)+(1−𝑦)log(1−𝑝))`
  * multiclass - [cross entropy](https://www.cs.princeton.edu/courses/archive/spring16/cos495/slides/ML_basics_lecture7_multiclass.pdf)
* Activation function
  * single class - sigmoid
  * multiclass - softmax

### [Decision Trees](http://cs229.stanford.edu/notes/cs229-notes-dt.pdf)
* Training runtime = `O(nfd)` where f = number of features, n = number of data points and d is depth of the tree. Worst case is `O(n^2f)` and best case is `O(nf log n)`
* Scoring runtime = `O(log n)`
* Hyperparameters
  * split criterion - entropy or gini (categorical), mse (continuous)
  * max depth
  * class weight - for imbalanced data sets.

### Support Vector Machine
* Minimize `||w||` s.t `y_i (w.x_i - b) >= 1`
* Solve the Lagrangian dual instead.
* SMO (sequential minimal optimization) commonly used
  * Runtime - `O(n^3)`
* Hyperparameters
  * C - regularization parameter, inversely proportional to the distance between dividing hyperplanes
  * kernel - rbf (radial basis function), sigmoid, polynomial
  * class weight - for imbalanced data sets.

### Random Forests
* Hyperparameters
  * num estimators - number of random trees
  * others same as [decision trees](#decision-trees)

### Boosted Trees
* Steps
  * Initialize to a constant value that minimizes loss
  * Fit a weak learner on residuals.
  * Find the optimal weight for the new learner by minimizing loss when combining the new learner with what has been trained so far.
  * Compute residuals and fit another weak learner and repeat.
* Regularize subsequent trees by shrinkage factor = learning rate.
* [Why boosted trees don't overfit](https://jeremykun.com/2015/09/21/the-boosting-margin-or-why-boosting-doesnt-overfit/)
* Hyperparameters
  * learning rate
  * num estimators
  * others same as [decision trees](#decision-trees)

### KNN
* Build KD tree from training data
  * Runtime - `O(dn log n)` where d = number of dimensions, n = number of data points.
* For each test point, do traverse the KD tree to narrow down number of candidates until you get the desired number of neighbors.

### K-means Clustering
* Lloyd's algorithm
* Runtime - `O(n * k * i * d)` where n = number of data points, k = number of clusters, i = number of iterations, d = number of dimensions.

### Naive Bayes

* Solve for `C_pred = argmax P(C_k|X) = argmax P(C_k) ∏ P(x_j|C_k)` where 1 <= j <= d, d = number of features, m = number of classes
* Good with high dimensional data due to independence assumption.
* Training runtime - `O(nd)` to compute and store `O(dm)` probabilities.

## Training Techniques

### Expectation Maximization
* Same as MAP (maximum a priori) and maximum likelihood.

### Backpropagation
* Iterative algorithm to train multilayer neural networks.
* Use optimizers (SGD, Adam etc) for direction training should take based on value of loss function.
* Single step forward + backprop runtime = `O(mnk)` where n = input dimensions, m = output dimensions, k = batch size assuming naive matrix multiplication

### Embeddings
* Convert sparse input tensor to a dense representation with fewer dimensions.
* Use embedding layer (same as dense layer but with [simplifying assumptions](https://stackoverflow.com/questions/47868265/what-is-the-difference-between-an-embedding-layer-and-a-dense-layer)) as the first hidden layer in a neural net to train a prediction model.
* The embedding is the **output of the first hidden layer** and is obtained as a byproduct of the neural net training.

### Regularization
* L1 - drives down number of non zero coefficients.
* L2 - drives down absolute value of feature coefficients.
* Dropout

# Applications

## Recommender Systems

### Components

#### Candidate Generation

* **Item similarity**
  * Build co-occurrence matrix of items from rating matrix.
  * Use [log-likelihood similarity metric](http://tdunning.blogspot.com/2008/03/surprise-and-coincidence.html) (entropy based) to weight anomalous co-occurrences higher - not just because the items were popular.
  * For each item, build top similar item list.
  * Write to an indexed store like HBase or ElasticSearch.
* **Matrix factorization**
  * Model rating matrix `A ~ U_T.M` where U is the user embedding and M is the item embedding of dimension d.
  * Loss function = MSE (mean squared error) + regularization = `||(A - U_T.M||^2 + w||U_T.M||^2`
  * Training
    * [Weighted alternating least squares](https://developers.google.com/machine-learning/recommendation/collaborative/matrix)
      * Initialize to random numbers.
      * Fix one matrix (U) and the loss function becomes convex for elements of the second matrix (M).
      * Use gradient descent to update weights of M.
      * Fix the weights of M and the loss function is now convex for elements of U.
      * Use gradient descent to update the weights of U.
      * Keep alternating until convergence.
    * Backprop / SGD
      * Slower to converge since loss function not convex.
      * Need negative sampling of unobserved entries, otherwise spurious recommendations can be made.
  * Precompute scores for each item j for a user for ranking:
    * dot product = ``<u, M_j>`` where u = user embedding and M_j is item embedding for item j
      * skewed toward popular item
    * cosine = ``<u, M_j> / ||u|| ||M_j||`` where u = user embedding and M_j is item embedding for item j
      * not skewed toward popular items

### Retrieval
* If scores have been precomputed, simple retrieval of top candidates.
* Approximate nearest neighbors.

### Scoring
* Get candidates from different sources and score by a single model for optimizing an objective function (e.g. clicks, watch time).

### Re-ranking
* Rerank based on user preferences and other factors like freshness, diversity, fairness.

## Resources
* [Google news recommender paper](https://www2007.org/papers/paper570.pdf)
* [Google recommender systems course](https://developers.google.com/machine-learning/recommendation/overview/types)

## Terms
* odds = `p/(1-p)`
* logit = log odds = `log(p/(1-p))`
