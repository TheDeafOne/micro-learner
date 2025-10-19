# Summary for EN.705.601.81.FA25 Applied Machine Learning – Module 6: Ensemble Learning – Module 6 -  Video Lectures

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=21c73759-fb0e-4a8c-a1c4-b0c60021a466

# Summary

- Ensembles of many weak classifiers that each use limited subsets of features improve supervised learning performance and robustness.
- Individual classifiers are intentionally simple/limited; their sheer number and majority voting combine strengths and reduce errors.
- Random forest is a top ensemble method built from weak decision tree classifiers.
- Decision tree classifiers and their visualizations are central to understanding and building such ensembles.
- Combining many weak classifiers that each use fewer features and limited learning capability yields aggregate performance that often surpasses individual classifiers.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4e3c5980-6e76-4826-90d1-b0c50151eccc

# Summary — Ensemble Learning & Random Forests

- Ensemble learning builds a strong classifier by combining many weaker learners (hundreds to thousands), improving robustness and generalization compared with a single complex classifier.
- Ensembles can run learners in parallel (faster inference) and reduce overfitting by aggregating diverse, more abstract weak learners.
- Two common ensemble techniques:
  - Bagging (bootstrap aggregating): use different subsets of data points for each learner.
  - Feature subsetting (used in random forests): use different subsets of features for each learner.
- Curse of dimensionality motivation: high-dimensional spaces require prohibitive amounts of data to estimate joint densities; training weak learners on feature subsets alleviates this.
- Aggregation method: majority voting (or similar) over weak learners’ predictions produces the final decision.
- Random forest specifics:
  - Base learners are decision trees built with bootstrap samples and feature subsets.
  - Typical heuristic: use sqrt(m) features per split (m = total number of features).
  - Ensemble size (number of trees) must be chosen, but predictions are not highly sensitive to this; common defaults work well (e.g., shallow trees of limited depth, a few hundred trees like 200–500).
  - Few hyperparameters and low sensitivity make random forests robust and popular.
- Decision tree learning (built with standard decision tree algorithms) is the core building block for random forests.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=79344ce4-bbc6-4783-a458-b0c600755943

# Decision Trees — Summary

- Role and motivation
  - Decision trees are interpretable classifiers and the base learners for random forests.
  - They are not black boxes, enabling direct communication with subject-matter experts.

- Data and encoding
  - Categorical levels with natural ordering (e.g., bad, okay, good) can be label-encoded (0,1,2) instead of one-hot encoding when order matters.
  - Conflicting rows in the dataset change conditional probabilities; trees model those probabilities rather than deterministic rules.

- Building and using trees (scikit-learn)
  - DataFrame → label encoding → X (features) and y (targets) → fit DecisionTreeClassifier.
  - Export and visualize trees using export_graphviz to produce DOT files (Graphviz) for plotting.
  - Feature names and class names can be included in the exported graph for readable visualizations.

- Visualization and interpretation
  - Tree nodes show splits (feature threshold), class predictions, and impurity metrics.
  - Example: food > 1.5 (good) leads to different tip outcomes than food ≤ 1.5 (bad/okay).
  - Visual trees are useful for sharing results and eliciting domain knowledge (e.g., “petal width < 1.75 implies versicolor”).

- Impurity measures and feature importance
  - Gini index and entropy quantify node impurity; values decrease as the tree makes informative splits.
  - The algorithm selects splits that reduce impurity most — higher impurity reduction signals more important features (e.g., petal width being most informative in Iris).

- Algorithms and complexity
  - ID3 (and similar algorithms) search over feature/value splits; exhaustive search grows combinatorially with features.
  - Practical algorithms use greedy heuristics to choose splits and are therefore fast in practice.
  - Occam’s razor principle: prefer simpler trees that achieve large impurity reductions near the root.

- Practical notes
  - Trees learned from data reflect the training model and may not have perfect reclassification accuracy.
  - Exported tree visualizations and impurity/threshold annotations make model decisions transparent and actionable.

## https://jh.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=53b4ba84-3ae3-4606-83db-b0c60178631e

- Dataset
  - Preprocessed Titanic data: 891 rows, mostly binary features plus numeric age and fare. Class label: survived (imbalanced: ~38% survived, ~61% not survived).
  - Initial data exploration showed expected patterns: higher survival for females and certain fare/class ranges; age effects (children/babies survive more).

- Baseline classifiers and evaluation
  - Ten-fold cross-validation used throughout; mean accuracy and standard deviation reported.
  - Gaussian Naive Bayes baseline: ~45% accuracy (high variance).
  - Other classifiers on full data: linear SVC ~80%, balanced SVC ~74%, RBF SVC 66–73% (parameter dependent), logistic regression ~81%, neural network ~84% (best).
  - Priors for Naive Bayes were computed and used to help balance class effects.

- Ensemble of weak learners (Naive Bayes)
  - Weak learners: Gaussian Naive Bayes trained on random subsets of features (feature subsets chosen without replacement).
  - Ensemble construction:
    - Generate ensemble_columns: a list of feature lists (one list per weak learner).
    - Fit each weak learner on the training folds using its assigned feature subset; store classifier + feature-list mapping.
    - Prediction by majority vote across weak learners for each sample.
  - Parameters experimented with: ensemble size (e.g., 100–200 weak learners), number of features per weak learner (e.g., 3–11), and multiple iterations (e.g., 10) to collect statistics.

- Problems observed with naive Bayes ensembles on raw data
  - Simple ensemble of Naive Bayes weak learners often performed worse or only slightly better than single Naive Bayes (examples: NB 45% → ensemble ~48% with large std; in some runs ensemble dropped to ~39%).
  - Cause: many weak learners randomly miss the informative features; Naive Bayes treats features equally and cannot internally select or down-weight useless features like decision trees do.

- Feature ranking and reduction
  - Used correlation of each feature with class label to rank features.
  - Removed weakly correlated features (simple thresholding), reducing to 25 features from the full set.
  - On reduced feature set:
    - Single Naive Bayes jumped to ~76% accuracy (low std).
    - Ensemble of Naive Bayes improved further to ~78% (lower standard deviation than single NB), showing better robustness.

- Systematic experiment: varying number of features
  - Ran experiments varying number of top-ranked features used (from few up to 35) comparing plain Naive Bayes vs ensemble Naive Bayes.
  - Findings:
    - Plain Naive Bayes accuracy is sensitive to which features are included; performance fluctuates and has higher variance.
    - Ensemble Naive Bayes is more robust to number of features, plateaus after ~15 top features and maintains stable performance and lower variance.
    - Ensembles reduce error variance (tighter std bands) and generalize better even if maximum accuracy is not the absolute highest.

- Comparisons and interpretation
  - Random Forests (decision-tree based ensembles) were less impacted by irrelevant features because individual trees select informative splits (information gain/Gini), so they naturally handle bad features better than Naive Bayes weak learners.
  - For weak learners that cannot internally select features (like Naive Bayes), external feature ranking/reduction is crucial before ensembling.

- Conclusions
  - Ensembles of weak learners can significantly improve generalization and reduce variance, but effectiveness depends on:
    - The base learner’s ability to handle irrelevant features.
    - Feature selection/ranking when base learners are feature-insensitive.
  - With proper feature reduction, an ensemble of Naive Bayes classifiers yields robust performance gains and lower standard deviation compared to single Naive Bayes.