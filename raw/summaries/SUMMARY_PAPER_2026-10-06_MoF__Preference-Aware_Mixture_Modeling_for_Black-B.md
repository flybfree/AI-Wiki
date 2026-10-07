---
title: MoF: Preference-Aware Mixture Modeling for Black-Box LLM Personalization
url: http://arxiv.org/abs/2610.08330v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_13-29-26Z_MoF_Preference_AwareMixtureModelingforBlack_BoxLLM.md
generated_at: 2026-10-06 22:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Mixture-of-Facets (MoF), a scalable personalization framework for proprietary black-box Large Language Models that represents user preferences as compositions of shared latent preference facets rather than dedicated per-user parameters. The framework uses history-conditioned routing over shared facet heads to personalize outputs, and the authors demonstrate that MoF achieves stronger personalization performance while remaining more parameter-efficient and generalizable to unseen users compared to prior approaches that rely on user-specific scoring heads.

## Key Takeaways
- Existing black-box LLM personalization methods attach user-specific scoring heads to the model, which causes the number of personalized parameters to grow linearly with the number of users and requires additional adaptation steps for any new user. MoF eliminates this bottleneck by decomposing preferences into a fixed set of shared latent facets, so the parameter count remains constant regardless of user population size.
- MoF personalizes responses through history-conditioned routing over shared facet heads, meaning the system dynamically composes a user's preference vector from the shared facet pool based on their interaction history. This routing mechanism enables zero-shot personalization for users who were never seen during training, without any additional parameter updates or fine-tuning.
- Empirical evaluation across diverse personalization tasks shows that MoF not only matches or exceeds the personalization quality of prior user-specific approaches but also demonstrates strong generalization to unseen users, confirming that the shared-facet representation captures transferable preference structure rather than memorizing individual user patterns.

## Context
As proprietary LLMs become the dominant interface for consumer and enterprise applications, providers increasingly need to tailor outputs to individual user preferences without exposing model weights or allowing per-user fine-tuning. The tension between personalization quality and scalability has been a persistent challenge: methods that achieve high personalization accuracy typically require per-user parameters that do not scale to millions of users, while scalable methods often sacrifice personalization fidelity. MoF addresses this gap by borrowing from the Mixture-of-Experts paradigm and applying it at the preference level rather than the model capacity level, offering a middle path that is both expressive and parameter-efficient.

## Implications
For industry practitioners deploying black-box LLM services at scale, MoF provides a practical blueprint for personalization that avoids the linear parameter growth and cold-start adaptation problems inherent in current approaches, reducing infrastructure costs and enabling immediate personalization for new users. For the broader research community, the work suggests that preference structure in language model outputs can be decomposed into a small, shared latent space, which opens avenues for preference-aware evaluation benchmarks, cross-user preference transfer, and privacy-preserving personalization where individual user data need not be stored as dedicated model parameters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.08330v1)
