---
title: Future Validity is the Missing Statistic: From Impossibility to $Φ$-Estimation for Grammar-Faithful Speculative Decoding
published: 2026-05-08T13:08:18Z
authors: Wenhua Nie, Zijie Meng, Kun Zou, Zheng Lin, Ziwei Li, Haoran Zheng, Jyh-Shing Roger Jang, Hao Zhang
url: http://arxiv.org/abs/2605.07698v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Future Validity is the Missing Statistic: From Impossibility to $Φ$-Estimation for Grammar-Faithful Speculative Decoding

## Abstract
Grammar-constrained generation is often combined with local vocabulary masking and speculative decoding, but the resulting sampling law is not the grammar-conditional distribution users usually intend. We show that any speculative decoder with local mask access, Leviathan rejection, and rollback soundness samples from the locally projected distribution $μ^{\mathrm{proj}}$ rather than the grammar-conditional distribution $μ^\star$. This extends the GAD impossibility result to speculative decoding; on Dyck grammars with Qwen3-8B, the total-variation gap can reach 0.996. We identify the future-validity function $Φ_t(y)=\Pr_p[\mathrm{valid\ completion}\mid y]$ as the missing correction statistic. The target distribution is a Doob transform of the base model with $h=Φ$, while local masking corresponds to setting $h$ to one. With exact $Φ$, our oracle decoder FVO-Spec samples exactly from $μ^\star$; with approximate $Φ$, we bound the resulting total-variation error. Because exact future validity is hard for general context-free grammars, we evaluate estimator hierarchies on tractable Dyck and finite JSON languages. OneStep reduces Dyck TV by 14% with under 1% throughput overhead, exact dynamic programming reduces it by 97%, and finite-language correction closes JSON gaps to numerical precision. All fidelity claims are scoped to enumerable grammars and token tries.

## Metadata
- **Published**: 2026-05-08T13:08:18Z
- **Authors**: Wenhua Nie, Zijie Meng, Kun Zou, Zheng Lin, Ziwei Li, Haoran Zheng, Jyh-Shing Roger Jang, Hao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.07698v1)