# Summary: 2026-08-01_15-41-55Z_Experience_CalibratedContrastiveDecodingforMitigat.md
Saved: 2026-08-03 23:56
Source: 2026-08-01_15-41-55Z_Experience_CalibratedContrastiveDecodingforMitigat.md
Model: None

---

## Summary  
The paper tackles a persistent problem in language‑model‑based text‑to‑speech (LM‑TTS): the generation of speech hallucinations that diverge from the intended text. Its core contribution is Experience‑Calibrated Contrastive Decoding (ECCD), a training‑free decoding‑time technique that strengthens the textual alignment signal while preserving useful acoustic experience information. By conditioning the contrastive loss on both text‑derived and experience‑derived cues, ECCD mitigates hallucinations without altering model architecture or requiring additional training data. The method is evaluated across four state‑of‑the‑art models and shows substantial improvements in standard evaluation metrics as well as a measurable gain in listening quality.

## Key Contributions  
- [Finding 1] Hallucinations arise when textual alignment support is insufficiently reflected at vulnerable transition points within the speech sequence.  
- [Finding 2] ECCD introduces a contrastive decoding framework that enhances only positive alignment signals while maintaining experience‑derived regularities, calibrated via set‑level compatibility scores.  
- [Finding 3] The method reduces Word Error Rate (WER) and Character Error Rate (CER) by up to 55.6 % across SeedTTS‑Eval settings and achieves a listening gain of +0.644 CMOS while preserving speaker similarity.

## Methodology  
ECCD adopts a conditional information view that separates *text‑derived alignment* from *experience‑derived regularities*. For each token, the model is trained to attend more strongly to tokens where the text condition provides strong textual support and the acoustic experience aligns with known speech patterns. The contrastive loss compares predictions made under full text conditioning versus those made without it, encouraging the decoder to select tokens that maximize both alignment gain and experience compatibility. Calibration is performed at the set level using a compatibility score derived from pairwise similarity between text‑conditioned and unconditioned embeddings, ensuring the enhancement does not overpower pure experience cues.

## Results  
Across four LM‑TTS models evaluated on SeedTTS‑Eval, ECCD yields WER/CER reductions of up to 55.6 % relative to baseline decoding. In multilingual CV3‑Eval, it improves performance in 24 out of 25 test sets. Listening tests confirm a measurable gain: the mean Cosine Similarity (CMOS) score rises by +0.644 while speaker similarity remains high. Analysis reveals that alignment influence is strongest at matched correct boundaries and weaker at first‑error boundaries, indicating calibrated control over hallucination risk.

## Significance  
ECCD demonstrates that decoding‑time interventions can substantially curb hallucinations without retraining the language model or adding new data. By explicitly balancing textual fidelity with acoustic regularities, it offers a practical, scalable solution for high‑quality TTS systems where hallucinations are costly in both user experience and downstream applications.

## Related Concepts  
- Experience‑calibrated contrastive decoding (ECCD)  
- Alignment information vs. experience information  
- Set‑level compatibility calibration  
- Text‑conditioned vs. unconditioned speech LM predictions  
- Hallucination mitigation in TTS  
- Contrastive loss for token selection  
- Experience information in acoustic regularities
