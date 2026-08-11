---
title: BASIS: Breach-Aware Selective Prompt Injection Shielding with Prefill Attention Probes
published: 2026-08-08T09:32:07Z
authors: Laiqiao Qin, Tianqing Zhu, Longxiang Gao, Wanlei Zhou
url: http://arxiv.org/abs/2608.08027v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BASIS: Breach-Aware Selective Prompt Injection Shielding with Prefill Attention Probes

## Abstract
Prompt injection is a critical security threat in large language model (LLM) applications, where attackers hijack model behavior by embedding malicious instructions in user or external data. Existing detection methods only detect the presence of injection and refuse to respond upon detection, overlooking the fact that for many modern aligned models, well-crafted instructions can resist most injection attacks. This means that the injection robustness varies significantly across instructions and models. This leads to widespread unnecessary over-refusal: inputs containing injections that the model could have handled correctly are rejected incorrectly. To deal with this over-refusal issue, we propose BASIS (Robustness-Aware Prompt Injection Defense). This defense method uses the Attention Competition Ratio ($ρ$) as features to train two sparse linear probes: an existence probe and a breach probe. Both probes make defense decisions through cascaded gating, which does not require additional LLM inference. BASIS comprises three stages: injection existence detection, per-sample breach prediction, and instruction robustness assessment; the online cascade refuses only when the model would actually be compromised and thus avoids over-refusal on robust instructions. Experiments across four tasks and six open-source LLMs show that BASIS maintains near-perfect injection detection while substantially reducing over-refusal on safe attack samples, especially under robust instruction templates.

## Metadata
- **Published**: 2026-08-08T09:32:07Z
- **Authors**: Laiqiao Qin, Tianqing Zhu, Longxiang Gao, Wanlei Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08027v1)