# Summary: 2026-07-14_17-53-22Z_Audio_NativeSpeechRecognitionwithaFrozenDiscrete_D.md
Saved: 2026-07-15 00:01
Source: 2026-07-14_17-53-22Z_Audio_NativeSpeechRecognitionwithaFrozenDiscrete_D.md
Model: None

---

## Summary  
The paper proposes an audio‑native speech recognition system that leverages a frozen discrete‑diffusion language model to generate full transcripts in parallel, contrasting sharply with the token‑by‑token autoregressive decoders that dominate current research. It trains DiffusionGemma, a 26 B mixture‑of‑experts model, using uniform random‑token diffusion and a lightweight Whisper encoder as an acoustic source. A frozen MoE backbone is adapted via low‑rank adapters and a connectionist temporal classification loss to incorporate the new audio modality. The approach achieves a 6.6 % word error rate on LibriSpeech clean test data across English, Hindi, and Mandarin with only eight parallel denoising steps.

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Introduces an audio‑native interface for diffusion language models that refines the entire transcript in parallel rather than sequentially emitting tokens.  
- [Finding 2] Shows that a frozen MoE backbone can be effectively adapted to new modalities using low‑rank adapters and a temporal classification loss, overcoming gradient deadlock.  
- [Finding 3] Demonstrates competitive performance (6.6 % WER) with minimal parameter overhead (0.16 % of the backbone) across multiple languages.

## Methodology  
The authors train DiffusionGemma using uniform random‑token discrete diffusion, a design that differs from absorbing‑mask schemes used in recent diffusion models. Acoustic features are extracted by a frozen Whisper encoder, projected into the model’s embedding space with a lightweight projector, and fed to low‑rank adapters that enable the MoE to attend to the new modality. To break the deadlock where gradients cannot reach the acoustic input, a connectionist temporal classification loss is applied through a frozen output head, ensuring the audio information influences generation.

## Results  
The model reaches 6.6 % word error rate on LibriSpeech clean test set, with consistent performance across utterance lengths and languages. It requires only eight parallel diffusion steps to produce a full transcript, and a single adapter trained on six source languages is evaluated on English, Hindi, and Mandarin, showing robust multilingual capability.

## Significance  
This work offers a scalable, low‑overhead alternative to autoregressive decoders, enabling real‑time transcription with minimal additional training cost. By freezing the massive MoE backbone and using only a few hundred thousand trainable parameters, the approach reduces inference latency while supporting diverse languages, which is crucial for deployment in resource‑constrained environments.

## Related Concepts  
Discrete diffusion language models, mixture‑of‑experts (MoE) architectures, frozen backbones, projection layers, low‑rank adapters, connectionist temporal classification loss, Whisper encoder, token‑wise denoising steps.
