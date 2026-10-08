---
title: BanglaRhet: Benchmarking Classical and Transformer Models for Rhetorical and Persuasion Detection in Bangla Political Speech
url: http://arxiv.org/abs/2610.09464v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_05-22-19Z_BanglaRhet_BenchmarkingClassicalandTransformerMode.md
generated_at: 2026-10-07 21:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces BanglaRhet, a manually annotated corpus of 30,289 Bangla political speech segments, and benchmarks four transformer-based models against classical TF-IDF baselines for detecting rhetorical and persuasion techniques in Bangla political discourse. BanglaBERT achieves the highest performance with 65.40% macro-F1 for rhetorical technique detection and 66.46% for persuasion technique detection, outperforming classical baselines by 19.2 and 13.8 macro-F1 points respectively. The study identifies semantic overlap among labels, figurative language ambiguity, and class imbalance as the primary sources of classification errors.

## Key Takeaways
- The paper formulates two supervised single-label classification tasks over the BanglaRhet corpus: rhetorical technique detection covering contrast, repetition, exaggeration, metaphor, and rhetorical questions, and persuasion technique detection covering blame assignment, call to action, unity call, moral appeals, emotional appeals, and logical appeals. This dual-task structure provides a systematic framework for fine-grained discourse analysis in Bangla political language, a domain previously underexplored in NLP benchmarking.
- BanglaBERT outperforms all other evaluated models, including BanglaBERT-Base, SahajBERT, and XLM-RoBERTa-Base, as well as tuned classical TF-IDF baselines, by substantial margins of 19.2 and 13.8 macro-F1 points. This demonstrates that language-specific pre-trained transformer architectures capture Bangla rhetorical and persuasive patterns far more effectively than generic multilingual models or bag-of-words approaches.
- Class-level error analysis reveals that misclassifications stem primarily from semantic overlap between labels (e.g., distinguishing metaphor from exaggeration), the inherent ambiguity of figurative language in political speech, and significant class imbalance within the annotated corpus. These findings underscore that single-label classification is insufficient for capturing the multifaceted nature of rhetorical devices in real-world political discourse.

## Context
While Bangla NLP has seen meaningful advances in sentiment analysis and opinion mining, systematic benchmarking of transformer architectures for fine-grained rhetorical and persuasion detection in political speech has remained largely absent from the literature. This paper fills that gap by providing the first large-scale annotated benchmark and comparative evaluation framework for Bangla political discourse analysis, positioning it alongside existing English-language rhetorical detection benchmarks such as those built on the Penn Discourse Treebank or the Rhetorical Structure Theory corpus.

## Implications
For researchers and practitioners working on low-resource language NLP, BanglaRhet establishes reproducible baselines and a standardized evaluation protocol that can accelerate progress in Bangla political discourse analysis, misinformation detection, and media literacy tooling. The identified limitations around semantic overlap and class imbalance point directly toward the need for multi-label modeling, context-aware architectures, and expanded annotation efforts, offering a clear roadmap for future work in computational rhetoric for Bangla and other underrepresented languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09464v1)
