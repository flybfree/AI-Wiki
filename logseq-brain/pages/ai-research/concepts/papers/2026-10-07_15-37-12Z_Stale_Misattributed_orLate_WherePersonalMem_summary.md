# Summary: 2026-10-07_15-37-12Z_Stale_Misattributed_orLate_WherePersonalMemoryFail.md
Saved: 2026-10-07 23:18
Source: 2026-10-07_15-37-12Z_Stale_Misattributed_orLate_WherePersonalMemoryFail.md
Original paper: [arXiv:2610.10265](https://arxiv.org/abs/2610.10265)
Model: None

---

## Summary
This paper investigates the hidden failures in personal memory systems for language agents, arguing that final answer accuracy obscures critical errors occurring before text generation. The authors introduce a framework to directly measure pre-generation failures, specifically focusing on stale data, misattribution, and latency issues. By utilizing Personal Fact Memory (PFM) as a reference layer, the study demonstrates that temporal validity is largely determined by memory construction rather than retrieval alone. The work advocates for a shift in evaluation metrics, separating stored-state validity, identity resolution, and serving latency to better understand agent memory performance.

## Key Contributions
- The study reveals that without proper update resolution, 70.3% of prompts expose superseded or stale values, highlighting that temporal validity is primarily a property of memory construction.
- It demonstrates that while participant-aware BM25 can match reference rankers when sharing an active store, the harder challenge lies in assigning revisions to the correct memory slots, where false merges silently remove current values.
- The paper shows that LLM-based key assigners achieve higher key recall than rule extractors but result in lower clean-retrieval rates, and that open-domain merge recall remains extremely low (never exceeding 0.062) on benchmarks like LongMemEval.

## Methodology
The authors approach the problem by using Personal Fact Memory (PFM) as a controlled reference layer to isolate and measure specific failure modes in agent memory. They employ a controlled revision benchmark to test temporal validity, comparing scenarios with and without update resolution. To address identity resolution, they evaluate various key assigners, including rule-based extractors and four different LLM-based assigners, measuring their impact on key recall and clean-retrieval rates. Additionally, they test participant-aware BM25 against reference rankers within a prespecified margin. The methodology also involves analyzing entity posteriors to mitigate same-name exposure and measuring retrieval latency versus prompt prefill time on specific hardware to understand serving bottlenecks.

## Results
The experiments show that serving only the active value of correctly keyed slots eliminates stale exposure, whereas the lack of update resolution leads to a 70.3% rate of exposing superseded values. In terms of retrieval, participant-aware BM25 is equivalent to the reference ranker when both share the same active store and participant information. However, identity resolution remains a significant bottleneck; LLM key assigners improve key recall but degrade clean-retrieval performance due to false merges. Misattribution persists even after validity filtering, as entity posteriors fail to distinguish identically named speakers in complex datasets like LoCoMo. Furthermore, two frozen language models were found to reproduce prompt errors in their generated text, and while retrieval latency varies by ranker, prompt prefill time dominates the overall turn-level latency.

## Significance
This research is significant because it challenges the prevailing metric of judging agent memory solely by final answer correctness. By exposing pre-generation failures such as stale data and misattribution, the paper argues for a more granular evaluation framework. This shift is crucial for developing reliable personal agents, as it highlights that high-quality retrieval is insufficient if the underlying memory state is invalid or if identity resolution fails. The findings suggest that improving agent reliability requires focusing on memory construction, update mechanisms, and identity disambiguation rather than just optimizing retrieval algorithms.

## Related Concepts
- Personal Fact Memory (PFM)
- Temporal Validity
- Stale Exposure
- Identity Resolution
- Key Assigners
- BM25 Retrieval
- LongMemEval
- LoCoMo
- Prompt Prefill
- Memory Construction
