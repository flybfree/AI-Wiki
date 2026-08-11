# Summary: 2026-08-08_06-12-18Z_MetadataReconstructionfromValuesAlone_RecoveringCo.md
Saved: 2026-08-10 22:50
Source: 2026-08-08_06-12-18Z_MetadataReconstructionfromValuesAlone_RecoveringCo.md
Model: None

---

## Summary  
The paper tackles the problem of reconstructing column semantics in undocumented data warehouses where identifiers are cryptic or missing. By embedding a language model inside a verification harness that extracts deterministic evidence from raw values, the authors propose a system called Rosetta that can recover meaningful metadata and abstain when uncertain. Their work demonstrates that this hybrid approach improves both coverage and accuracy compared to using the model directly on undocumented data.

## Key Contributions  
- [Finding 1] The verification harness extracts structural evidence—value fingerprints, a 26‑pattern library, and checksum verdicts—to condition a language model’s semantic proposals.  
- [Finding 2] Compared to a direct model application, the harness achieves 0.475 accuracy on 42 % of columns it commits to versus 0.223 for the same model without evidence, with a coverage boost of +0.257.  
- [Finding 3] The deterministic layer acts as a competence detector: it decides whether to speak (coverage) but does not amplify the model’s prose quality; abstention is correctly applied at query time.

## Methodology  
Rosetta places a language model inside a verification harness that functions as a deterministic profiler. The profiler scans each column, generates evidence such as value fingerprints and pattern matches, then feeds this evidence to the model which proposes semantics with provenance tags and confidence scores bounded by the evidence class. A code‑enforced commit gate records predictions first; only when both evidence exists and the gate permits does the system output a metadata fact.

## Results  
Across 680 paired columns in eleven BIRD databases, identifiers destroyed, the harness delivers metadata that is 0.475 accurate on the 42 % of columns it commits to, versus 0.223 for the model alone. On the 283 columns where both arms speak, the harness writes no better prose than the model itself; its gain is selection, not improvement. In a blind i2b2 clinical warehouse, Rosetta decodes 95.5 % of real ICD‑9 codes from values alone and abstains on all 44 NDC drug codes. The catalog supports calibrated abstention at query time: under full schema opacity a naive translator falls from 0.92 to 0.42 execution accuracy, while our gate answers at 86 % accuracy over 59 % coverage.

## Significance  
The work provides a practical solution for production warehouses where documentation is absent or unreliable, enabling reliable data translation and reducing downstream errors. By separating evidence‑driven decision making from model output, the system offers calibrated confidence and avoids hallucinated metadata.

## Related Concepts  
value fingerprints, pattern library, checksum verdicts, language model verification harness, deterministic profiler, evidence class, abstention, schema opacity, code‑enforced commit gate, provenance, BIRD databases.
