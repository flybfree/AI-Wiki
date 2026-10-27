---
title: Position, Role or Label? A Controlled Study of Instruction Conflicts in LLM Agents
published: 2026-10-23T18:48:27Z
authors: Anish Laddha, Nitesh Pradhan, Gaurav Srivastava
url: http://arxiv.org/abs/2610.33201v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Position, Role or Label? A Controlled Study of Instruction Conflicts in LLM Agents

## Abstract
LLM agents take instructions from the operator, repository configuration, user, tool results and saved memory, which often conflict. Instruction-hierarchy benchmarks ask whether the higher-ranked source wins, but a source sets position, role and label at once. First, we build WhoWins, 1,080 code-scored scenarios in five task types, each with up to five mutually exclusive instructions, and seven controlled experiments that vary only how instructions are delivered. Second, we study 14 open-weight models (0.6B to 122B, thinking off and on) over 1,887,356 scored replies, checking main findings on held-out scenarios. Inside one message the first of two conflicting lines wins 72.42 to 94.66%, and across messages it keeps 22.95 to 62.65%. A policy sent first in the system (or developer) message loses most conflicts with later lines in every Qwen model but wins most on gpt-oss when it acts. In tool and file-write tasks it wins less often than the same text sent first as a labelled user message, in every model-mode. Third, we test whether pairs forecast larger conflicts; forecasts improve in every model-mode once they know where the task line is. Finally, by our keyword patterns at most 2.92% of decided pair replies flag or hedge a conflict.

## Metadata
- **Published**: 2026-10-23T18:48:27Z
- **Authors**: Anish Laddha, Nitesh Pradhan, Gaurav Srivastava
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33201v1)