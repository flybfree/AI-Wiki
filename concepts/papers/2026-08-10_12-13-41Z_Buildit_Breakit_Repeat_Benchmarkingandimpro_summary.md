# Summary: 2026-08-10_12-13-41Z_Buildit_Breakit_Repeat_BenchmarkingandimprovingLLM.md
Saved: 2026-08-10 23:47
Source: 2026-08-10_12-13-41Z_Buildit_Breakit_Repeat_BenchmarkingandimprovingLLM.md
Model: None

---

## Summary  
The paper tackles the growing challenge of detecting machine‑generated disinformation on social media, where large language models (LLMs) can rewrite posts to evade static classifiers. By adapting the classic “Build it, Break it, Fix it” framework into an iterative “Build it, Break it, Repeat” (BiBiR) protocol, the authors stress‑test detectors under successive adversarial transformations and evaluate whether their performance degrades over time. The study demonstrates that iterative attacks can flip labels up to 95 % of the time while preserving original meaning, and that a novel triplet contrastive model with dynamic anchor switching improves detection accuracy by 15 percentage points compared with strong baselines. Overall, the work shows how an iterative adversarial loop both exposes detector weaknesses and drives robustness gains, though it also highlights the need for semantic‑preservation checks to distinguish valid evasion from altered claims.

## Key Contributions  
- The best adversarial breakers combine back‑translation with LLM persona‑based rewriting, achieving a 95 % label‑flip rate (LFR) while retaining original meaning.  
- A triplet contrastive model equipped with dynamic anchor switching (DASS) is the strongest builder, delivering an average accuracy of 72.68 % and outperforming the baseline by 15 points on the most robust set of breakers’ attacks.  
- The BiBiR iterative framework reveals how detector reliability erodes under repeated adversarial conditions, prompting both robustness improvements and a need for semantic‑preservation analysis.

## Methodology  
The authors repurpose the “Build it, Break it, Fix it” paradigm into an iterative “Build it, Break it, Repeat” (BiBiR) workflow. In each of five sessions, they generate adversarial versions of social‑media posts using back‑translation and LLM persona rewriting, then feed these transformed posts to a detector. The process repeats, tracking label flips across iterations. Detectors are evaluated on both the original posts and their progressively more evasive counterparts, allowing measurement of robustness degradation.

## Results  
The most effective breakers produced adversarial texts that flipped labels at 95 % (LFR) while preserving semantic content. The top‑performing builder—a triplet contrastive model with dynamic anchor switching (DASS)—reached an average accuracy of 72.68 %, surpassing the strong baseline (fine‑tuned e5‑small‑LoRA) by 15 percentage points on the most robust breakers’ attacks. These results quantify how iterative adversarial pressure can both degrade detection performance and motivate architectural enhancements.

## Significance  
The BiBiR approach provides a systematic method for stress‑testing LLM‑based disinformation detectors, exposing hidden failure modes that static benchmarks miss. By quantifying label‑flip rates and accuracy gains, it offers concrete guidance for improving robustness. However, the study also underscores that iterative evasion can sometimes alter the original claim’s meaning, necessitating additional semantic checks to ensure detection remains faithful.

## Related Concepts  
- Build it, Break it, Fix it framework  
- Adversarial detection of LLM‑generated disinformation  
- Triplet contrastive models with dynamic anchor switching (DASS)  
- Back‑translation and persona‑based rewriting as evasion techniques  
- Label flip rate (LFR) metric  
- Semantic preservation analysis
