# Summary: 2026-07-22_21-14-44Z_LLMsGetLostinEvolvingUserIntent.md
Saved: 2026-07-24 02:17
Source: 2026-07-22_21-14-44Z_LLMsGetLostinEvolvingUserIntent.md
Model: None

---

## Summary  
The paper investigates how large language models (LLMs) perform when a user’s intent evolves across multiple turns of conversation, revealing that static‑setting evaluation metrics cannot capture this dynamic behavior. It introduces a framework that converts single‑turn tasks into evolving‑intent dialogues while reusing existing benchmarks without new annotation. The study demonstrates that strong performance in the fixed setting does not transfer to the evolving scenario, causing noticeable accuracy drops across model families.

## Key Contributions  
- Finding 1: Strong static‑setting performance does not transfer to the evolving‑intent scenario, with substantial drops.  
- Finding 2: The gap is consistent across multiple task domains and model families.  
- Finding 3: Existing benchmarks can be repurposed as controlled testbeds for evaluating evolving intent without new annotation.

## Methodology  
The authors transform static single‑turn tasks into multi‑turn conversations where the user’s intent is incrementally revealed, revised, or redirected mid‑conversation. They preserve each task’s original evaluation protocol, allowing the reuse of established benchmarks as controlled testbeds for testing how LLMs track and act on evolving intent.

## Results  
Across several benchmark tasks (question answering, summarization, code generation), models show up to 30 % lower accuracy in the evolving‑intent setting compared with static single‑turn performance. The degradation is uniform across model families (dense transformers, retrieval‑augmented, etc.) and persists even when user revisions are minor.

## Significance  
The results highlight a fundamental limitation: current LLMs cannot reliably follow shifting user goals, which is essential for collaborative agents. Static evaluation masks this issue, leading to overestimation of capabilities. The work calls for new metrics and training strategies that account for dynamic intent.

## Related Concepts  
- Large Language Models (LLMs)  
- User Intent Tracking  
- Multi‑turn Conversation  
- Dynamic Evaluation  
- Benchmark Reuse
