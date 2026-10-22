---
title: Real PMIDs, Wrong Papers: Harness Design for Biomedical Claim-Verification Agents
url: http://arxiv.org/abs/2610.29812v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-21_14-35-56Z_RealPMIDs_WrongPapers_HarnessDesignforBiomedicalCl.md
generated_at: 2026-10-21 23:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a controlled ablation study comparing four different harness architectures for biomedical claim-verification agents using the SciFact dataset and the live PubMed API as the sole retrieval tool. The central finding is that retrieval quality, not reasoning capability, is the dominant bottleneck in these systems, and that closed-book language models produce citations that are almost always real PubMed IDs but almost never relevant to the claim being verified.

## Key Takeaways
- Naive single-shot retrieval, where the claim text is used directly as a PubMed query, retrieves the gold paper for only 6% of claims and converts overconfident errors into abstentions without improving accuracy. In contrast, allowing the agent to formulate its own search queries (a ReAct-style approach) triples gold recall and achieves the best verdict accuracy at 62%, compared to 49–59% for other realistic harnesses, though these differences are not statistically significant at the sample size used and agents consume fewer than half their search budget.
- When models are given the gold abstracts directly (an oracle condition), accuracy jumps to 79–86%, revealing a significant 17–24 point gap that isolates retrieval as the primary failure mode rather than reasoning or output formatting. This finding holds across two different efficient-frontier backbone models, suggesting the bottleneck is architectural rather than model-specific.
- A citation audit reveals a critical safety gap: closed-book models generate PubMed IDs that almost always exist (327 out of 335), but a cross-family LLM judge rates only 3 of those 327 as actually relevant to the claim, versus 67% relevance for citations produced by the search agent. This demonstrates that verifying a citation's existence is a wholly insufficient safeguard for scientific agents, since plausible-looking but irrelevant references can masquerade as grounded evidence.

## Context
This work addresses a growing gap in the evaluation of agentic AI systems deployed in scientific and medical domains. As literature-searching language agents become standard components of scientific assistants for the life sciences, practitioners lack controlled evidence about which architectural choices in the tool-use harness actually matter. By holding the backbone model and output format fixed while varying only the retrieval strategy, the paper provides a clean experimental design that isolates harness effects from model capability, a methodological contribution that is largely absent from existing agentic AI literature.

## Implications
For practitioners building biomedical or scientific claim-verification systems, the findings argue strongly against naive query construction and in favor of agent-driven query formulation, while also warning that existence checks on citations provide a false sense of grounding. For the broader AI safety and reliability community, the citation audit exposes a failure mode where models produce convincing but irrelevant references that would pass superficial validation, suggesting that evaluation pipelines for scientific agents must incorporate relevance-based citation auditing rather than relying on identifier existence alone. The authors' release of code, prompts, and cached tool calls supports reproducibility and gives the community a concrete benchmark for testing future harness designs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29812v1)
