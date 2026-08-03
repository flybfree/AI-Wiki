# Summary: 2026-08-03_IntroducingInkling-Small.md
Saved: 2026-08-03 10:28
Source: 2026-08-03_IntroducingInkling-Small.md
Model: qwen3.6:35b

---

## Summary
Thinking Machines has officially released Inkling-Small, an efficient open-weights model that delivers performance comparable to its larger predecessor, Inkling, while utilizing only a quarter of the parameters. This Mixture-of-Experts transformer features 276 billion total parameters with 12 billion active during inference, trained on advanced NVIDIA GB300 NVL72 systems. The release highlights a significant advancement in balancing computational efficiency with high-level reasoning capabilities across audio, image, and text modalities.

## Key Takeaways
- Inkling-Small achieves competitive performance against the larger Inkling model (975B total parameters) on critical benchmarks such as Terminal-Bench 2.1, Humanity's Last Exam, and IFBench, despite having significantly fewer active parameters.
- The model supports variable thinking effort, allowing users to dynamically adjust computational resources to balance cost and performance, making it highly adaptable for diverse use cases ranging from minimal to extreme reasoning tasks.
- It demonstrates superior efficiency compared to other open-weights models in its weight class, offering a compelling alternative for developers seeking high-performance AI without the prohibitive costs associated with larger parameter counts.

## Context
The rapid evolution of large language models has traditionally favored scaling laws where increased parameters correlate directly with improved performance. However, this trend has led to substantial computational and financial barriers for widespread adoption. The introduction of Inkling-Small reflects a growing industry shift toward optimizing Mixture-of-Experts architectures to maximize efficiency. By leveraging advanced hardware like NVIDIA GB300 NVL72 systems, Thinking Machines addresses the critical need for models that can handle complex, multi-modal reasoning tasks without requiring exorbitant computational overhead. This aligns with broader trends in the AI community focusing on sustainable and accessible model deployment.

## Implications
This release significantly impacts the AI industry by democratizing access to high-performance reasoning models. For enterprises and developers, the ability to achieve near-state-of-the-art results with reduced active parameters translates to lower inference costs and faster response times. This efficiency enables more scalable deployment of agentic tools and complex reasoning applications in resource-constrained environments. Furthermore, the open-weights nature of Inkling-Small fosters greater transparency and innovation within the community, allowing researchers to build upon a robust foundation without licensing restrictions. Ultimately, this advancement accelerates the practical integration of advanced AI capabilities into real-world applications, making sophisticated reasoning tools more accessible and economically viable for a broader range of users.
