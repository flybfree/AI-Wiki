# Summary: 2026-08-06_11-07-42Z_CodeGrep_AnRL_TrainedRetrievalAgentforLLMCodingAge.md
Saved: 2026-08-06 20:39
Source: 2026-08-06_11-07-42Z_CodeGrep_AnRL_TrainedRetrievalAgentforLLMCodingAge.md
Model: None

---

## Summary  
CodeGrep is an RL‑trained retrieval agent that tackles the inefficiency of LLM coding agents, which waste tokens searching for files to patch rather than performing the actual edits. By training a 14B model end‑to‑end with GRPO to issue parallel grep, glob and read tool calls, CodeGrep returns candidate files to a frozen downstream coding agent, thereby reducing round and token consumption while preserving resolution rates.

## Key Contributions  
- **CodeGrep**, an RL‑trained retrieval system that cuts token usage for file‑finding tasks in LLM agents.  
- An end‑to‑end training pipeline where the 14B model uses GRPO to issue multi‑turn parallel grep/glob/read calls and selects candidates based on precision thresholds.  
- Demonstration that applying efficiency signals at the advantage layer improves downstream utility and reduces KL drift compared with reward‑layer placement.

## Methodology  
The authors mine supervision from 67 K open‑source agent trajectories using CATM to build a Git‑worktree environment for multi‑turn reinforcement learning. CodeGrep is trained end‑to‑end: the RL agent issues parallel file‑search tool calls, evaluates candidate files against precision thresholds (e.g., 0.375, 0.445, 0.677), and returns the selected set to a frozen downstream coding model. The efficiency signal is injected at the advantage layer rather than the reward layer to keep KL divergence low.

## Results  
On all 500 SWE‑Bench Verified instances, CodeGrep maintains the resolve rate (27.0 % vs 25.8 % baseline) while achieving 15 % fewer rounds and 19 % fewer tokens on resolved issues. Retrieval precision thresholds show BM25 at p=0.375 degrades performance, Jina at p=0.445 is neutral, and CodeGrep at p=0.677 reduces rollout cost.

## Significance  
This work resolves a major bottleneck in LLM coding agents—inefficient file retrieval—by introducing an RL‑trained component that directly optimizes token usage without sacrificing resolution rates, leading to faster, cheaper code‑generation pipelines.

## Related Concepts  
- Retrieval‑Augmented Generation (RAG) for LLMs.  
- Gradient Policy Optimization (GRPO).  
- Multi‑turn tool calls in Git‑worktree environments.  
- Precision thresholds in information retrieval.  
- KL divergence control via advantage‑layer signal injection.
