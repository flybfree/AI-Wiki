---
title: On the Capability Separation Between World-Model Policy Learning and Imitated World-Action Models
published: 2026-08-23T03:25:31Z
authors: Yang Yu
url: http://arxiv.org/abs/2608.22197v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Capability Separation Between World-Model Policy Learning and Imitated World-Action Models

## Abstract
World-action models predict a future outcome and then infer an associated action. Although this factorization can improve representation learning and data efficiency, it is unclear whether it provides stronger control capability than direct behavior cloning when both are trained from the same observational demonstrations.   We compare a direct behavior-cloning policy, an imitation-trained world-action policy, and a policy optimized with an action-conditioned world model. At the controller-class level, every world-action policy can be flattened into a direct stochastic policy with the same closed-loop trajectory distribution. At the population level, under realizability, exact optimization, common deployment information, and distribution-preserving deployment, direct behavior cloning and world-action imitation both recover the observational behavior policy. Thus, future prediction changes the learning factorization but not the unrestricted external policy class or ideal imitation target.   Action-conditioned world-model learning differs by predicting outcomes under specified actions and comparing them through a control objective. We characterize the irreducible action-specific prediction error of future models that do not condition on the candidate action, identify conditions under which a world-action joint can recover an interventional forward model, and show that observational demonstrations do not identify action effects in general. Finally, we construct an environment family in which every observational learner has positive worst-case regret, whereas one informative intervention permits zero regret. The key distinction is therefore between predicting futures associated with observed behavior and predicting consequences of specified actions for policy optimization.

## Metadata
- **Published**: 2026-08-23T03:25:31Z
- **Authors**: Yang Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22197v1)