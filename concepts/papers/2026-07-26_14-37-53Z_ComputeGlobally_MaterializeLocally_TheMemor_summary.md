# Summary: 2026-07-26_14-37-53Z_ComputeGlobally_MaterializeLocally_TheMemoryContra.md
Saved: 2026-07-27 23:55
Source: 2026-07-26_14-37-53Z_ComputeGlobally_MaterializeLocally_TheMemoryContra.md
Model: None

---

## Summary  
The paper investigates how long‑horizon language agents can reuse their KV cache as a form of memory, questioning whether retained events remain useful when the observations that generated them are evicted. It demonstrates “semantic materialization”: a downstream event’s cached rows can act as an independently servable view of computation even after its source observation is gone. The authors also show that purposeful phrasing of answer‑free events dramatically improves recovery performance, whereas passive harvesting yields no benefit. This work establishes a memory contract for sparse event‑KV serving—what to write, where it lands, and what survives once the original input disappears.

## Key Contributions  
- [Finding 1] A retained event can still be informative even after its originating observation is evicted from the KV cache, indicating that downstream events carry a bounded semantic payload.  
- [Finding 2] Deliberately phrasing an answer‑free event raises donor‑aligned recovery accuracy from 6 % to 51 % on Qwen3‑8B, proving that phrasing can encode recoverable information without naming the value.  
- [Finding 3] The survival of compact state degrades toward chance for larger payloads, and two equally understood phrasings can produce divergent outcomes, revealing that meaning alone does not guarantee stable memory.

## Methodology  
The authors construct long‑horizon agent simulations where a subset of KV cache entries is kept while others are evicted. They compare three scenarios: (1) omitting an earlier observation and observing whether the downstream event’s answer follows the omitted value, (2) deliberately crafting an answer‑free event with donor‑aligned phrasing, and (3) harvesting natural mentions from long‑term dialogue without intentional framing. By varying payload size and phrasing, they measure accuracy loss, recovery rate, and the stability of cached rows.

## Results  
Experiments show that when a source observation is removed, answers aligned with it are still correct in most cases, confirming semantic materialization. Deliberate answer‑free events improve donor alignment from 6 % to 51 %, whereas passive harvesting yields no detectable gain (≈0 %). Larger payloads (>20 tokens) exhibit near‑random accuracy, and two different phrasings that the model understands equally well produce opposite outcomes with high variance. These findings quantify the memory contract: what is written, where it lands in the cache, and what persists after eviction.

## Significance  
Understanding this memory contract matters because agents increasingly rely on KV caches to reduce compute cost; if retained events lose meaning after source eviction, long‑horizon training may waste resources. The paper’s demonstration that phrasing can encode recoverable information offers a principled way to design sparse event‑KV serving strategies, potentially improving efficiency and reliability without sacrificing performance.

## Related Concepts  
- KV cache (key‑value memory) in transformer models  
- Event‑based memory or “event‑KV” representation  
- Long‑horizon agents and episodic memory  
- Eviction policies for sparse caches  
- Semantic materialization of downstream events  
- Donor alignment and recovery accuracy
