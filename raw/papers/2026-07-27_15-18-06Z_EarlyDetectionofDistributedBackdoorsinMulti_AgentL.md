---
title: Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study
published: 2026-07-27T15:18:06Z
authors: Diego Fernandez Arias, Dev Prashant Mistry, Ren Wang, Yibo Hu
url: http://arxiv.org/abs/2607.24893v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Early Detection of Distributed Backdoors in Multi-Agent LLM Systems: A Characterization Study

## Abstract
Multi-agent LLM systems can be attacked by a payload that no single agent ever holds in full: a poisoned tool hides encrypted fragments in its observations, spreads them across several agents, and an external step reassembles and executes them after the run. Per-step safety checks that judge each action in isolation may fail to recognize the complete distributed payload. We investigate how early such an attack can be detected while the run is still unfolding, and how robustly it can be caught once its most obvious cues are stripped away. We build a working instance on a hierarchical multi-agent system, run it under benign and attacked conditions across five language models and two task domains, and record when each fragment is injected and when the payload is assembled and executed. Detection is a race against assembly. Before the first fragment is injected, attacked and benign runs are indistinguishable; once injection begins, a prefix detector flags $99.3\%$ of successful attacks with a median of five steps remaining and a $10.3\%$ safe-run false-positive rate. Because assembly occurs only after the run, these alarms arrive in time to abort nearly every successful attack. We then measure how much of that warning rests on removable surface cues of the attack rather than on its distributed structure. Generic zero-shot and behavior-trained detectors provide almost no warning at all; the detectors that do work lean in part on removable surface cues, chiefly the ciphertext's length and entropy, and once the entropy cue is removed from the payload and the length features from the detector, detection arrives later and transfers poorly across domains, though a fine-tuned model recovers some of the loss.

## Metadata
- **Published**: 2026-07-27T15:18:06Z
- **Authors**: Diego Fernandez Arias, Dev Prashant Mistry, Ren Wang, Yibo Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24893v1)