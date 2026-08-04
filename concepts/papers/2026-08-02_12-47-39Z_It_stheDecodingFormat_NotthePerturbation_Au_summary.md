# Summary: 2026-08-02_12-47-39Z_It_stheDecodingFormat_NotthePerturbation_AuditingC.md
Saved: 2026-08-03 23:27
Source: 2026-08-02_12-47-39Z_It_stheDecodingFormat_NotthePerturbation_AuditingC.md
Model: None

---

## Summary  
The paper investigates why test‑time scaling strategies that rely on self‑verification fail to transfer from pure language models to vision‑language models (VLMs). It proposes Perturbation Grounded Selection (Pgs) and a format‑matched control (MatchedCtrl) to isolate the role of image‑grounded versus language‑only decoding, showing that simple majority voting is often outperformed but only under uncontrolled conditions. The study demonstrates that once prompt length and decoding budget are held constant, perturbation consistency provides no reliable advantage over baseline methods.

## Key Contributions  
- [Finding 1] Pgs recovers the behavior of plain majority voting when the perturbation set is empty, confirming it is a label‑free, training‑free rule.  
- [Finding 2] MatchedCtrl tracks or exceeds Pgs on all benchmark datasets (TextVQA, MATH‑Vision, MMMU, ViLP) within statistical noise, and no Qwen category shows a significant gain over this control.  
- [Finding 3] The observed stability gap is real and image‑dependent (up to +0.48 points), yet it does not predict per‑instance wins; perturbation consistency is at best a partial diagnostic of visual dependence.

## Methodology  
The authors introduce Perturbation Grounded Selection (Pgs) as a label‑free, training‑free selection mechanism that scores each candidate answer by whether the model re‑derives it under image‑preserving perturbations such as cropping, background masking, or mild photometric/geometric jitter. To control for prompt format and decoding budget, they create MatchedCtrl: the same short, no‑CoT draws spent on the original image are used in both Pgs and the baseline majority voting. Experiments compare Pgs against plain majority voting and CoT‑only majority voting across four vision‑language benchmarks.

## Results  
On TextVQA with Qwen’s three‑seed mean, Pgs improves over plain majority voting by up to +31.8 points, but MatchedCtrl tracks or exceeds Pgs within noise on every benchmark, including the vision‑required ViLP. The stability gap is real and image‑dependent (up to +0.48), yet it does not correlate with per‑instance wins. Thus, gains reported against CoT‑only majority voting overstate the utility of perturbation consistency.

## Significance  
The result is negative and diagnostic: Perturbation Grounded Selection is at best a partial indicator of visual dependence and, once prompt format and budget are controlled, does not provide a usable selection signal. The paper cautions that reported gains overstate the effectiveness of self‑verification methods in VLMs.

## Related Concepts  
- Test‑time scaling for large language models  
- Vision‑language models (VLMs)  
- Majority voting and chain‑of‑thought prompting  
- Self‑verification selection mechanisms  
- Prompt format (CoT, no‑CoT)  
- Perturbation Grounded Selection (Pgs)  
- Format‑matched control (MatchedCtrl)
