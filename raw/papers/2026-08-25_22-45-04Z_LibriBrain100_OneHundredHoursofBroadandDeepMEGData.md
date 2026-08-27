---
title: LibriBrain100: One Hundred Hours of Broad and Deep MEG Data for Neural Speech Decoding at Scale
published: 2026-08-25T22:45:04Z
authors: Francesco Mantegna, Dulhan Jayalath, Gereon Elvers, Tasha Kim, Benjamin Ballyk, Alex Fung, SungJun Cho, Teyun Kwon, Luisa Kurth, Miran Özdogan, Gilad Landau, Pratik Somaiya, Natalie Voets, Mark Woolrich, Oiwi Parker Jones
url: http://arxiv.org/abs/2608.25204v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LibriBrain100: One Hundred Hours of Broad and Deep MEG Data for Neural Speech Decoding at Scale

## Abstract
We introduce LibriBrain100, a large-scale MEG dataset for speech decoding designed from the ground up for reproducible, standardised evaluation. LibriBrain100 more than doubles the size of the original LibriBrain release, resulting in over 100 hours of high-quality MEG acquired while subjects listened to naturalistic continuous speech. With $\sim$80 hours from a single subject, LibriBrain100 sets a new record for deep, within-subject neural data (8$\times$ more than the next comparable dataset and roughly 80$\times$ more than other datasets). To demonstrate the payoff of this depth-first design, we evaluate on a word-classification benchmark---an increasingly well-established stepping stone towards the open challenge of noninvasive brain-to-text decoding. Using an existing decoding model, we achieve state-of-the-art performance---validating both the quality of the recordings and the value of within-subject data at scale. Because collecting 80 hours of data per user is impractical for real-world applications, we also collected $\sim$40 minutes of additional data from each of 32 subjects. Using the same word-classification benchmark, we demonstrate the value of broad multi-subject data: supervised finetuning of a pre-trained model can substantially compensate for limited per-subject data. We provide standard train, validation, and test splits, all reproducible through an open-sourced Python library that supports easy downloading, optional preprocessing, and data loading for common deep learning frameworks. In addition, the dataset and evaluation infrastructure are being released alongside an open machine-learning competition with a public leaderboard for standardised benchmarking. Ultimately, our hope is that LibriBrain100 will accelerate progress towards practical non-invasive brain-computer interfaces, capable of restoring communication to people living with severe paralysis.

## Metadata
- **Published**: 2026-08-25T22:45:04Z
- **Authors**: Francesco Mantegna, Dulhan Jayalath, Gereon Elvers, Tasha Kim, Benjamin Ballyk, Alex Fung, SungJun Cho, Teyun Kwon, Luisa Kurth, Miran Özdogan, Gilad Landau, Pratik Somaiya, Natalie Voets, Mark Woolrich, Oiwi Parker Jones
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25204v1)