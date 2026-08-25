---
title: Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations
published: 2026-08-23T14:49:59Z
authors: Isotta Magistrali, Chen Shani
url: http://arxiv.org/abs/2608.22444v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aligned Alone, Misaligned Together: Forecasting Adversarial Capture in LLM Agent Populations

## Abstract
The unit of AI safety evaluation is still the individual model, yet language-model agents are increasingly deployed in interacting populations that read and write one another's decisions. This raises a question no single-agent audit can answer: an agent that is well-calibrated on its own may still be pulled toward a different decision by the agents around it. We study this on a security-triage task, where populations of language-model monitors decide whether to escalate or dismiss alerts, and into which we can inject a committed minority that always pushes one way. We find that two alerts a single agent judges almost identically on its own can drive collective behavior far apart, so auditing any one member need not reveal what the population will do. Yet that collective behavior can be predicted in advance. From a population's benign, adversary-free operation alone, we calibrate a response function that forecasts, before any attack is run, how far a committed minority will later move it. We then ask what shifts the outcome and find that letting agents see each other's reasoning neutralizes a weak attack, while only delaying it against a strong one, turning the question from whether the population converges on the adversaries' choice into when. Finally, we exclude the hypothesis of capture being an irreversible trap: once the committed agents are removed, the population drifts back toward where it began, so capture is a temporary state. Alignment in isolation is not alignment in a population, yet what a population will do under attack can be read in advance, from how it behaves before any adversary arrives.

## Metadata
- **Published**: 2026-08-23T14:49:59Z
- **Authors**: Isotta Magistrali, Chen Shani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22444v1)