---
title: PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios
url: http://arxiv.org/abs/2610.20548v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_17-39-35Z_PerSo_InvestigatingFacetsofLLMs_SocialIntelligence.md
generated_at: 2026-10-14 21:50
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces PerSo, a benchmark designed to evaluate both cognitive and behavioral aspects of social intelligence in large language models using real-world persuasion dialogues sourced from Reddit's ChangeMyView community. The authors construct evaluation tasks through an LLM-in-the-loop pipeline validated by human annotation, and their experiments reveal that while LLM performance generally scales with model size, the strongest model slightly surpasses the best human performance on behavioral tasks while humans retain an advantage on cognitive tasks involving mental state inference.

## Key Takeaways
- PerSo addresses a critical gap in existing evaluation frameworks by testing cognitive intelligence (inferring others' mental states) and behavioral intelligence (selecting appropriate social actions to achieve goals) simultaneously within a single real-world persuasion context, rather than evaluating these facets in isolation through synthetic scenarios as prior benchmarks have done.
- The benchmark leverages authentic persuasion dialogues from Reddit's ChangeMyView community, where users attempt to change others' viewpoints, providing a natural testbed where both mental state inference and strategic social action selection are inherently intertwined, and the evaluation tasks are constructed via an LLM-in-the-loop pipeline that is validated through human annotation to ensure reliability.
- The empirical findings show a nuanced performance landscape: model size correlates with improved performance across dimensions, but the strongest LLM only marginally exceeds the best observed human on behavioral tasks, while humans maintain a clear lead on cognitive tasks, suggesting that inferring complex human mental states remains a harder problem for current models than selecting effective persuasive strategies.

## Context
As LLMs are increasingly deployed in multi-agent environments, human-AI interaction systems, and collaborative settings, understanding their social intelligence has become a prerequisite for safe and effective deployment. Existing benchmarks have largely treated social cognition and social behavior as separate evaluation targets using artificial or synthetic scenarios, which limits ecological validity and fails to capture the interplay between understanding others and acting socially. PerSo fills this gap by grounding evaluation in genuine human persuasion interactions, aligning benchmark design with the complex, multi-faceted nature of real social reasoning.

## Implications
For practitioners building AI agents intended to operate in collaborative, persuasive, or socially sensitive environments, PerSo provides a more realistic diagnostic tool for identifying where current models fall short, particularly in inferring nuanced human mental states. The finding that humans still outperform LLMs on cognitive tasks signals that deploying AI in roles requiring deep empathy, theory of mind, or understanding of human motivations requires caution and human oversight. For the research community, the benchmark's methodology of combining real-world data with LLM-assisted task construction and human validation offers a template for building more ecologically valid evaluations of social capabilities in future models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20548v1)
