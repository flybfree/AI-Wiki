---
title: When Personal Memory Has No Single Answer: Evaluating LLM Agents under Irreducible Conflict
published: 2026-08-14T03:48:08Z
authors: Lu Yang, Shusheng Xu, Zhuoran Li, Tongkai Yang, Longbo Huang
url: http://arxiv.org/abs/2608.13921v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Personal Memory Has No Single Answer: Evaluating LLM Agents under Irreducible Conflict

## Abstract
LLM agents increasingly maintain personal memory across sessions, but it can conflict. Preferences depend on context, behavior evolves, and sources can conflict. When a query lacks context, time, or source authority to interpret conflict, treating one memory as definitive converts unresolved conflict into an unjustified, overconfident action. Existing benchmarks recover one answer from conflicting evidence, overlooking whether agents recognize underdetermination, preserve alternatives, seek missing information, and choose appropriate actions. We introduce \underline{T}esting \underline{A}gents' \underline{N}avigation of \underline{G}enuine, \underline{L}atent, and \underline{E}ntangled Memory Conflicts (\textsc{TANGLE}), a benchmark for genuinely unresolvable memory conflicts. It comprises 541 instances across 40 personas and three types: Context-Partitioned Conflict (CPC), Behavior-Oscillation Conflict (BOC), and Source-Contradiction Conflict (SCC). We evaluate two tracks---an oracle track with curated memory and a pipeline track that extracts memory from multi-session dialogues---on five dimensions: conflict perception, causal reasoning, confidence calibration, clarification seeking, and memory faithfulness. Experiments reveal pipeline challenges. With curated memory, models recognize conflicts more reliably than they calibrate actions or seek targeted clarification. With end-to-end pipeline memory, extraction fails to preserve conflict-bearing relations needed for downstream reasoning. Policy comparisons show fixed rules are insufficient when actions must reflect conflict. These findings motivate Conflict-Aware Action Policy (CAAP), which adapts actions to each conflict using available evidence. \textsc{TANGLE} frames conflict handling as recognizing underdetermination, retaining conflicting evidence, and acting without forcing a definitive answer.

## Metadata
- **Published**: 2026-08-14T03:48:08Z
- **Authors**: Lu Yang, Shusheng Xu, Zhuoran Li, Tongkai Yang, Longbo Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13921v1)