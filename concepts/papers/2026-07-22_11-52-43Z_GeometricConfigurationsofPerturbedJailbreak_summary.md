# Summary: 2026-07-22_11-52-43Z_GeometricConfigurationsofPerturbedJailbreakPrompts.md
Saved: 2026-07-24 01:48
Source: 2026-07-22_11-52-43Z_GeometricConfigurationsofPerturbedJailbreakPrompts.md
Model: None

---

## Summary  
This paper investigates how string‑level perturbations that transform unsuccessful jailbreak prompts into successful ones are represented internally within small‑weight versions of Qwen‑2.5 and Llama‑3.2 large language models. By examining two distinct embedding spaces—the last‑layer‑last‑token space and the top‑50 next‑token probability space—it discovers that neither space separates compliant from refusal answers along a simple hyperplane, indicating that jailbreak success is not governed by a single linear decision boundary.

## Key Contributions  
- [Finding 1] The authors find no behavioral hyperplane in either representation space, meaning the data do not cluster cleanly into “compliant” versus “refusal” groups.  
- [Finding 2] In the Qwen‑2.5‑1.5B model, the next token “Sure” shows a strong statistical association with compliant responses.  
- [Finding 3] In Llama‑3.2 models, both tokens “,” and “ĊĊ” are similarly linked to compliant outputs.

## Methodology  
The authors selected two representation spaces for analysis: (1) the last‑layer‑last‑token embedding space, which captures spelling and format information, and (2) the top‑50 next‑token probability space, a one‑dimensional view of token likelihoods. They applied these embeddings to a set of perturbed jailbreak prompts that were labeled as either “refusal” or “compliant.” The analysis focused on small‑weight model variants—Qwen‑2.5‑1.5B/3B/7B‑Instruct and Llama‑3.2‑1B/3B/3.1‑8B‑Instruct—to isolate the influence of internal representations.

## Results  
Across both spaces, the response set is dominated by refusals, yet no hyperplane separates the two classes. The only significant deviations are token‑level: “Sure” in Qwen‑2.5‑1.5B and “,” / “ĊĊ” in Llama‑3.2 models correlate with compliant answers. This suggests that compliance is driven by specific token patterns rather than a global geometric boundary.

## Significance  
The findings reveal that jailbreak mitigation cannot be understood as a simple linear classifier operating on full prompt embeddings; instead, subtle token associations dictate outcomes. This insight challenges existing safety frameworks and highlights the need for more nuanced, representation‑aware defenses against adversarial prompts.

## Related Concepts  
Jailbreak prompts, LLM safety, perturbation techniques, embedding spaces (last‑layer‑last‑token, next‑token probability), behavioral classification, hyperplane separation, token‑level association.
