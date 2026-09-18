# Summary: 2026-09-18_OpenJev.md
Saved: 2026-09-18 05:27
Source: 2026-09-18_OpenJev.md
Model: freedomaisvr/gemma-4-12b-it

---

## Summary
OpenJev is a live, local experiment designed to test whether large language models (LLMs) can perform decision-making tasks directly within a web browser using the user's own GPU. The project specifically compares two methods of inference: "direct readout" (extracting raw probability logits from the model) versus "token generation" (asking the model to produce a JSON representation of those same probabilities). By running these processes locally, the tool provides a transparent look at how models process choices without relying on external backends or cloud infrastructure.

## Key Takeaways
- **Browser-Based Inference:** The project utilizes quantized weights (via wllama) and Hugging Face's model library to run inference entirely in the browser, ensuring that user inputs never leave the local environment.
- **Comparative Methodology:** It pits "Direct Readout" (soft-maxing probabilities across provided options without decoding) against "JSON Generation" (token-by-token output of the same distribution), measuring the wall-time ratio between the two methods.
- **Hardware-Specific Scaling:** The tool offers different model tiers—ranging from a 0.6B model for mobile devices to a 4B model for high-end desktops—to demonstrate how hardware constraints affect inference speed and accuracy.
- **Quantized Performance:** The experiment acknowledges that while quantization allows for local execution, it can significantly alter both the quality of the output and the speed of the inference compared to full-precision models.

## Context
This project sits at the intersection of "Local AI" and "Privacy-Preserving Inference." As the industry moves toward more private interactions, there is a growing need to run models on edge devices (phones, laptops) rather than centralized servers. OpenJev contributes to this by exploring the technical feasibility of complex decision-making tasks—which usually require high-compute environments—on consumer hardware using browser-based execution.

## Implications
The implications for the AI field are significant regarding both privacy and the democratization of AI. By proving that sophisticated inference can happen in a browser, it paves the way for applications where data privacy is paramount (e.g., personal assistants or private data analysis) because no information ever reaches a server. Furthermore, by providing a side-by-side comparison of "readout" vs. "generation," the project helps researchers understand the efficiency trade-offs between raw model output and structured text generation, which is critical for optimizing inference costs in production environments.
