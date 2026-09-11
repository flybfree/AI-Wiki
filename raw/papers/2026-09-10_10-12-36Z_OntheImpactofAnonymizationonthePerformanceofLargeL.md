---
title: On the Impact of Anonymization on the Performance of Large Language Models
published: 2026-09-10T10:12:36Z
authors: Tobias Deußer, Max Hahnbück, Lorenz Sparrenberg, Tobias Uelwer, Christian Bauckhage, Rafet Sifa
url: http://arxiv.org/abs/2609.11335v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Impact of Anonymization on the Performance of Large Language Models

## Abstract
As large language models are increasingly deployed in sensitive domains, anonymizing input data to protect personally identifiable information has become a critical practice. However, the impact of this anonymization on model utility is not well understood. This paper presents a systematic empirical study of the trade-off between privacy and performance. We evaluate five prominent language models across eleven diverse benchmarks, comparing their performance on original versus pseudonymized inputs. Our results reveal that while anonymization generally degrades performance, the effect is highly nuanced. We find that more capable models, such as Qwen2.5-72B and GPT-4o mini, suffer the largest performance drops, suggesting a stronger reliance on specific entity information. The impact is also task-dependent: performance on TruthfulQA improves with anonymization, while retrieval-focused tasks like RGB experience a catastrophic decline. Further experiments show that reversible anonymization techniques that preserve entity uniqueness significantly outperform irreversible ones like redaction, and that explicitly prompting models about anonymization offers no discernible benefit. We conclude that anonymization is not a one-size-fits-all solution and must be co-designed with the model and task in mind to balance privacy and utility effectively. Our findings provide a crucial baseline for developing more robust, privacy-aware AI systems.

## Metadata
- **Published**: 2026-09-10T10:12:36Z
- **Authors**: Tobias Deußer, Max Hahnbück, Lorenz Sparrenberg, Tobias Uelwer, Christian Bauckhage, Rafet Sifa
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11335v1)