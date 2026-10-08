---
title: Are Parameter-Efficient Fine-tuning Methods Really Different?
url: http://arxiv.org/abs/2610.09122v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-06_21-13-22Z_AreParameter_EfficientFine_tuningMethodsReallyDiff.md
generated_at: 2026-10-07 22:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper systematically compares six parameter-efficient fine-tuning (PEFT) methods across language and diffusion models to determine whether their methodological differences translate into meaningful functional distinctions. The authors find that LoRA-family methods already approximately preserve pretrained weight geometry, and that explicitly restoring slightly drifted singular-value spectra largely recovers task performance, thereby questioning whether strict geometric preservation is truly necessary. The study further reveals that different PEFT methods exhibit distinct adaptation-retention trade-offs, with LoRA most consistently limiting forgetting, DoRA achieving higher mean task scores, and PiSSA incurring greater retention costs.

## Key Takeaways
- Spectral preservation, a design principle central to orthogonal fine-tuning (OFT), may not be as critical as previously assumed: the authors demonstrate that LoRA-family methods already approximately maintain pretrained weight geometry, and that restoring their minor singular-value drifts largely preserves task performance, suggesting that explicit geometric constraints may be less essential than the field has assumed.
- The adaptation-retention trade-off varies meaningfully across PEFT methods and settings: LoRA most consistently limits catastrophic forgetting while maintaining competitive task performance, DoRA achieves higher mean task scores than LoRA in most comparisons, and PiSSA often incurs greater retention costs, indicating that no single method dominates across all evaluation dimensions.
- Intervention experiments reveal that restoring dominant spectral components (rather than intermediate or trailing ones) produces the largest mean reduction in general-text negative log-likelihood or base-image drift, implying that performance gains from different PEFT methods can be attributed to modifications in different groups of spectral components and that the functional consequences of geometric constraints matter more than preservation alone.

## Context
Parameter-efficient fine-tuning has become a cornerstone of modern AI deployment, enabling practitioners to adapt large pretrained models without the prohibitive computational cost of full fine-tuning. The field has proliferated with numerous PEFT variants—LoRA, DoRA, PiSSA, OFT, and others—each motivated by distinct theoretical justifications such as spectral preservation, low-rank decomposition, or orthogonal transformations. However, the community has lacked rigorous, cross-method comparisons that connect these theoretical parameterizations to observable functional outcomes like task performance, catastrophic forgetting, and changes in pretrained weight geometry. This paper fills that gap by providing a unified experimental framework across both language and diffusion model domains.

## Implications
For practitioners selecting a PEFT method, this work suggests that the choice should be guided by the specific adaptation-retention trade-off relevant to the deployment scenario rather than by theoretical elegance of geometric constraints. For the research community, the finding that restoring dominant spectral components matters most while explicit geometric preservation may be unnecessary challenges prevailing design assumptions and motivates evaluating PEFT methods through their functional consequences rather than through preservation metrics alone. Industry teams fine-tuning large language or diffusion models can leverage these insights to make more informed method selections, potentially reducing both computational overhead and the risk of catastrophic forgetting in production systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09122v1)
