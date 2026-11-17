---
title: Model Maps: A Documentation Framework for Tracing Foundation Model Ancestry and Understanding AI Entanglement
url: http://arxiv.org/abs/2611.18998v1
type: paper-summary
date: 2026-11-16
source_paper: 2026-11-13_22-54-13Z_ModelMaps_ADocumentationFrameworkforTracingFoundat.md
generated_at: 2026-11-16 21:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces "model maps," a conceptual documentation framework designed to trace the ancestry of foundation models by representing relationships between upstream artifacts (models, datasets, benchmarks) that influence a downstream model's behavior. By applying this framework to 15 closed and open-weight foundation models, the authors document 2,778 unique dependencies spanning up to 9 hops of separation, demonstrating the extensive complexity of AI entanglement in current model development practices.

## Key Takeaways
- The authors propose a taxonomy of 13 dependency mechanisms (including model fine-tuning, synthetic data generation, and other upstream influences) that formalize how pre-existing AI artifacts propagate properties into downstream foundation models. This taxonomy provides a structured vocabulary for identifying how security vulnerabilities, hallucinations, and biased predictions can be inherited from upstream artifacts rather than originating in the model itself.
- Applying the model map framework to 15 real-world foundation models revealed 2,778 unique dependencies and traced artifacts located up to 9 hops away from the resulting model. This empirical finding demonstrates that AI entanglement is not a theoretical concern but a pervasive, deeply nested reality in current model development pipelines, making root-cause identification extremely difficult without structured documentation.
- The framework builds upon existing documentation standards such as ecosystem graphs, datasheets, and model cards, extending them into a detailed knowledge graph representation. The authors argue that AI transparency requirements must expand beyond individual model disclosures and training-data statements to encompass upstream dependencies, enabling more effective risk assessment, auditing, and accountability across the entire AI supply chain.

## Context
Foundation model development increasingly relies on a layered supply chain of pre-existing models, synthetic datasets, benchmarks, and fine-tuning pipelines, creating entangled webs where upstream properties propagate downstream. Existing documentation frameworks like model cards and datasheets address individual artifacts in isolation but fail to capture the relational structure connecting these artifacts to a final model. This gap leaves developers, regulators, and researchers without tools to trace the provenance of problematic behaviors such as inherited biases or security vulnerabilities, making accountability across the AI supply chain nearly impossible.

## Implications
For practitioners and regulators, model maps offer a practical mechanism to audit foundation models for inherited risks, assign accountability to upstream contributors, and design more targeted mitigation strategies rather than treating models as opaque black boxes. The public release of model maps at modelmaps.ai provides a reference implementation that could inform future AI governance standards, procurement due diligence, and compliance frameworks. For the research community, the 13-mechanism dependency taxonomy and the empirical evidence of 9-hop entanglement underscore the urgent need for standardized, machine-readable documentation of model lineage to support safety evaluations and regulatory oversight at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.18998v1)
