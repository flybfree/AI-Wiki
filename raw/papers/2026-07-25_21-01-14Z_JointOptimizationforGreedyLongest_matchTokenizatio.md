---
title: Joint Optimization for Greedy Longest-match Tokenization
published: 2026-07-25T21:01:14Z
authors: Adhiraj Singh, Deepanshu Mody, Ghina Al Shdaifat, Hamza Alshamy, Adam Wiemerslage, Varshini Reddy, Craig W. Schmidt
url: http://arxiv.org/abs/2607.23362v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Joint Optimization for Greedy Longest-match Tokenization

## Abstract
Recent work has shown that subword vocabularies can be trained to optimize compression for a specific inference rule rather than relying on greedy heuristics such as Byte Pair Encoding (BPE). We extend this approach to greedy left-to-right longest-match decoding, the fast and widely used inference rule underlying WordPiece. We introduce Joint Optimization for Greedy Longest-Match Tokenization (JOLT), which formulates vocabulary learning as an integer program over vocabulary-selection and segmentation-choice variables. Greedy-consistency constraints ensure that each optimized segmentation exactly matches the segmentation produced by longest-match decoding under the selected vocabulary, aligning the training objective with deployment-time tokenization. To scale the optimization, we solve a linear programming relaxation and selectively introduce higher-order segmentations only for unresolved pretokens. The resulting relaxation is nearly integral: rounded solutions fall within 0.008 - 0.176 % of the LP lower bound on the training scope. The bound also shows that BPE is already within 1 - 2 % of the best achievable compression under greedy longest-match decoding, while JOLT closes 89.6 - 99.4 % of the remaining gap. On held-out validation data across four training scopes and vocabulary sizes of 32,000 and 64,000, JOLT produces up to 0.78 % fewer tokens than BPE, with improvements generally increasing as the training scope grows. These results demonstrate that inference-aligned vocabulary optimization can recover most of the limited compression headroom left by BPE while providing a certificate of near-optimality.

## Metadata
- **Published**: 2026-07-25T21:01:14Z
- **Authors**: Adhiraj Singh, Deepanshu Mody, Ghina Al Shdaifat, Hamza Alshamy, Adam Wiemerslage, Varshini Reddy, Craig W. Schmidt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23362v1)