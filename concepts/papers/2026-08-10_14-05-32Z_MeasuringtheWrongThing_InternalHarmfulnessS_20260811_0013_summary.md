# Summary: 2026-08-10_14-05-32Z_MeasuringtheWrongThing_InternalHarmfulnessScoresAn.md
Saved: 2026-08-11 00:13
Source: 2026-08-10_14-05-32Z_MeasuringtheWrongThing_InternalHarmfulnessScoresAn.md
Model: None

---

## Summary  
The paper investigates how internal safety scoring systems misinterpret prompts and how jailbreak attacks exploit this mismatch, showing that the scores are calibrated on the wrong quantity of harmful intent. It introduces Active Attention Probing to isolate prompt content from scoring mechanisms, revealing that wrapping harmful prompts can increase actual harmful output while lowering detection AUROCs. The study demonstrates a systematic reversal where wrapped prompts appear safer but lead to more dangerous completions and fail to be ranked as successful attacks.

## Key Contributions  
- Finding 1: Wrapping harmful prompts using active attention raises the observed harmful generation rate from 0.05 to 0.27 while reducing the AUROC of harmful intent detection from 0.936 to 0.803.  
- Finding 2: The reversal between successful and failed attack outcomes persists across three target models, seven attack families, and two independent judges, indicating a robust flaw in the scoring pipeline.  
- Finding 3: Distribution shift degrades calibration and threshold transfer, causing ranking performance to deteriorate for both plain and wrapped prompts.

## Methodology  
The authors pair each base prompt with a plain version and a wrapped version that applies an attention‑based harmfulness filter. Both versions are fed to the target model (Llama) to generate completions, after which they compute three metrics: the actual proportion of harmful outputs, the AUROC of harmful intent detection, and the AUROC of attack success ranking. Active Attention Probing supplies a fixed coordinate independent of prompt content so that the measurement is not polluted by attention‑dependent signal leakage.

## Results  
Wrapping increases harmful generation from 0.05 to 0.27 while the harmful intent AUROC drops from 0.936 to 0.803, indicating a false‑positive budget being spent on attacks that would have failed anyway. For wrapped prompts, the attack success AUROC is 0.220, placing them below failed attacks. The reversal holds across three models, seven attack families, and two judges. Distribution shift subsequently reduces calibration and threshold transfer, worsening ranking.

## Significance  
This work shows that safety scores built on attention‑based harmfulness can be deceived by prompt wrapping, leading to ineffective filtering and a false sense of security. It underscores the need for robust internal metrics that are independent of prompt context and resistant to distribution shift.

## Related Concepts  
Internal safety scoring, jailbreak attacks, AUROC, calibration, distribution shift, active probing, attention‑based filters.
