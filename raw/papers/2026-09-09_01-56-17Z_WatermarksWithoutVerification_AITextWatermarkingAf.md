---
title: Watermarks Without Verification: AI Text Watermarking After the EU AI Act
published: 2026-09-09T01:56:17Z
authors: Alexander Nemecek, Vipin Chaudhary, Erman Ayday
url: http://arxiv.org/abs/2609.09604v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Watermarks Without Verification: AI Text Watermarking After the EU AI Act

## Abstract
On August 2, 2026, the obligations of Article 50 of the EU AI Act took effect, requiring generative AI providers to mark the content their systems produce and ensure it can be detected as AI-generated. Days later, Anthropic disclosed that every Claude model released after that date embeds a watermark based on SynthID-Text in all generated text, enabled by default with no user opt-out; Google has deployed SynthID-Text in Gemini since 2024. Users objected that the watermark degrades quality, particularly for code, that it secretly encodes identifying information, and, in mutual contradiction, that it is easily removable and inescapable; the vendor answered with assurances of unchanged quality, no identifying information, and robustness to light editing. In this work, we argue that neither the objections nor the assurances can currently be verified and that this unverifiability, rather than watermarking itself, is the substantive governance failure. We sort the contested assertions by what it would take to settle each and evaluate the open-source SynthID-Text implementation on two open-weight models, because no public tool can test the deployed systems. On prose, the measured effect of the watermark does not exceed that of changing the sampling seed. On code, the cost is three points of correctness on one model and below measurement on the other, while detection remains near chance, a limitation of detectability rather than quality. The remaining gaps trace to withheld access or missing institutions and we map each to a requirement: release of matched outputs, configuration disclosure, accredited audits, a shared evaluation protocol, and interoperable detection.

## Metadata
- **Published**: 2026-09-09T01:56:17Z
- **Authors**: Alexander Nemecek, Vipin Chaudhary, Erman Ayday
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09604v1)