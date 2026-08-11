# Summary: 2026-08-09_11-15-21Z_SmartCompaction_PredictingCompactionUtilityfromLak.md
Saved: 2026-08-10 23:17
Source: 2026-08-09_11-15-21Z_SmartCompaction_PredictingCompactionUtilityfromLak.md
Model: None

---

## Summary  
The paper tackles the problem of deciding when to perform compaction on lakehouse tables, a task that traditionally relies on arbitrary thresholds and can degrade query performance. By leveraging metadata rather than raw data, it builds an open simulation framework that predicts the utility of compaction as a continuous file‑reduction ratio, ultimately revealing a single partition‑level rule that makes a learned model unnecessary. The study also validates this approach across multiple schemas and query patterns, showing both benefits for metadata‑heavy workloads and potential slowdowns for full‑scan aggregations.

## Key Contributions  
- A large‑scale simulation generates 2,376 Apache Iceberg tables with 17 metadata features, training an XGBoost model that predicts a continuous reduction ratio (R² = 0.998, RMSE = 0.013).  
- The binary decision to compaction is trivially separable by the single threshold `max_files_per_partition > 4`, eliminating the need for a learned model.  
- Cross‑schema validation on 96 TPC‑H tables and a query benchmark confirm generalisation (R² = 0.976) while highlighting trade‑offs between metadata‑heavy queries and full‑scan aggregations.

## Methodology  
The authors constructed an open simulation framework that extracts 17 metadata attributes from Iceberg manifest files without reading the underlying data, feeds these features into an XGBoost regression model to estimate the file‑reduction ratio, and then tests whether a simple threshold on `max_files_per_partition` suffices for binary compaction decisions. Validation is performed on a TPC‑H dataset using the same metadata, confirming that no retraining is required.

## Results  
The XGBoost regression achieves a high R² of 0.998 with RMSE of 0.013, indicating strong predictive power for continuous reduction estimates. The binary decision rule `max_files_per_partition > 4` correctly separates compaction‑beneficial from non‑beneficial tables across the simulated data. Cross‑schema validation yields an R² of 0.976 on TPC‑H tables, demonstrating robust generalisation. Query benchmarking shows that metadata‑heavy queries gain performance, whereas full‑scan aggregations may experience reduced task parallelism due to smaller file counts.

## Significance  
This work provides a data‑driven, threshold‑based methodology for compaction decisions in lakehouse environments, reducing reliance on manual heuristics and improving overall storage efficiency. By exposing the single most influential metadata feature, it enables automated optimisation pipelines that can be applied across diverse schemas without retraining models.

## Related Concepts  
- Lakehouse architecture  
- Apache Iceberg table format  
- Compaction (data‑storage maintenance)  
- XGBoost regression for continuous prediction  
- File fragmentation and reduction ratio  
- Metadata feature extraction from manifest files  
- TPC‑H benchmark suite  
- Query performance trade‑offs between metadata‑heavy and full‑scan workloads
