# Models

### Approach
* Ask clarifying questions.
* Identify type of problem (classification, regression, timeseries)
* Brainstorm wide variety of diverse data sources.
* Quickly list out potential features and transforms needed.
  * Discretize continuous values.
  * Feature crosses.
  * Analyze feature coverage for positive and negative examples.
  * **Feedback loop prevention** - positional features
    * Weight higher position features heavily so other features get lower weights. When serving turn position feature off.  
* Ensure features are available at inference time.
* Talk through model complexity and training stats
  * Number of data points - N
  * Neural net - size of embedding ~ log(N)
  * Size of trained model ~ number of parameters
    * Linear model - number of feature weights that can be learned ~ N
    * Scale up model size with amount of data
      * 1000 examples - 12 features e.g. dot product, TF-IDF, human engineered
      * 1 million examples - 100k features e.g.intersection terms, regularization and feature selection.  
      * 1 billion+ examples - 10 million features e.g.feature crosses, feature selection and regularization
* Define model evaluation metrics.
* Brainstorm business metrics and experimentation strategy to measure model lift over baseline.
* Observability and monitoring for feature data quality and prediction quality.  


### Linear Regression
* L2 loss = `||Y - X.beta||^2`
* Closed form solution `beta = (X_T.X)^-1.X_T.Y`
* Runtime = `O((n+d)* d^2)`
* Distributed training - backprop with SGD optimizer
* Feature manipulation
  * max(features) can be a valid new feature which improves performance.
  * linear combination of features will create a non invertible matrix and give indeterminate coefficients.

### Logistic Regression
* Loss function
  * single class - [binary cross entropy / log loss](http://en.wikipedia.org/wiki/Cross_entropy#Cross-entropy_loss_function_and_logistic_regression) = `-Σ(ylog(y_hat)+(1−y)log(1−y_hat))` where y is the 1 / 0 label and y_hat is the predicted probability.
  * multiclass - [cross entropy](https://www.cs.princeton.edu/courses/archive/spring16/cos495/slides/ML_basics_lecture7_multiclass.pdf)
* Training - no closed form solution, use gradient descent.
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
* Minimize `||w||` s.t `y_i (w.x_i - b) >= 1` to get **w** and b.
  * Separation between the support vector hyperplanes = `2/||w||`
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
  * Loss function = sum of distances to cluster centroids for all points.
  * First phase - single pass greedy (local optimum) approach to get approximate clusters.
  * Second phase - multiple iterations over each point to update cluster assignment if it reduces the loss function.  
* Runtime - `O(n * k * i * d)` where n = number of data points, k = number of clusters, i = number of iterations, d = number of dimensions.

### Naive Bayes

* Solve for `C_pred = argmax P(C_k|X) = argmax P(C_k) ∏ P(x_j|C_k)` where 1 <= j <= d, d = number of features, m = number of classes
* Good with high dimensional data due to independence assumption.
* Training runtime - `O(nd)` to compute and store `O(dm)` probabilities.

### Heterogenous Treatment Effects
* Hybrid of experimentation and inference model.
  * Control / treatment assignment is an additional feature.
  * Train GBM and use predictions for control / treatment assignment decision.

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
* For overfit models i.e. training RMSE << test RMSE
* L1 - drives down number of non zero coefficients.
* L2 - drives down absolute value of feature coefficients.
* Neural nets - use dropout
* Decision trees - limit tree depth

## Visualization
* [Decision Boundary](https://www.kdnuggets.com/2015/06/decision-boundaries-deep-learning-machine-learning-classifiers.html)
* [Scatterplot matrix](https://seaborn.pydata.org/examples/scatterplot_matrix.html)

## Model Evaluation
* Classification
  * Precision = `TP / (TP + FP)`
  * Recall / True Positive Rate = `TP / (TP + FN) = TP / P`
  * False Positive Rate = `FP / (TN + FP) = FP / N`
  * Accuracy = `(TP + TN) / (P + N)`
  * PR curve - precision decreases with increase in recall.
  * ROC curve - true positive rate vs false positive rate.
    * Diagonal for completely random classifier, AUC = 0.5

# Applications

## Recommender Systems

### Components

#### Candidate Generation

* **Item similarity**
  * Collaborative Filtering
    * Build co-occurrence matrix of items from rating matrix.
    * Use [log-likelihood similarity metric](http://tdunning.blogspot.com/2008/03/surprise-and-coincidence.html) (entropy based) to weight anomalous co-occurrences higher - not just because the items were popular.
    * For each item, build top similar item list.
    * Write to an indexed store like HBase or ElasticSearch.
  * MinHash / LSH clustering
  * KNN on item embedding from matrix factorization.
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
* [Neural Nets](https://developers.google.com/machine-learning/recommendation/dnn/softmax)
  * Softmax DNN
    * Input
      * Per user dense and sparse features
    * Output
      * Probability vector of user interaction with each item.
    * Loss function
      * Cross entropy loss from actual user / item interaction data.
    * The weights of the final softmax layer correspond to the item embedding V in matrix factorization.
    * Scoring
      * Take user query and convert to a query embedding - run it through trained net until the pre-softmax layer.
      * Take the dot product with the item embedding to get a probability score vector.
  * Neural net with user and item embeddings
    * one neural net maps user / query features to embedding.
    * one neural net maps item features to embedding.
    * dot product between embeddings provides score for each user / item pair.
  * Pros - can use user and item features in the model
  * Cons - query embedding needs to be computed at serving time which is expensive.


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
* [Rules of ML](https://developers.google.com/machine-learning/guides/rules-of-ml/)
* [Neural net recipes](http://karpathy.github.io/2019/04/25/recipe/)
* [Imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data)

## Terms
* odds = `p/(1-p)`
* logit = log odds = `log(p/(1-p))`
