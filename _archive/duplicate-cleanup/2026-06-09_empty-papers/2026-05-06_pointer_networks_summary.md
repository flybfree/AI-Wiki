# Pointer Networks
Saved: 2026-05-07 22:08
Source: 2026-05-06_pointer_networks.md

---

## Summary
Pointer Networks introduce a mechanism for selecting discrete outputs by pointing into the input sequence rather than generating from a fixed vocabulary. This makes them useful for variable-length structured prediction problems where the output elements are copies of input items. The approach extends seq2seq modeling with attention-based selection.

## Key Takeaways
- The model outputs pointers to input positions instead of symbolic tokens.
- This is well suited to combinatorial or variable-length selection tasks.
- Attention serves as the basis for discrete output selection.

## Context
The source file is a reading-list entry linking to the original paper and PDF. Its main significance is as an early formulation of pointer-based attention.

## Implications
Pointer networks influenced later copy mechanisms and structured prediction architectures. They remain a useful reference for tasks where outputs are subsets, permutations, or ordered selections from inputs.

## Original Reference
- Title: Pointer Networks
- Authors: Oriol Vinyals, Meire Fortunato, Navdeep Jaitly
- Published: 2015
- URL: https://papers.nips.cc/paper_files/paper/2015/hash/29921001f2f04bd3baee84a12e98098f-Abstract.html
- Source file: /home/rich/wiki/ai-research/raw/papers/2026-05-06_pointer_networks.md