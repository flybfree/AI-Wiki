# Summary: 2026-07-22_22-38-16Z_HARP_TheHuman__AIResearchPlatform.md
Saved: 2026-07-24 02:18
Source: 2026-07-22_22-38-16Z_HARP_TheHuman__AIResearchPlatform.md
Model: None

---

## Summary  
The paper introduces HARP, a platform that enables systematic study of human‑AI interaction using live AI agents in controlled mock scenarios. It allows researchers to manipulate agent prompts and model parameters while capturing fine‑grained behavioral data such as prompt composition time and response latency. By integrating self‑report measures with recorded interactions, HARP provides a comprehensive toolkit for testing how design choices affect user experience. The authors demonstrate this capability in a study on the impact of technical specificity and response length on LLM output retention.  

## Key Contributions  
- HARP creates a modular research platform that decouples AI agent configuration from experimental control, enabling systematic variation of prompts, model parameters, and response characteristics.  
- It captures both quantitative behavioral metrics (prompt composition time, keystroke pauses, latency) and qualitative self‑report data, offering a mixed‑methods approach to human‑AI interaction studies.  
- The platform’s planned multimodal extensions—voice, facial expression, gesture, and emotion analysis—extend classic HCI methods into embodied AI testing.  

## Methodology  
The authors designed HARP as a web‑based interface that runs in a browser, allowing researchers to set up a mock scenario with a live LLM agent. They configure the agent’s prompt template, model temperature, maximum token limit, and response style (e.g., concise vs. verbose). Throughout the session, participants interact via text input while the system logs keystroke timestamps, pause durations, and deletion events. At predefined checkpoints, the platform triggers surveys to collect self‑report measures of comprehension, confidence, and retention. The authors also outline future extensions for multimodal sensing.  

## Results  
In the pilot study, participants exposed to concise technical responses (short, jargon‑heavy) retained 42 % of information after a 5‑minute delay, whereas those receiving verbose explanations retained only 18 %. Response latency averaged 0.73 seconds per token, and average prompt composition time was 1.9 seconds. Participants reported higher confidence in concise answers but lower perceived usefulness. The platform successfully recorded these metrics across multiple runs with <5 % variance.  

## Significance  
HARP bridges the gap between static prototype testing and live AI interaction, providing a reproducible framework for evaluating how design choices influence user cognition and behavior. By integrating behavioral logs with self‑report data, it offers richer insights than traditional usability studies. The platform also paves the way for multimodal research that can assess affective responses to AI outputs.  

## Related Concepts  
- Large Language Models (LLMs)  
- Human‑Computer Interaction (HCI)  
- Usability testing  
- Prompt engineering  
- Mixed‑methods research  
- Multimodal sensing
