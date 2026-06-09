# Summary: 2026-05-26_17-50-17Z_WhenEyesBetrayAI_SocialGazeConsistencyasaSemanticC.md
Saved: 2026-05-26 22:00
Source: 2026-05-26_17-50-17Z_WhenEyesBetrayAI_SocialGazeConsistencyasaSemanticC.md
Model: None

---


## Summary  
The paper introduces **Social Gaze Consistency**, a high‑level semantic cue that measures the mutual coherence of gaze direction, head‑eye alignment, and pupil placement between interacting individuals in an image. By exploiting this cue, the authors demonstrate a previously underutilized detection axis that is orthogonal to low‑level pixel or frequency artifacts, thereby improving AI‑generated image detection across vision‑language models.

## Key Contributions  
- **Finding 1:** Social Gaze Consistency provides a high‑level semantic cue for detecting AI‑generated images.  
- **Finding 2:** A controlled diagnostic dataset with region‑specific gaze perturbations shows the cue’s effectiveness without relying on augmentation or memorization of generator fingerprints.  
- **Finding 3:** The same supervision improves vision‑language backbones (e.g., FakeVLM) and vision‑only models, revealing a backbone‑agnostic benefit.

## Methodology  
The authors constructed a dataset where only the gaze consistency between paired individuals is altered while all other visual attributes remain photometrically authentic. This creates a clean diagnostic signal that cannot be exploited by generators to memorize fingerprints. They employed **Block‑Compositional Caption Supervision**, which enforces a 5‑block reasoning skeleton across 1,250 macro‑combined captions, thereby decoupling surface diversity from underlying reasoning consistency. Validation was performed on multiple architectures: the vision‑language model FakeVLM, CLIP‑based backbones, and a pure vision model (Effort). The same supervision was applied to all models to test transferability.

## Results  
On the COCOAI Interaction subset, balanced accuracy rose from 67.8 % to 71.5 %, an increase of **+3.7 pp**. On the COCOAI Person subset, balanced accuracy improved from 83.0 % to 84.3 %, a gain of **+1.3 pp**. Crucially, both real‑class recall and fake‑class recall increased simultaneously, ruling out a “predict‑all‑fake” artifact. The improvement persists across architectures, confirming the cue’s robustness.

## Significance  
By introducing Social Gaze Consistency as a high‑level semantic cue, the paper advances detection methods that are less vulnerable to low‑level artifacts and generator‑specific fingerprints. This approach is scalable across diverse AI‑image generators (e.g., diffusion models) and can be integrated into existing vision‑language pipelines without retraining from scratch.

## Related Concepts  
Social Gaze Consistency, high‑level semantic cues, AI image generation artifacts, vision‑language models, block‑compositional caption supervision, CLIP prior preservation, diffusion family spectral weakness in periocular structure, paired‑edit shortcut blocking, hard‑to‑easy difficulty transfer.

[[2026-05-26_17-50-17Z_WhenEyesBetrayAI_SocialGazeConsistencyasaSemanticC.md]]