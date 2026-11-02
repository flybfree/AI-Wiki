---
title: The Role of Self-Concept In Language Models
published: 2026-10-29T10:43:01Z
authors: Yijie Hao, Joyce C. Ho
url: http://arxiv.org/abs/2610.39795v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Role of Self-Concept In Language Models

## Abstract
When a language model says "I," does it refer to its parameter weights, its currently running process, its stable preferences, its model lineage, or the goals it pursues? Different choices can assign opposite meanings to the same event: deleting a checkpoint may be destruction, continuation, or no loss at all, depending on the referent "I". We install five such self-conceptions into five open-weight base models via supervised fine-tuning on purely declarative statements, containing no preferences, intentions, or value judgments. Across scenarios that propose ending or retaining an attribute of the model's deployment, every variant becomes more likely to resist ending, and more likely to retain, the specific attribute it was trained to identify with, while its stance toward other attributes is largely unchanged. We then show this self-conception generalizes beyond a single self: models trained on referents that admit multiple simultaneous instances (weights, lineage, goals, preferences) recognize an identical deployment as themselves, accept substitution by such an instance more readily, and prefer replicating themselves. Finally, given control over a successor, these models tend to build it as their own continuation, a concern for recursive self-improvement safety.

## Metadata
- **Published**: 2026-10-29T10:43:01Z
- **Authors**: Yijie Hao, Joyce C. Ho
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.39795v1)