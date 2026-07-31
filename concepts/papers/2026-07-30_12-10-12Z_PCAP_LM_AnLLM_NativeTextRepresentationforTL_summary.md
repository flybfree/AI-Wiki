# Summary: 2026-07-30_12-10-12Z_PCAP_LM_AnLLM_NativeTextRepresentationforTLSBulkTr.md
Saved: 2026-07-30 20:35
Source: 2026-07-30_12-10-12Z_PCAP_LM_AnLLM_NativeTextRepresentationforTLSBulkTr.md
Model: None

---

## Summary  
PCAP‑LM is an LLM‑native text representation designed for TLS bulk traffic analysis, converting raw capture files into concise semantic summaries. It uses a custom ASCII alphabet called PacketGlyphs to encode packet direction, TCP/TLS state, log‑scale size and inter‑packet delay. By applying a constrained PMI‑BPE tokenizer together with motif run‑length encoding, the representation aggressively collapses repetitive patterns while preserving an @REFS side‑index for lossless drill‑down.  

## Key Contributions  
- [Finding 1] The PacketGlyphs alphabet and its integration into a PMI‑BPE tokenizer enable a 812× size reduction of TLS bulk captures, fitting entire files within a single LLM context window.  
- [Finding 2] A forensic question‑answering benchmark shows that a frontier LLM achieves 99.3% accuracy on PCAP‑LM documents versus only 51.0% when using an equivalent token budget from tshark -V, demonstrating superior reasoning capability.  
- [Finding 3] The lossy design introduces a known blind spot: TCP retransmissions are missed with roughly 24% false‑negative rate, highlighting the trade‑off between compression and completeness.  

## Methodology  
The authors approached the problem by first defining PacketGlyphs as an ASCII alphabet that simultaneously encodes four attributes of each packet: direction (inbound/outbound), protocol type (TCP/TLS), log‑scale size, and inter‑packet delay. Raw PCAP files are transcoded into a sequence of these glyphs, which is then processed through a constrained PMI‑BPE tokenizer to produce a compact vocabulary. Repetitive behavioural motifs are collapsed using run‑length encoding, while an @REFS side‑index maps each glyph back to its original packet for lossless reconstruction.  

## Results  
Experimental evaluation on a homogeneous corpus of 5G/4G TLS 1.3 bulk‑download traffic demonstrates that the BPE vocabulary saturates at 159 tokens, achieving an 812× reduction in size compared with tshark -V output and fitting entire captures within one LLM context window. In a forensic question‑answering task on 30 held‑out files, a state‑of‑the‑art LLM attains 99.3% accuracy using PCAP‑LM documents versus 51.0% when fed the token‑budgeted tshark -V prefix. The lossy representation also incurs a 24% false‑negative rate for TCP retransmissions, indicating that some packet events are omitted.  

## Significance  
This work matters because it bridges the gap between raw network capture data and LLM reasoning by providing a compact, semantic text form that fits within typical context limits. By enabling faster analysis of massive TLS traffic without sacrificing too much interpretability, PCAP‑LM can accelerate security investigations and anomaly detection in real‑time environments.  

## Related Concepts  
- Large language models (LLMs)  
- Context window constraints  
- Token‑budget matching  
- Lossy compression  
- PacketGlyphs ASCII alphabet  
- PMI‑BPE tokenization  
- Run‑length encoding  
- @REFS side‑index
