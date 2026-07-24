# Summary: 2026-07-22_14-28-28Z_surprisalisNotaTheory.md
Saved: 2026-07-24 02:00
Source: 2026-07-22_14-28-28Z_surprisalisNotaTheory.md
Model: None

---

## Summary  
This paper challenges the notion that surprisal—defined as the negative log-likelihood of a sequence under a language model—can serve as a universal, representation-agnostic measure of cognitive processing in computational psycholinguistics. The authors argue that despite its widespread use, surprisal is not a theory but rather a metric whose interpretation depends heavily on underlying algorithmic and representational choices. They contend that large language models (LLMs) do not bypass the need for explicit representational commitments; instead, their probabilistic outputs are shaped by architectural decisions that obscure the true nature of model behavior. The paper calls for a reevaluation of how surprisal is applied in research involving LLMs, emphasizing that treating model probabilities as interchangeable risks misrepresenting both computational and cognitive theories.

## Key Contributions  
- [Finding 1] Surprisal cannot be treated as a theory because it relies on specific algorithmic implementations rather than abstract representational principles.  
- [Finding 2] The architecture of language models, including attention mechanisms and layer depths, significantly influences the computation of model probabilities and thus their surprisal values.  
- [Finding 3] Researchers must distinguish between computational-level metrics like surprisal and cognitive-level theories, avoiding conflation that obscures representational commitments.

## Methodology  
The authors conducted three empirical analyses to examine how different language model architectures produce varying surprisal outputs for the same input sequences. These models varied in size, attention depth, and training regimes, allowing them to isolate the impact of architectural choices on probability computation. By comparing surprisal across these models with identical inputs, they demonstrated that algorithmic differences—not just representational content—drive observed variations in surprisal. The study also included theoretical comparisons to highlight how computational-level narratives may misattribute model behavior to cognitive processes.

## Results  
The results showed that even when input sequences are semantically and syntactically identical across models, their surprisal values differ substantially due to differences in model architecture and training dynamics. For example, a larger model with deeper attention layers generated higher surprisal for the same sentence than a smaller, shallower model, despite producing nearly identical output probabilities. Additionally, the authors found that surprisal is not invariant under minor perturbations in input sequences when model architectures differ, further underscoring its dependence on computational structure rather than content alone.

## Significance  
This work matters because it calls into question the epistemological foundation of using surprisal as a proxy for cognitive processing in psycholinguistic research. By revealing that surprisal is algorithmically contingent, the paper undermines claims of representation-agnosticism and highlights the need for methodological transparency. It encourages researchers to move beyond black-box evaluation and instead consider how model design shapes probabilistic outputs—thereby aligning computational metrics with their theoretical interpretations.

## Related Concepts  
- Surprisal (negative log-likelihood)  
- Language models (LLMs)  
- Computational psycholinguistics  
- Representation-agnostic research  
- Algorithmic determinism in model output  
- Black-box AI systems
