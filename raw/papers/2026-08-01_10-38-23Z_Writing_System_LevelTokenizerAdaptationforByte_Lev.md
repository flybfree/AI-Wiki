---
title: Writing-System-Level Tokenizer Adaptation for Byte-Level BPE
published: 2026-08-01T10:38:23Z
authors: Bohdan Didenko
url: http://arxiv.org/abs/2608.00582v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Writing-System-Level Tokenizer Adaptation for Byte-Level BPE

## Abstract
Pretrained byte-level BPE tokenizers can segment underrepresented languages inefficiently. Replacing a tokenizer changes the meaning of nearly every token ID, while vocabulary expansion enlarges the model's embedding and output matrices. We study post-hoc adaptation that keeps the model-vocabulary size fixed and preserves most existing token-to-ID assignments as a construction-time compatibility property. Directly transferring tokens from a language-specific tokenizer does not guarantee derivability through the target BPE merge graph: an inserted entry can conflict with the target's greedy merge ranks. We formalize this failure as the merge ordering problem and introduce BPE-guided insertion, which builds each transferred token through a target-reachable decomposition. Our pipeline uses script-aware row selection to limit collateral fragmentation, reconstructs target-script byte-level prerequisites, and applies guided insertion to maintain merge-graph reachability. On Ukrainian adaptations of Nemotron and GPT-OSS, it reduces token counts by 33.5% and 36.6%, keeps changes on English and the evaluated four-language European aggregate within 0.05%, and retains 78.5%/77.3% of original model-vocabulary rows at the same IDs. Constraint-matched global and frequency-based removal achieve similar Ukrainian compression but increase English/European token counts by 0.7-2.2%; fresh same-size retraining compresses Ukrainian slightly more but retains effectively no same-ID rows and increases English token counts by 7.6-8.6%. The reallocation increases token counts on the evaluated three-language Cyrillic micro-aggregate by 6.7%/10.1%. Structural audits find all 28,134/45,398 inserted BPE nodes reachable under ordinary rank-ordered merging and no retained same-ID model-vocabulary entry newly broken. We release all tokenizers and code.

## Metadata
- **Published**: 2026-08-01T10:38:23Z
- **Authors**: Bohdan Didenko
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00582v1)