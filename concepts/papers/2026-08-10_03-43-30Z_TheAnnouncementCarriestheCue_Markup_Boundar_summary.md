# Summary: 2026-08-10_03-43-30Z_TheAnnouncementCarriestheCue_Markup_Boundaries_and.md
Saved: 2026-08-10 23:35
Source: 2026-08-10_03-43-30Z_TheAnnouncementCarriestheCue_Markup_Boundaries_and.md
Model: None

---

## Summary  
The paper argues that the way a document’s markup and boundary cues are encoded in pre‑training corpora is an unmeasured training variable that can profoundly affect model performance, yet it is never recorded on dataset cards. By defining “clean‑window survival” as a deterministic measure of how much text still requires boundary inference after conversion, the authors quantify notation across three dimensions: what corpora carry, what readers use, and what writers impose. Their work reveals that the presence or absence of an announcement (e.g., paragraph breaks) is more influential than the actual sigil itself, and that this cue should be recorded as a format operator rather than preserved for fidelity. The contribution is both methodological—introducing a new metric and a reproducible data‑card schema—and substantive: it shows how annotation choices shape model training.

## Key Contributions  
- [Finding 1] Clean‑window survival drops to 0.153 in vision‑converted PDF slices versus 0.889 in C4, indicating that long stretches of unmarked text are the scarce resource rather than outright missing markup.  
- [Finding 2] Deleting a structural announcement makes subsequent prose measurably harder to predict across models from 0.6B to 8.2B parameters, while merely swapping its notation has no effect.  
- [Finding 3] Base models do not automatically re‑insert announcements when they are removed; the “bounded null” is preserved at a rate indistinguishable from zero against an authored reference of zero.

## Methodology  
The authors surveyed thirteen public corpora, converting PDFs to text and measuring survival on both marked and unmarked slices. They also conducted a pre‑registered supply test using five base models and two pipelines to compare prediction difficulty before and after announcement removal. A sidecar format was created where every announcement is deleted into a reversible auxiliary file, allowing mixed training of the pure frame (paragraphs in authored order) against the marked copy with or without announcements.

## Results  
Survival statistics confirm that unmarked text is abundant but long stretches are rare; prediction difficulty rises when announcements are omitted. The sidecar‑mixed approach yields a clean training set where the only variable is announcement presence, not notation. Across all models, deleting an announcement reduces survival by ~0.73 (from 0.889 to 0.156), whereas altering its visual form leaves prediction unchanged.

## Significance  
Understanding that annotation cues—not just the text itself—drive model behavior is crucial for reproducible research and fair dataset evaluation. By treating these cues as trainable variables, researchers can design experiments that isolate their impact, improving both model training efficiency and the transparency of data cards.

## Related Concepts  
- Clean‑window survival metric  
- Pre‑training corpus annotation  
- Boundary inference  
- Format operators  
- Sidecar format for reversible markup deletion
