---
title: FleetPilot: Fine-Grained Steering Empowers Real-World LLM Personalization
published: 2026-10-10T14:44:50Z
authors: Kounianhua Du, Jianxing Liu, Kangning Zhang, Wenxiang Jiao, Yuan Lu, Jiarui Jin, Jianghao Lin, Weiwen Liu, Yong Yu, Weinan Zhang
url: http://arxiv.org/abs/2610.14970v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FleetPilot: Fine-Grained Steering Empowers Real-World LLM Personalization

## Abstract
With the rapid evolution of large language models (LLMs), there is an increasing demand for effective personalization techniques that can adapt model behavior to individual user preferences. Personalized LLMs must infer a user's query-dependent preferences from limited, heterogeneous, and evolving interaction histories. Existing approaches rely primarily on in-context personalization, parametric adaptation, or personalized reward modeling, but respectively incur recurring costs in context management, model optimization and deployment, or multi-candidate generation and scoring. These limitations become particularly restrictive when user observations are sparse and the preference evidence relevant to each query varies across contexts and over time. To address these challenges, we propose \modelname, a fine-grained and instance-tailored steering framework that dynamically generates sample-level interference vectors from user data and injects them into the model's forward pass for personalized adaptation. Our approach introduces: match contrast that produces user-relevant signals, fine-grained steering component that captures nuanced signals by hooking activations from attention and MLP layers, and query-conditioned aggregation module that synthesizes these signals into contextually relevant enhancements. Extensive experiments across diverse scenarios, including short-to-long text generation, and web function calling, validate the effectiveness and compatibility of \modelname. Results show that our method consistently brings significant performance gains, and show extreme superiority in fast-shifting and data-sparse environments. Additionally, \modelname rids us of training cycles and incurs light overhead of storage or inference latency. These make \modelname a strong and real-world deployable method. Implementation is available \footnote{https://anonymous.4open.science/r/FleetPilot}.

## Metadata
- **Published**: 2026-10-10T14:44:50Z
- **Authors**: Kounianhua Du, Jianxing Liu, Kangning Zhang, Wenxiang Jiao, Yuan Lu, Jiarui Jin, Jianghao Lin, Weiwen Liu, Yong Yu, Weinan Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14970v1)