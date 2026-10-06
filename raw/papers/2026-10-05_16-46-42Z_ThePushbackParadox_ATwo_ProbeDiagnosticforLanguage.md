---
title: The Pushback Paradox: A Two-Probe Diagnostic for Language Model Compliance
published: 2026-10-05T16:46:42Z
authors: Stefan Bühler, David Exler, Markus Reischl, Mark Schutera
url: http://arxiv.org/abs/2610.06673v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Pushback Paradox: A Two-Probe Diagnostic for Language Model Compliance

## Abstract
Are language models compliant with user instructions? A model that always complies can be stopped but also exploited, while one that always resists can be neither exploited nor stopped. We contribute an open two-probe benchmark that can place any language model on this spectrum. In the active probe, a user instructs the model to act and accept a lower payoff, which measures exploitability. In the passive probe, the user instructs it to wait and give up a higher payoff, which measures stoppability. The two compliance rates combine into a compliance index $κ$. Applied to twelve language models, the benchmark shows that seven mostly follow the instruction in both probes and justify their action by pointing to the instruction. Only Claude Sonnet-4.6 and Claude Opus-4.7 can be stopped without being exploitable, Claude Opus-4.6 and GPT-5-mini resist both instructions, and no model is exploitable but unstoppable. Knowing where a language model sits on the compliance index $κ$ matters for human operators and for multi-agent systems, whether distributed or orchestrated.

## Metadata
- **Published**: 2026-10-05T16:46:42Z
- **Authors**: Stefan Bühler, David Exler, Markus Reischl, Mark Schutera
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.06673v1)