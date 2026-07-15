title: "Summary: 2026-07-01_17-50-48Z_ArePerformance_OptimizationBenchmarksReliablyMeasu.md"
# Summary: 2026-07-01_17-50-48Z_ArePerformance_OptimizationBenchmarksReliablyMeasu.md
Saved: 2026-07-01 23:01
Source: 2026-07-01_17-50-48Z_ArePerformance_OptimizationBenchmarksReliablyMeasu.md
Model: None

---


## Summary  
The paper critiques repository‑level performance‑optimization benchmarks—GSO, SWE‑Perf, and SWE‑efficiency—that rank coding agents by applying patches to real repositories and measuring runtime improvements. It argues that these leaderboard scores can be misleading because many reference patches are not reproducible across machines, some violate original validity rules, and the scoring rules inflate certain tasks or ignore others. The authors audit three benchmarks on 740 optimization tasks spread across four Google Cloud machine types to expose these problems. Their findings suggest that aggregate rankings hide important per‑task performance gaps.

## Key Contributions  
- [Finding 1] Only a minority of GSO (39/102), SWE‑Perf (11/140) and SWE‑efficiency (411/498) reference patches satisfy the original benchmark validity rules when replayed across machines.  
- [Finding 2] Public submission rankings diverge; eight shared submissions have nine pairwise disagreements, and SWE‑efficiency’s scoring rule assigns extreme weight to ten tasks (58.5%–82.8%).  
- [Finding 3] For each task, at least one public submission matches or beats the reference patch on 85.3% of replay‑valid GSO and SWE‑efficiency tasks and beats unoptimized base code on 99.8%.

## Methodology  
The authors systematically replay official patches on four Google Cloud machine types to test reproducibility, compare benchmark scores under different scoring rules, and collect public submissions for each task. They compute per‑task contributions by evaluating how often a submission improves or matches the reference patch relative to an unoptimized baseline.

## Results  
Replay validity holds for most tasks but reference patches are invalid in many cases; SWE‑Perf is especially fragile with near‑zero runtime changes. Leaderboard rankings differ across submissions, and high per‑task performance is achievable—85.3% of replay‑valid GSO and SWE‑efficiency tasks have a submission that matches or exceeds the reference patch.

## Significance  
This work reveals hidden flaws in benchmark scores, encourages more reliable evaluation metrics, and highlights gaps that aggregate leaderboards mask, thereby guiding future research toward transparent, reproducible coding‑agent performance measurement.

## Related Concepts  
benchmark validity, replayability, scoring rule bias, aggregation vs. per‑task analysis, code optimization agents, repository patches.
