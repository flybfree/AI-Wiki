---
title: When Evidence Changes: Evaluating Memory Repair and Re-reading in Language-Model Agents
url: http://arxiv.org/abs/2610.03902v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-02_18-13-29Z_WhenEvidenceChanges_EvaluatingMemoryRepairandRe_re.md
generated_at: 2026-10-05 22:08
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether language-model agents should repair their stored memory or simply re-read source documents when supporting evidence is revoked or replaced. Using medication- and problem-list extraction tasks drawn from public ICU records, the author benchmarks multiple memory-management strategies—including caching, rebuilding, graph-local repair, full re-reading, and source-filtered re-reading—across two 7B-parameter models. The central finding is that while local repair dramatically reduces revision token costs on short records, every memory pipeline still costs at least twice as much as full re-reading in held-out conditions, and source-filtered re-reading consistently emerges as the cheapest strategy across all tested scenarios.

## Key Takeaways
- On short records, graph-local repair consumes 5 to 10 times fewer revision tokens than full memory rebuilding, yet the total pipeline cost (ingest plus revision plus every downstream use) still exceeds full re-reading by at least a factor of two, meaning the apparent efficiency of targeted repair is offset by hidden overhead in the complete workflow.
- When records are extended to roughly 10,000 tokens by adding task-ineligible documents, memory-based pipelines can become cheaper than full re-reading after only 2 to 14 uses, partly because truncated extraction limits the amount of text processed per query; however, source-filtered re-reading—reading only the relevant source documents rather than the entire record—remains the lowest-cost option even at this scale.
- In the evidence-replacement study, none of the four primary confirmatory statistical tests reached significance, indicating that the proposed memory-repair mechanisms did not produce reliably measurable improvements over simpler re-reading baselines, and the author explicitly argues that any future evaluation of agent memory after evidence revision must be benchmarked against source-filtered re-reading across the full pipeline rather than against naive full re-reading alone.

## Context
As language-model agents increasingly rely on persistent memory stores to accumulate derived facts over long interactions, the question of how to handle evidence that is later corrected, revoked, or replaced becomes critical for safety-critical deployments such as clinical decision support. This paper addresses a gap in the evaluation literature: most prior work measures memory performance under static conditions, ignoring the operational reality that source documents change over time. By framing the comparison around the full cost pipeline—including ingestion, revision, and every subsequent use—the work challenges the assumption that maintaining a repaired memory store is inherently more efficient than simply re-reading filtered sources.

## Implications
For practitioners building agentic systems in healthcare, legal review, or any domain where source documents are updated, this work suggests that investing in sophisticated memory-repair infrastructure may not yield net cost savings once the complete pipeline is accounted for, and that a simpler source-filtered re-reading strategy should serve as the default baseline. For the research community, the failure of all four confirmatory tests in the replacement study signals that current memory-repair techniques lack robust statistical support, and future evaluations must adopt source-filtered re-reading as the standard comparator to avoid overstating the benefits of memory architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03902v1)
