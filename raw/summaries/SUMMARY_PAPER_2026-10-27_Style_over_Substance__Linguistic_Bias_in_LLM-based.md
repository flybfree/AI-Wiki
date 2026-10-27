---
title: Style over Substance? Linguistic Bias in LLM-based Peer Review Copy title
url: http://arxiv.org/abs/2610.35254v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_11-34-31Z_StyleoverSubstance_LinguisticBiasinLLM_basedPeerRe.md
generated_at: 2026-10-27 00:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a controlled experimental framework to investigate whether LLM-based peer reviewers are influenced by linguistic style rather than scientific substance. By systematically rewriting research papers to alter native/non-native English features and high/low-confidence linguistic markers while preserving the underlying scientific content, the authors demonstrate that LLM reviewers systematically reward confident rhetoric independent of actual scientific merit, exposing a critical vulnerability in automated peer review systems.

## Key Takeaways
- The authors construct fine-grained rewriting instructions grounded in linguistic literature to create controlled perturbations of research papers, specifically targeting two dimensions: linguistic features associated with native versus non-native English writing, and high-confidence versus low-confidence linguistic features. These interventions are explicitly designed to preserve the underlying scientific content, isolating style as the sole variable being tested.
- The experimental results reveal that LLM reviewers systematically reward confident rhetoric regardless of the actual scientific content of the paper. This means that a paper with weaker scientific claims but more assertive language may receive higher evaluation scores than a paper with stronger claims expressed in hedged or tentative language, fundamentally undermining the validity of LLM-assisted peer review.
- The study highlights that while LLM capabilities have improved considerably, their evaluations remain susceptible to linguistic characteristics entirely unrelated to scientific content, raising serious concerns about the robustness and fairness of LLM-based assessments in academic peer review pipelines.

## Context
The volume of submissions to major AI conferences has increased dramatically in recent years, creating an unsustainable peer-review workload for human researchers. In response, both individual reviewers and conference organizations have increasingly turned to large language models to assist or automate the review process. This paper addresses a critical gap in understanding whether these LLM-based evaluation tools can truly assess scientific quality or whether they are susceptible to superficial linguistic cues that have no bearing on research merit.

## Implications
For the AI research community and conference organizers, these findings suggest that LLM-based peer review tools currently in deployment may systematically disadvantage authors who write in non-native English or who use appropriately cautious scientific language, potentially introducing a new form of structural bias into the publication pipeline. Practitioners and conference organizers should treat LLM-generated review scores with caution and consider implementing safeguards such as style-normalization preprocessing or multi-model evaluation panels before relying on automated assessments for high-stakes decisions like paper acceptance or rejection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35254v1)
