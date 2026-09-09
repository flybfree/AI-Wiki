---
title: SerenAI: State-transition system inspired by text-based world AI models
published: 2026-09-06T14:57:18Z
authors: Elvin Babayev, Artem Sinitsa, Arash Hajisharifi, Kabir Bakhshaei
url: http://arxiv.org/abs/2609.06647v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SerenAI: State-transition system inspired by text-based world AI models

## Abstract
Although professional workflows leverage large language models widely, the interpretation for auditing unconstrained free-text generation is usually intractable if such generation demands legal, operational or financial workflow. We hereby demonstrate a text based system called SerenAI - inspired by world-models, it is a state transition system that outputs verifiable predictions rather than merely text: Provided with a description of the environment, state, and actions, the generated output contains 4 items: causal deltas that causally effect the given state, a next state that can logically follow from the given state and action, a validity reward, and a termination signal. For the released proto-model, we employ 2 steps of adaptation training, namely parameter efficient fine-tuning followed by verifier based RL over 50,000 exampled cause and effects in 12 environments spanning 10 reasoning domains. Compared to an initial internal evaluation of an 8B open-weight baseline, SerenAI increased JSON validity from 85.0% to 93.2%, schema validity from 55.0% to 84.0%, exact structured-output match from 0.0% to 41.5%, causal-delta exact match from 0.0% to 41.5%, resulting-state exact match from 0.0% to 42.0%, reward exact match from 1.0% to 80.5%, and termination exact match from 38.0% to 81.5%. These support the narrower claim that verifier-compatible adaptation can improve structured transition prediction. They do not yet establish legal-grade reliability. Accordingly, the paper also specifies a validation protocol for evidence-grounded legal workflows, calibration, human oversight, and sovereign on-premise deployment.

## Metadata
- **Published**: 2026-09-06T14:57:18Z
- **Authors**: Elvin Babayev, Artem Sinitsa, Arash Hajisharifi, Kabir Bakhshaei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.06647v1)