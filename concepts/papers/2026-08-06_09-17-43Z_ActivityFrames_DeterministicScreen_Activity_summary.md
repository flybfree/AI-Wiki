# Summary: 2026-08-06_09-17-43Z_ActivityFrames_DeterministicScreen_ActivityCompila.md
Saved: 2026-08-06 20:34
Source: 2026-08-06_09-17-43Z_ActivityFrames_DeterministicScreen_ActivityCompila.md
Model: None

---

## Summary  
The paper proposes **Activity Frames**, a deterministic pipeline that converts raw screen‑capture streams into typed activity frames for agent memory and replay. It eliminates the need for models to infer user actions, instead producing byte‑identical, cacheable context blocks that can be fed directly to agents. The compiler reduces a day of capture to an 86× smaller prompt while maintaining high accuracy against an independent oracle. This approach also supplies measurable parameters—Routine Overhead Ratio (R) and routine recurrence (h)—that were previously unmeasured.

## Key Contributions  
- Deterministic compilation of screen activity into typed frames without any model.  
- Quantification of Routine Overhead Ratio (R) up to 343× and routine recurrence around 7.7% out‑of‑sample.  
- Demonstration that compiled routines can be replayed deterministically at zero model tokens.

## Methodology  
The authors passively capture screen activity, segment it into episodes with metadata such as application, site, timing, input volume, and evidence pointers to the raw rows. No machine‑learning models are involved in the pipeline; the output is a deterministic, cacheable block ready for agent prompts.

## Results  
On 128,756 frames captured over 51 active days, the compiler reduces the size of a day’s capture by 86× in just 68 ms. An LLM reading the resulting block answers questions with 98.4% accuracy (Wilson 95% CI 91.7–99.7%), whereas a mid‑tier model achieves only 66–80%. Crucially, the compiled routine can be replayed deterministically at zero tokens on a guard‑matched hit.

## Significance  
This method replaces costly, uncertain LLM summaries with reliable, auditable memory blocks that capture exact user actions. It provides measurable efficiency metrics—R and h—that improve cost models for large fleets of agents and enables zero‑token replay, lowering operational overhead.

## Related Concepts  
- Activity Frames  
- Deterministic compilation  
- Screen activity capture  
- Agent memory  
- Routine Overhead Ratio (R)  
- Routine recurrence (h)  
- Zero‑token replay  
- Prompt‑ready context block
