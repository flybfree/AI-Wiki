---

title: "Summary: LongMemEval-V2: Evaluating Long-Term Agent Memory Toward Experienced Colleagues"
url: http://arxiv.org/abs/2605.12493v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-12_17-59-34Z_LongMemEval_V2_EvaluatingLong_TermAgentMemoryTowar.md
generated_at: "2026-06-11 10:39"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-05-12 17-59-34Z Longmemeval V2 Evaluatinglong Termagentmemorytowar


## Summary
The paper introduces LongMemEval-V2, a benchmark for evaluating long-term memory in web agents, and demonstrates that AgentRunbook-C achieves the highest accuracy at 72.5% while outperforming RAG baselines. The results highlight a strong trade‑off between performance and latency.

## Key Takeaways
- LME‑V2 contains 451 manually curated questions covering static state recall, dynamic state tracking, workflow knowledge, environment gotchas, and premise awareness, using up to 500 trajectories and 115 million tokens.  
- AgentRunbook‑C, a coding‑agent memory method that stores trajectories as files and invokes a sandboxed agent to gather evidence, reaches 72.5% average accuracy, surpassing the strongest RAG baseline at 48.5% and an off‑the‑shelf coding agent at 69.3%.  
- Coding‑agent approaches improve accuracy but incur high latency costs, indicating a clear performance‑speed trade‑off.

## Context
Long‑term memory is essential for agents navigating complex web environments where success depends on recalling state dynamics and workflows. Existing benchmarks often focus on user histories or downstream task outcomes rather than directly measuring whether memory systems internalize environment experience.

## Implications
This benchmark forces researchers to design memory systems that balance accuracy with latency, providing a practical testbed for building knowledgeable colleagues in customized settings. Practitioners can use the findings to prioritize efficient memory strategies over purely high‑accuracy approaches.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.12493v1)
