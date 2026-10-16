---
title: Agentic-Priors: Using Large Language Models to Address the Cold Start Problem in Preference Elicitation
url: http://arxiv.org/abs/2610.21938v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_14-14-04Z_Agentic_Priors_UsingLargeLanguageModelstoAddressth.md
generated_at: 2026-10-15 22:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Agentic-Priors, a method that leverages the implicit knowledge embedded in large language models to construct informative priors for preference elicitation systems, directly addressing the cold start problem faced by agents learning user preferences from observed choices. Rather than requiring historical choice data to fit priors, the approach asks an LLM to articulate a new user's trade-offs in interpretable terms such as willingness to pay or value of time, maps these to a prior over multinomial logit coefficients, and then refines the prior through Bayesian updating as actual choices are observed. Across seven choice datasets, the method improves cold start accuracy by 5 to 40 percentage points over an uninformed prior and outperforms the state-of-the-art AutoElicit method on three of four tested datasets.

## Key Takeaways
- Agentic-Priors replaces the need for historical choice data by prompting an LLM to state a new user's trade-offs in interpretable economic terms (e.g., willingness to pay, value of time), which are then mapped to a prior distribution over multinomial logit coefficients, enabling a Bayesian learner to begin with a meaningful starting point rather than a flat, uninformed prior.
- The method demonstrates substantial practical gains: it improves cold start accuracy by 5 to 40 percentage points over an uninformed prior, outperforms AutoElicit on three datasets while losing on only one, and is up to 18 percentage points more accurate than in-context learning while never being significantly worse, establishing it as a robust and competitive approach.
- In terms of log-loss, the LLM-generated prior is equivalent in value to surveying roughly 6 to 40 users, meaning the approach's utility is heavily concentrated in a deployment's earliest interactions, after which observed data naturally supersedes the prior, making it most impactful precisely when no data exists.

## Context
Preference elicitation is a foundational challenge in recommendation systems, adaptive interfaces, and human-computer interaction, where agents must infer user preferences from sparse behavioral signals. The cold start problem has long been addressed through hierarchical Bayesian models fitted to survey data or through methods like AutoElicit that attempt to extract priors from LLMs, but these approaches either require costly historical data or produce less interpretable, less accurate priors. Agentic-Priors sits at the intersection of LLM reasoning, Bayesian decision theory, and discrete choice modeling, offering a principled bridge between the broad implicit knowledge of language models and the structured probabilistic frameworks used in preference learning.

## Implications
For practitioners deploying new recommendation or adaptive systems, Agentic-Priors offers a way to achieve meaningful personalization from the very first user interaction without waiting to accumulate historical data, potentially reducing onboarding friction and improving early user experience. For the broader AI research community, the work demonstrates that LLMs can serve as structured prior generators for classical statistical models, opening a pathway for hybrid systems that combine the breadth of language model knowledge with the rigor of Bayesian updating. The finding that the method's value is concentrated in a deployment's first users also suggests a practical deployment strategy: use LLM-generated priors during cold start phases and transition to data-driven models as interaction history accumulates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21938v1)
