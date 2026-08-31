---
title: ReToolSQL: Agentic Reinforcement Learning for Robust Text-to-SQL
published: 2026-08-28T00:23:31Z
authors: Pratik Kakkar, Chandra Dhir, Ravi Shankar, Pareekshit Reddy Gaddam, Anup Shirgaonkar
url: http://arxiv.org/abs/2608.27796v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReToolSQL: Agentic Reinforcement Learning for Robust Text-to-SQL

## Abstract
Recent work has shown that reinforcement learning from execution feedback can substantially improve text-to-SQL performance, often enabling smaller models to match or exceed much larger systems. However, most existing approaches treat SQL generation as a single-turn task, limiting the model's ability to recover from errors through iterative refinement. We present ReToolSQL, a two-stage training framework for text-to-SQL that combines (i) a supervised warm-start on rejection-sampled reasoning traces with (ii) agentic reinforcement fine-tuning (RFT) over multi-turn tool-use trajectories. The key insight is that the two stages act on complementary axes, the supervised fine-tuning (SFT) on verified privileged-teacher traces expands the set of solvable questions (raising pass@k coverage on the hardest cases), while RFT converts that expanded capability into higher single-pass accuracy by teaching the model when to verify, what evidence to retrieve, and how to repair faulty SQL from execution feedback. Applied to Gemma 4 instruction-tuned (31B), RFT alone achieves 73.66% execution accuracy (EX) on the BIRD-SQL development benchmark (74.12% EX with self-consistency). Initializing RFT from the SFT checkpoint (SFT$\to$RFT) yields our strongest model at 74.32% EX single-pass and 74.77% EX with self-consistency. At the time of writing, this ranked first on the BIRD single-model development-set leaderboard. The approach uses composite rewards anchored on execution correctness, requires no human annotation beyond the benchmark itself, and operates within a single dense 31B model, showing that a properly designed SFT$\to$RFT pipeline over tool-use trajectories is a practical path toward robust enterprise-grade text-to-SQL.

## Metadata
- **Published**: 2026-08-28T00:23:31Z
- **Authors**: Pratik Kakkar, Chandra Dhir, Ravi Shankar, Pareekshit Reddy Gaddam, Anup Shirgaonkar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27796v1)