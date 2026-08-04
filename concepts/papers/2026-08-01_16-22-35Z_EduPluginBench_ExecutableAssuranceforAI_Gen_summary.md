# Summary: 2026-08-01_16-22-35Z_EduPluginBench_ExecutableAssuranceforAI_GeneratedE.md
Saved: 2026-08-03 21:28
Source: 2026-08-01_16-22-35Z_EduPluginBench_ExecutableAssuranceforAI_GeneratedE.md
Model: None

---

## Summary  
This paper introduces EduPluginBench, an executable benchmark that evaluates AI‑generated educational plugins for compliance with a suite of security and governance constraints such as least privilege, telemetry consent, provenance, privileged‑write authority, lifecycle constraints, and bounded failure. The authors propose a staged admission protocol (P0–P4) that progressively checks functional correctness while enforcing these constraints, thereby providing a concrete measure of “executable assurance.” Their contribution is both the benchmark itself—validated across 1,440 activation‑checked mutants from 30 specifications—and the empirical findings that demonstrate how this framework improves defect recall and clarifies the limits of controlled contract consistency.  

## Key Contributions  
- [Finding 1] P0–P4 increased release‑blocking‑defect recall by 74.7 percentage points (specification‑clustered 95 % CI 73.4–75.8) over the baseline P0–P2, showing a substantial boost in defect detection when full compliance is enforced.  
- [Finding 2] In a frozen transfer study of 600 unmodified generations from two current coding models, 300 were parsed but none passed P0 or achieved any level of P0‑P4 conformance (95 % upper bound 0.64%); downstream assurance estimands remained undefined.  
- [Finding 3] Negative transfer results—such as the Moodle study retaining only 16 vulnerable/fixed pairs and the generic PHP detector finding no vulnerabilities—prevent the interpretation of controlled contract consistency as independent proof of real‑defect effectiveness.  

## Methodology  
The authors built EduPluginBench by creating a set of activation‑checked first‑order mutants (P0–P4) derived from 30 educational specifications, each representing a distinct class of constraints. They then staged admission: P0 checks basic executable integrity, while higher levels enforce least‑privilege execution, telemetry consent, provenance verification, privileged‑write authority, lifecycle constraints, and bounded failure handling. The benchmark was evaluated on 1,440 mutants across specifications, supplemented by a Moodle study of real plugin deployments and a frozen generic PHP detector that examined 600 unmodified generations. Bounded repair analyses were also performed to assess the impact of post‑hoc fixes on conformance. All artifacts—protocols, provenance records, raw generation logs, row‑level decisions, audit trails, analysis code, and reproduction instructions—are publicly available.  

## Results  
The primary experimental result is a 74.7 pp increase in recall for release‑blocking defects when P0–P4 are enforced compared with the weaker P0–P2 baseline (95 % CI 73.4–75.8). No clean reference plugins were rejected, indicating that the benchmark does not over‑penalize correct code. In contrast, frozen transfers show a very low pass rate: only 300 of 600 parsed generations meet P0, and none achieve any higher conformance level (95 % upper bound 0.64%). This suggests that downstream assurance estimands are undefined for the vast majority of generated plugins. A negative transfer study retained 16 vulnerable/fixed pairs, while an earlier diagnostic on 540 generations found 112 P0 passes—all nonconforming—showing a recall jump from 13.4 % to 100 %. The artifact retains full provenance and reproducibility instructions, enabling independent verification.  

## Significance  
EduPluginBench provides the first systematic, executable measure of how AI‑generated educational plugins satisfy complex governance constraints, bridging the gap between theoretical safety guarantees and practical deployment. By quantifying recall improvements and exposing the limits of controlled contract consistency, it informs developers and regulators about the reliability of bounded repair techniques and the need for stricter admission protocols. The findings also highlight that negative transfer studies are essential to avoid mistaking low false‑positive rates as evidence of real‑world effectiveness.  

## Related Concepts  
executable assurance, least privilege, telemetry consent, provenance, lifecycle constraints, bounded failure, contract consistency, staged admission (P0–P4), activation‑checked mutants, bounded repair, negative transfer studies, defect recall, release‑blocking defects.
