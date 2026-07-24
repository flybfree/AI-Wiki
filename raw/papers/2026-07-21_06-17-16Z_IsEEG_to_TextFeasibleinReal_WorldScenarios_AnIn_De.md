---
title: Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark
published: 2026-07-21T06:17:16Z
authors: Zihan Zhang, Yu Bao, Xiao Ding, Tianyi Jiang, Kai Xiong
url: http://arxiv.org/abs/2607.18749v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Is EEG-to-Text Feasible in Real-World Scenarios? An In-Depth Analysis Using a Neuropsychology-Inspired Benchmark

## Abstract
Translating brain signals into text could restore communication for people with severe paralysis, yet practically usable systems to date rely on invasive electrocorticography (ECoG). Electroencephalography (EEG) offers a non-invasive alternative, and EEG-to-text (EEG2Text) has been widely explored. Interestingly, however, EEG2Text models generally rely on teacher-forcing evaluation; without it, they fail to generate meaningful decoding. This reliance prevents EEG2Text from being applied in real-world, non-academic settings. This has fueled numerous debates about whether EEG2Text is a meaningful direction, by extension, and whether EEG truly contains decodable linguistic information. Here, using a neuropsychology-informed paradigm, we find that existing EEG2Text benchmarks have neglected EEG instability, a flaw that has confounded inference and sparked debate. Our experiments furnish key evidence for the feasibility of teacher-forcing-free EEG2Text decoding. Accordingly, we assemble the Corpus OF Eeg-To-Text (COFETT) using a 128-channel high-density EEG cap, providing a benchmark dedicated to evaluating EEG2Text models. In comparisons with multiple existing benchmarks, COFETT achieves SOTA ability to distinguish among model performances and enables robust, teacher-forcing-free evaluation, thereby opening a path toward practical EEG2Text applications. COFETT is open sourced in https://github.com/baoyudu/COFETT.

## Metadata
- **Published**: 2026-07-21T06:17:16Z
- **Authors**: Zihan Zhang, Yu Bao, Xiao Ding, Tianyi Jiang, Kai Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18749v1)