---
title: Spicing up Genetic Netlist Generation with LLMs
published: 2026-08-24T14:34:22Z
authors: Stefan Uhlich, Yağız Gençer, Andrea Bonetti, Arun Venkitaraman, Chia-Yu Hsieh, Eisaku Ohbuchi, Lorenzo Servadei
url: http://arxiv.org/abs/2608.23317v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spicing up Genetic Netlist Generation with LLMs

## Abstract
Analog circuit topology synthesis remains challenging because useful designs occupy a tiny fraction of a combinatorial search space, and small structural changes can induce highly nonlinear changes in behavior. Evolutionary algorithms are attractive because they can optimize over discrete circuit topologies using only black-box evaluations, but they often require many SPICE simulations and may converge prematurely. We introduce LLM-SPICEMixer, a hybrid synthesis framework that augments genetic netlist generation with IGEL (Inspiration-Guided Evolution with LLMs), an LLM-based proposal operator. During search, IGEL prompts an LLM with high-performing circuits from the elite set and instructs it to generate a new SPICE netlist, which is then evaluated by SPICE and selected using the same reward mechanism as conventional genetic operators. Thus, the LLM contributes structured topology proposals while simulation remains the source of truth. We evaluate LLM-SPICEMixer on a challenging benchmark task: synthesizing transistor-level circuits that implement a discriminant function for Iris classification. Compared with the genetic framework without LLM guidance, LLM-SPICEMixer improves the median final training reward by 8.4% and the median validation-selected test reward by 8.8%. The best validation-selected circuit achieves 93.3% test accuracy at the nominal tt corner and 85.9% average test accuracy across 17 process, voltage, and temperature corners.

## Metadata
- **Published**: 2026-08-24T14:34:22Z
- **Authors**: Stefan Uhlich, Yağız Gençer, Andrea Bonetti, Arun Venkitaraman, Chia-Yu Hsieh, Eisaku Ohbuchi, Lorenzo Servadei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23317v1)