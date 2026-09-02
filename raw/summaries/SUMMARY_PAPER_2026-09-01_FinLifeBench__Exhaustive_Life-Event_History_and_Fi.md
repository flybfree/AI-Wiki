---
title: FinLifeBench: Exhaustive Life-Event History and Financial-State Reconstruction from Longitudinal Banking Dialogue
url: http://arxiv.org/abs/2609.01198v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_13-06-27Z_FinLifeBench_ExhaustiveLife_EventHistoryandFinanci.md
generated_at: 2026-09-01 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
FinLifeBench introduces a comprehensive benchmark for reconstructing life‑event histories and financial states from long banking dialogues. The study evaluates 11 large language models on two tasks: recall of every event with its first session and reconstruction of a full 34‑path financial state at checkpoints, using gold standards derived from synthetic trajectories.

## Key Takeaways
- Event‑anchor recall drops sharply as dialogue lengthens, falling from 0.591 at 15 sessions to 0.445 at 300, indicating models lose track of early events even when they can locate evidence later.
- Financial‑state reconstruction often treats superseded or outdated information as current, leading to inaccurate state snapshots despite correct event recall.
- The two tasks show only weak association; high performance on one does not guarantee reliability on the other.

## Context
Longitudinal financial assistants must maintain accurate records across many sessions without explicit prompting. Existing benchmarks focus on short‑term QA or isolated recalls, leaving a gap for models that need to sustain full histories over time.

## Implications
Practitioners should design evaluation protocols that stress both event continuity and state fidelity, as current LLMs excel at evidence retrieval but fail to preserve temporal validity. This highlights the need for architectural improvements that enforce chronological constraints in dialogue processing.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01198v1)
