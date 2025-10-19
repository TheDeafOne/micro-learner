# Summary for EN.705.601.81.FA25 Applied Machine Learning – Module 6: Ensemble Learning – Module 6 -  Video Lectures

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=21c73759-fb0e-4a8c-a1c4-b0c60021a466

# Lecture summary

- Ensembles of many weak classifiers trained on random subsets of features can improve supervised learning.
- Weak learners have limited capacity; diversity is created by using different feature subsets and randomness.
- Aggregation by majority voting leverages the sheer number of weak classifiers to reduce error, increase robustness, and often outperform single complex classifiers.
- Random forest is a prime example: an ensemble of weak decision trees.
- Decision tree classifiers and their visualizations are used to illustrate how weak learners operate.
- Using fewer features per weak classifier increases diversity; combined (voted) predictions typically surpass individual classifier performance.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4e3c5980-6e76-4826-90d1-b0c50151eccc

# Summary — Ensemble learning & random forests

- Ensemble learning: combine many weak learners (hundreds or thousands) to form a stronger, more robust classifier. Ensembles often generalize better and reduce overfitting compared to single complex models.

- Ways to build ensembles:
  - Bagging (bootstrap aggregating): train weak learners on different subsets of data points.
  - Feature subsampling: train learners on different subsets of features (used in random forests).
  - Boosting (iterative reweighting of samples) — mentioned as another ensemble approach.

- Why ensembles help:
  - Parallelizable — learners can be trained/evaluated in parallel for speed.
  - Increased robustness and generalization through diversity among learners.
  - Mitigates curse of dimensionality by training learners on feature subsets rather than the full joint feature space (example: with many features, using subsets avoids needing an exhaustive joint density).

- Random forest specifics:
  - Ensemble of decision trees, each trained on a bootstrap sample of data and a random subset of features.
  - Common heuristic: use sqrt(m) features (where m = total number of features) per tree.
  - Final prediction by majority voting (classification) or averaging (regression).
  - Low sensitivity to hyperparameters; reasonable defaults (e.g., shallow trees, 200–500 trees, sqrt(m) features) often produce strong results.
  - Few parameters to tune, making random forests widely useful and robust.

- Implementation note: each tree is built using standard decision tree construction on its sampled data/features; the ensemble aggregates their outputs.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=79344ce4-bbc6-4783-a458-b0c600755943

# Decision tree classifier — concise summary

- Purpose and advantages
  - Decision trees are interpretable classifiers (not black-box like SVMs or neural nets).
  - They form the base learners in ensemble methods such as random forests.
  - Useful for communicating models to subject-matter experts because the split rules are explicit.

- Data and encoding
  - Categorical feature levels can be mapped to ordinal integers when a natural order exists (e.g., food: bad=0, okay=1, good=2).
  - Binary targets (e.g., tip: yes/no → 1/0) can be encoded with label encoders; one-hot encoding is not required when order/relation exists.
  - Real datasets may contain conflicting rows; this only affects conditional class probabilities, not the ability to build a tree.

- Building and visualizing trees (scikit-learn)
  - Fit a DecisionTreeClassifier on X (features) and y (labels) using scikit-learn.
  - Use export_graphviz to export the learned tree to DOT (graph description language) format and render with Graphviz (installable via conda).
  - The exported visualization shows feature names, class names, split thresholds, node impurity (Gini/entropy), sample counts and class distributions.

- Example outcomes
  - A learned tree reproduces human-readable rules (e.g., "if food is bad/okay → no tip; if food is good then check speed/price → yes/no").
  - Applied to standard datasets (e.g., Iris), the tree yields specific thresholds (e.g., petal width cutoff) and node impurities reflecting split quality.

- Impurity measures and feature importance
  - Node impurity measured by entropy or Gini index; these decrease as the tree partitions the data.
  - The algorithm chooses splits that maximize impurity reduction; features producing the largest decrease are ranked more important.

- Algorithms and complexity
  - ID3 and similar algorithms evaluate candidate splits using impurity criteria rather than exhaustive truth-table enumeration.
  - Exhaustive search over all feature/value combinations grows exponentially with the number of features; impurity-based heuristics make training tractable.
  - Training uses greedy optimization (choose best split at each node) and follows Occam’s razor by favoring simpler trees (fewer splits) that reduce impurity early.

- Practical note
  - Visual, rule-based trees aid model interpretation and collaboration; the remaining algorithmic details (pruning, splitting criteria variants, stopping rules) can be studied as extensions.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=53b4ba84-3ae3-4606-83db-b0c60178631e

# Summary

- Dataset
  - Titanic preprocessed dataset: 891 rows, mostly binary/categorical features plus numerical features like age and fare.
  - Class imbalance: ~61% not survived, ~38% survived.
  - Exploratory insights: higher survival for females and first-class passengers; fare correlates strongly with survival; age shows nonmonotonic effects (babies more likely to survive).

- Experimental setup / implementation details
  - Models evaluated with 10-fold cross-validation; mean accuracy and standard deviation recorded.
  - Weak-learner ensemble implementation:
    - Use Gaussian Naive Bayes as the primitive (weak) learner.
    - For each ensemble member: randomly select a subset of features (without replacement), train a Naive Bayes, store that classifier and its feature list.
    - For prediction: each weak learner predicts on its feature subset; final class by majority voting.
    - Parameters varied: ensemble size (hundreds), number of features per weak learner, number of repetitions for statistics.

- Individual classifier results (examples)
  - Gaussian Naive Bayes (full features): ~45% mean accuracy (high variance).
  - Linear SVC: ~74–80% depending on settings.
  - Logistic Regression: ~81%.
  - Neural network: ~84%.
  - Random forest consistently high due to built-in feature selection (information gain / Gini).

- Ensemble of Naive Bayes weak learners (observations)
  - Naive Bayes weak-learner ensembles can perform worse if many weak learners lack access to informative features: examples showed ensemble accuracy dropping (e.g., ~39%) with many irrelevant features and many weak learners.
  - Individual weak learners showed large variance when using random small feature subsets (some succeed by chance, many fail).
  - Plain Naive Bayes using all features can outperform a poorly constructed Naive Bayes ensemble because it benefits from aggregating all informative features.

- Feature ranking / reduction
  - Correlation-based ranking with the class used to remove low-correlation features (simple thresholding).
  - Reducing to top ~25 features markedly improved Naive Bayes performance.
  - Results after reduction:
    - Plain Naive Bayes (reduced features): ~76% accuracy.
    - Ensemble Naive Bayes (using ranked-reduced features; ensemble size ~211): ~78% accuracy with lower standard deviation.
  - Varying number of features showed:
    - Plain Naive Bayes is highly sensitive to which features are included (high variance).
    - Ensemble Naive Bayes is more robust/insensitive: performance plateaus after ~15 features and maintains lower variance.

- Conclusions / takeaways
  - Ensembles of weak learners can improve generalization and reduce variance, but success depends on the weak learner's ability to work with randomly sampled feature subsets.
  - Naive Bayes weak learners are vulnerable to irrelevant/useless features; ensembles of such weak learners require careful feature ranking/reduction to be effective.
  - Decision-tree-based ensembles (e.g., random forest) are more robust to irrelevant features because trees perform implicit feature selection during training.
  - Combining feature ranking with ensembles yields better and more stable performance than either naive ensembles or plain Naive Bayes on unfiltered features.