---
title: Learning Strategies to Break Judges
published: 2026-09-27T17:13:52Z
authors: Guruprerana Shabadi, Aaditya Naik, Rajeev Alur, Mayur Naik
url: http://arxiv.org/abs/2609.33773v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning Strategies to Break Judges

## Abstract
As AI agents surpass human performance, it becomes exceedingly hard for system designers to evaluate them directly and understand their failure modes. Consequently, agents themselves are being deployed extensively to evaluate, judge, and provide feedback on model traces. But this raises an important question: how can we trust the judge? In this work, we propose an agent-guided method to find weaknesses of agentic judges that expose interpretable failure mechanisms. Our method focuses on mathematical reasoning and proceeds in two stages: first, we deploy adversarial agents to mutate a set of sound proofs by introducing errors, attempting to misguide judges---in other words, injecting errors that judges are unable to catch. Then, we distill these attempts into a small set of mutation strategies which allow us to analyze the failure modes of the judges. To ensure that these strategies are not overfit to the initial set of proofs, we evaluate them by applying the mutation strategies to a held-out set of proofs and querying the same judge. We deploy our method on GPT-5.6-sol and Claude Opus 5, paired with their agent orchestrators, Codex and Claude Code, respectively. These are used both as mutators to introduce errors and as judges to evaluate correctness of mathematical reasoning. We find that across all the agentic judges, we are able to distill mutation strategies that consistently bypass their evaluations, thereby enabling us to ascertain actionable failure modes. Our analysis also reveals that judge reliability degrades at the frontier: errors in Olympiad-level proofs or graduate-level mathematical texts are detected more consistently, whereas flaws in research-level manuscripts are more likely to escape detection.

## Metadata
- **Published**: 2026-09-27T17:13:52Z
- **Authors**: Guruprerana Shabadi, Aaditya Naik, Rajeev Alur, Mayur Naik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33773v1)