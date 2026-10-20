---
title: Secure Agentic Coding through Counterexample-Grounded Feedback
published: 2026-10-19T07:18:34Z
authors: Tue Le, Anh Nguyen Hoang, Gabriel Sasseville, Doseok Jang, Pierre-Luc Bacon, Nghi D. Q. Bui
url: http://arxiv.org/abs/2610.25916v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Secure Agentic Coding through Counterexample-Grounded Feedback

## Abstract
As coding models and agent harnesses become more capable, reliable security verification is becoming a central bottleneck. Improving secure code generation requires a signal whose reported progress remains aligned with actual program behavior under optimization; otherwise, an optimizer can improve the signal's verdict without removing the underlying vulnerability. Existing model-based approaches require models to either infer program behavior from source code or specify correct outcomes for adversarial tests, placing substantial reasoning demands on the security signal. We introduce \falcon{}, a counterexample-grounded verification framework that separates attack exploration from behavioral verification and connects them through execution traces of the program under test. In test-time repair, \falcon{} yields substantially stronger held-out functional-security gains than alternative security signals across secure code generation benchmarks, while preserving or improving functionality. As an RL reward, \falcon{} also outperforms static-analysis and learned rewards on held-out functional-security, even when all policies successfully optimize their respective training rewards. Combining \falcon{} with either proxy reward further improves held-out performance, suggesting that execution-grounded feedback can mitigate reward overoptimization while preserving useful guidance from existing security signals.

## Metadata
- **Published**: 2026-10-19T07:18:34Z
- **Authors**: Tue Le, Anh Nguyen Hoang, Gabriel Sasseville, Doseok Jang, Pierre-Luc Bacon, Nghi D. Q. Bui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25916v1)