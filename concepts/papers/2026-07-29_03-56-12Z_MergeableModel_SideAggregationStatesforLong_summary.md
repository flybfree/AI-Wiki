# Summary: 2026-07-29_03-56-12Z_MergeableModel_SideAggregationStatesforLong_Contex.md
Saved: 2026-07-29 20:22
Source: 2026-07-29_03-56-12Z_MergeableModel_SideAggregationStatesforLong_Contex.md
Model: None

---

## Summary  
Long‑context language models struggle with non‑additive set‑based aggregations such as cardinality estimation, set relationships, and grouped statistics because their performance degrades as context length grows. To address this limitation, the authors propose a model‑side aggregation interface that maintains compact Hash‑based HyperLogLog (HLL) sketch states alongside a frozen language model. The interface extracts canonical identities from each relevant record, hashes them, and updates the HLL state without invoking an additional generate‑execute‑return cycle. Crucially, these states can be merged across context segments or read out directly for downstream reasoning, keeping memory usage constant regardless of set size.

## Key Contributions  
- [Finding 1] The authors introduce a mergeable model‑side aggregation interface that uses HLL sketch states of fixed size (2 KiB) to perform set‑based aggregations in long contexts.  
- [Finding 2] Validation on one million records shows a mean relative error of only 1.6% for distinct‑count estimation, with the method achieving 99.2 % accuracy versus 100 % exact aggregation on Gemma‑4 (31B).  
- [Finding 3] The approach improves over chain‑of‑thought reasoning by 60.9 points on Qwen and 56.3 points on Gemma, demonstrating substantial gains in set‑aware tasks.

## Methodology  
The model processes the input while an extractor maps each record to a canonical identity; this identity is hashed and used to update a Hash‑based HyperLogLog sketch state stored separately from the frozen language model. Because the HLL state size (2048 registers) does not depend on context length or set cardinality, merging multiple segment states yields an exact readout equivalent to a single pass over the stream. This design eliminates the need for repeated generation‑execution cycles and preserves a fixed budget of memory.

## Results  
The fixed‑budget interface was tested across 3,969 aggregate‑then‑reason tasks from 174 source windows on Gemma 4 (31B, BF16), reaching 99.2 % accuracy—0.8 percentage points below the exact aggregation baseline (95 % CI: 0.5–1.3). On a Qwen benchmark, it improved over full‑context reasoning by 63.2 points and over chain‑of‑thought by 60.9 points. In an Oolong‑Synth subset of 1,200 tasks, the method achieved 91.1 % on Qwen and 99.3 % on Gemma.

## Significance  
This work enables long‑context language models to handle set‑based aggregations with constant memory overhead, reducing reliance on costly generate‑execute‑return loops. By providing a mergeable HLL state that can be read out directly, the approach improves both accuracy and efficiency for tasks involving logs, tables, multi‑turn conversations, and any scenario where exact set statistics are required.

## Related Concepts  
Hash‑based HyperLogLog (HLL), canonical identity extraction, model‑side aggregation interface, mergeable sketch states, fixed‑budget inference, long‑context language models, set‑based aggregation, cardinality estimation.
