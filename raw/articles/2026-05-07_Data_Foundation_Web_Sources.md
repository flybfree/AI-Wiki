# Web sources for Lesson 3: Data as the Foundation of Learning

This note collects web sources that support the lesson’s discussion of leakage, split strategy, imbalance-aware evaluation, feature consistency, and versioning.

## Sources

- scikit-learn common pitfalls: https://scikit-learn.org/stable/common_pitfalls.html
  - Supports the discussion of data leakage, pipelines, and the need to fit transformations on training data only.

- scikit-learn precision-recall example: https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html
  - Supports the point that precision-recall curves are useful when classes are very imbalanced.

- scikit-learn balanced_accuracy_score: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.balanced_accuracy_score.html
  - Supports the point that balanced accuracy averages recall across classes and is useful when one class dominates.

- scikit-learn TimeSeriesSplit: https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.TimeSeriesSplit.html
  - Supports the idea that time-ordered data should be split chronologically rather than randomly.

- IBM, What is Data Leakage in Machine Learning?: https://www.ibm.com/think/topics/data-leakage-machine-learning
  - Supports the beginner-friendly explanation of train/test leakage and why split design matters.

- Google, Rules of Machine Learning: https://developers.google.com/machine-learning/guides/rules-of-ml
  - Supports the discussion of training-serving skew, code reuse between training and serving, and explicit monitoring.

- Google Cloud blog on training-serving skew: https://cloud.google.com/blog/topics/developers-practitioners/monitor-models-training-serving-skew-vertex-ai
  - Supports the practical explanation of how data drift and pipeline mismatches create skew.

- Databricks, Point-in-time feature joins: https://docs.databricks.com/aws/en/machine-learning/feature-store/time-series
  - Supports point-in-time correctness and the risk of using future feature values in training data.

- Feast point-in-time joins: https://docs.feast.dev/getting-started/concepts/point-in-time-joins
  - Supports the feature-store discussion, especially historical joins that reproduce the state of the world at prediction time.

- Microsoft Learn, Dataset versioning: https://learn.microsoft.com/en-us/azure/machine-learning/how-to-version-track-datasets?view=azureml-api-1
  - Supports the point that dataset versions should be reproducible and that changing referenced content can break reproducibility.

- Encord, How to Split Machine Learning Datasets: Training, Validation, & Test Sets: https://encord.com/blog/train-val-test-split/
  - Supports stratified splitting and the idea of keeping class proportions representative across splits.
