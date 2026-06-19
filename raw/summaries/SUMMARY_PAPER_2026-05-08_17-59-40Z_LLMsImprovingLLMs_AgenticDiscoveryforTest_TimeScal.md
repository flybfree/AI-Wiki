---

title: "LLMs Improving LLMs: Agentic Discovery for Test-Time Scaling"
url: http://arxiv.org/abs/2605.08083v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-08_17-59-40Z_LLMsImprovingLLMs_AgenticDiscoveryforTest_TimeScal.md
generated_at: "2026-06-11 10:31"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces AutoTTS, an environment‑driven framework that automatically discovers test‑time scaling (TTS) strategies instead of relying on manual design. Experiments show the discovered strategies improve accuracy‑cost tradeoffs over strong handcrafted baselines and generalize across benchmarks and model scales while the entire discovery process costs only $39.9 and 160 minutes.

## Key Takeaways
- AutoTTS replaces individual TTS heuristics with an automated search environment that constructs a tractable control space for strategy discovery.
- The width‑depth TTS problem is reframed as controller synthesis over pre‑collected reasoning trajectories and probe signals, allowing cheap evaluation without repeated LLM calls.
- The entire discovery effort costs $39.9 and 160 minutes, and the learned strategies generalize to held‑out benchmarks and model scales.

## Context
Test‑time scaling is a key technique for boosting large language model performance, yet current approaches depend on intuition‑driven heuristics that limit exploration of the computational allocation space. This work advances AI research by demonstrating how automated discovery can uncover effective TTS policies without exhaustive manual tuning.

## Implications
For researchers and practitioners, AutoTTS offers a scalable way to enhance LLM inference without costly iterative design cycles. The open‑source implementation lowers barriers to entry, encouraging broader adoption of test‑time scaling across the industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.08083v1)
