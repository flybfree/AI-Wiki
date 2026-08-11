# Summary: 2026-08-09_11-15-21Z_SmartCompaction_PredictingCompactionUtilityfromLak.md
Saved: 2026-08-10 23:20
Source: 2026-08-09_11-15-21Z_SmartCompaction_PredictingCompactionUtilityfromLak.md
Model: None

---

## Summary  
Open lakehouse table formats accumulate small data files over time, which degrades query performance, yet deciding when compaction is worthwhile relies on simple thresholds that ignore the true impact of metadata. This paper introduces a systematic simulation framework to quantify how 17 metadata features from Iceberg manifest files correlate with compaction utility, measured as the continuous file‑reduction ratio (R2 = 0.998, RMSE = 0.013). The study also discovers that the binary decision to compact can be solved by a single partition‑level threshold and does not require a learned model.

## Key Contributions  
- [Finding 1] XGBoost predicts compaction utility with high accuracy (R2 = 0.998, RMSE = 0.013) using only metadata extracted from Iceberg tables.  
- [Finding 2] The optimal binary decision is trivially separable by the threshold `max_files_per_partition > 4`, indicating no need for a learned model.  
- [Finding 3] Cross‑schema validation on 96 TPC‑H tables shows generalisation without retraining (R2 = 0.976), confirming robustness across schemas.

## Methodology  
The authors generated 2,376 Apache Iceberg tables spanning three orders of magnitude in file size. From each table’s manifest they extracted 17 metadata features—such as number of files per partition and schema complexity—without reading the underlying data. These features were fed into an XGBoost regressor to model the reduction ratio, while a simple rule‑based classifier was used for the binary compaction decision. The pipeline was repeated across multiple schemas to evaluate generalisation.

## Results  
The regression achieved R2 = 0.998 and RMSE = 0.013, demonstrating strong predictive power. The binary threshold `max_files_per_partition > 4` correctly separates tables that benefit from compaction from those that do not, with a classification accuracy of near‑perfect results (R2 ≈ 1). Cross‑schema validation on TPC‑H data retained R2 = 0.976, confirming the model’s applicability without retraining. A query benchmark revealed that compaction improves performance for metadata‑heavy queries but can marginally slow full‑scan aggregations by reducing task parallelism.

## Significance  
By quantifying which metadata characteristics drive compaction utility, this work enables lakehouse operators to automate and optimise table maintenance. The discovery of a single partition‑level threshold eliminates the need for complex models, reducing overhead while preventing unnecessary compactions that could impair query performance.

## Related Concepts  
- Apache Iceberg (open lakehouse storage format)  
- Compaction (process of merging small files into larger ones)  
- File‑reduction ratio (R2) and RMSE as evaluation metrics  
- XGBoost (gradient boosting classifier for regression)  
- Metadata features extracted from table manifests  
- Partition‑level thresholding in distributed storage systems  
- TPC‑H benchmark suite for evaluating query performance
