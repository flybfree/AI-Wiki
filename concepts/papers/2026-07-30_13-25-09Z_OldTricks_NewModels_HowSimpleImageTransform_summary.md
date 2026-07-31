# Summary: 2026-07-30_13-25-09Z_OldTricks_NewModels_HowSimpleImageTransformationsB.md
Saved: 2026-07-30 21:51
Source: 2026-07-30_13-25-09Z_OldTricks_NewModels_HowSimpleImageTransformationsB.md
Model: None

---

## Summary  
The paper investigates whether the shift from traditional classifiers to large foundation models for image moderation improves robustness. It shows that simple image transformations can bypass all three commercial APIs, indicating that model upgrade alone does not guarantee security. Findings highlight vulnerabilities across datasets and harm categories, especially self‑harm content. The work argues that foundation‑model APIs must be evaluated under realistic conditions rather than assumed to provide a reliable safety boundary.

## Key Contributions  
- Finding 1: All three services can be circumvented using inexpensive, gradient‑free image transformations that require no knowledge of the target system.  
- Finding 2: Even basic transforms such as color inversion and grayscale conversion induce unsafe‑to‑safe decision changes while preserving human recognizability.  
- Finding 3: Robustness varies substantially across datasets and harm categories, with multimodal content and self‑harm exhibiting pronounced weaknesses.

## Methodology  
The authors conducted a large‑scale black‑box evaluation on three established commercial image‑moderation APIs. They selected seven simple, model‑agnostic transformations (e.g., color inversion, grayscale conversion, rotation, blur, contrast adjustment) and applied them with varying intensities across multiple harm categories. Transformations were evaluated under perceptual similarity constraints to ensure the altered images remain recognizable.

## Results  
The experiments demonstrated that each API’s decision changed from unsafe to safe after applying certain transforms, with no need for gradient‑based attacks or external models. Robustness dropped sharply on multimodal and self‑harm datasets; other categories showed modest degradation. This variability suggests that foundation‑model APIs are not uniformly secure.

## Significance  
The study reveals a critical flaw in assuming that larger models automatically provide stronger safety filters, prompting the need for layered moderation pipelines and rigorous testing under realistic transformations.

## Related Concepts  
image moderation, AI safety, foundation models, black‑box evaluation, content transformation attacks, multimodal detection, self‑harm content classification.
