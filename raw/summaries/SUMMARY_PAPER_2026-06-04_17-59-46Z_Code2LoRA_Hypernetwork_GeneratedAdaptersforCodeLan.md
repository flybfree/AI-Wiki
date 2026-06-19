---

title: "Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution"
url: http://arxiv.org/abs/2606.06492v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-04_17-59-46Z_Code2LoRA_Hypernetwork_GeneratedAdaptersforCodeLan.md
generated_at: "2026-06-11 10:53"
model: nvidia/nemotron-3-nano-4b

---


## Summary  
Code2LoRA introduces a hypernetwork framework that creates repository‑specific LoRA adapters for code language models, injecting repository knowledge without any inference‑time token overhead. On static tasks it reaches 63.8% cross‑repo and 66.2% in‑repo exact match, matching the per‑repository LoRA upper bound; on evolving tasks Code2LoRA‑Evo achieves 60.3% cross‑repo exact match, a gain of +5.2 percentage points over a single shared LoRA.

## Key Takeaways  
- Code2LoRA‑Static converts a single repository snapshot into an adapter with zero inference‑time token overhead.  
- It matches the per‑repository LoRA upper bound on static tasks (63.8% cross‑repo, 66.2% in‑repo).  
- Code2LoRA‑Evo maintains an adapter backed by a GRU hidden state updated per code diff, delivering +5.2 pp over a single shared LoRA on evolving tasks.

## Context  
Code language models require repository‑level context to resolve imports and APIs, yet existing methods rely on long inputs or costly per‑repository fine‑tuning that become brittle as code evolves. This paper presents an efficient hypernetwork approach that sidesteps these limitations.

## Implications  
The method enables scalable, cost‑effective adaptation for both stable and evolving codebases, reducing the expense of repository‑specific training. Practitioners can adopt Code2LoRA to maintain high performance without retraining full models on each commit.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.06492v1)
