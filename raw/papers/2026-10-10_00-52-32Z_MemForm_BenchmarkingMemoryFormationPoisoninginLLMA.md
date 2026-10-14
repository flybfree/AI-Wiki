---
title: MemForm: Benchmarking Memory Formation Poisoning in LLM Agents
published: 2026-10-10T00:52:32Z
authors: Haowen Pan, Pengyang Shao, Yunshan Ma, Yanzheng Jin, Naixin Zhai, Xiang Wang, Xun Yang
url: http://arxiv.org/abs/2610.14431v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemForm: Benchmarking Memory Formation Poisoning in LLM Agents

## Abstract
Long-term memory enables LLM agents to learn from past interactions but exposes memory formation to adversarial influence. Existing studies primarily organize memory poisoning by attack channels, corruption patterns, or lifecycle stages, leaving formation interfaces insufficiently characterized. We formulate Memory Formation Poisoning as adversarial manipulation of the interfaces through which persistent agent memory is produced and committed, and introduce MemForm, a controlled diagnostic benchmark covering five interfaces: Content, Evidence, Scope, Selection, and Path Poisoning. We introduce Selection and Path Poisoning as controlled intervention categories that isolate retention and consolidation order effects, respectively. Each category pairs clean and poisoned conditions with interface-specific controls. Evaluations across six LLMs and two response formats reveal broad susceptibility at all five interfaces under the evaluated memory protocols and implementations. Crucially, authentic experiences with successful outcomes do not guarantee reliable behavior after memory formation: changes to contextual support, retention, or consolidation order can induce undesirable downstream behavior. In particular, consolidation order can alter behavior even with identical retained experiences, depending on the memory formation procedure. Additional analyses show that interface applicability depends on memory architecture and that Path Poisoning susceptibility depends on the updater. The evaluated defenses provide incomplete mitigation that varies by interface. These findings motivate protecting both what is committed to persistent memory and how memory is formed from experiences. Code and data are available at https://github.com/opanhw/memform-code.

## Metadata
- **Published**: 2026-10-10T00:52:32Z
- **Authors**: Haowen Pan, Pengyang Shao, Yunshan Ma, Yanzheng Jin, Naixin Zhai, Xiang Wang, Xun Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14431v1)