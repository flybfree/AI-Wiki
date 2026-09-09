---
title: A Layered Analysis of Disagreement And Answer Quality in Multi-Agent LLM Debate
published: 2026-09-07T21:57:44Z
authors: Chen Qian
url: http://arxiv.org/abs/2609.08016v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Layered Analysis of Disagreement And Answer Quality in Multi-Agent LLM Debate

## Abstract
Multi-agent debate, in which several LLMs exchange arguments before answering, is widely assumed to improve answer quality by surfacing genuine disagreement. That mechanism is rarely checked. We introduce four measurements: (A) the agreement a debater reports; (B) whether its reply text actually pushes back; (C) whether the position persists once the eliciting instruction is removed; and (D) for open-weight models, the stance response in the debater's own token log-probabilities. We evaluate three-model committees debating open-ended GlobalOpinionQA across 750 debates under three tones: friendly (seek common ground), neutral, and hostile (stress-test every position). (A) Tone strongly reshapes reported agreement: full agreement differs by 50.4 percentage points between the friendly and hostile endpoints. (B) A judge that reads only the reply text, never the self-report or the condition, recovers the same pattern. (C) The dissent appears partly tied to the instruction that elicited it: labels revert toward agreement 23.1 points more often after deleting the hostile instruction than under a matched re-ask that keeps it; question-weighted inference is inconclusive on first-round turns alone (p=0.0625), significant pooling all rounds (p=0.016), and only 11/28 first-round reversions also appear in the reply text. (D) Opposing arguments weaken a debater's stance margin more consistently than they shift its direction. For final answers we detect no quality gain: a bias-checked jury returns 299/299 ties (ruling out only large differences), accuracy on a verifiable control task is unchanged, and a jury without the bias check had declared debate the winner 66% of the time -- an artifact of reading order. Taken together, LLM debate readily changes what agents say, but we find much weaker evidence that it changes what they persistently endorse or improves the quality of the final answer.

## Metadata
- **Published**: 2026-09-07T21:57:44Z
- **Authors**: Chen Qian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08016v1)