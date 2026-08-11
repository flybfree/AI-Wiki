# Summary: 2026-08-08_22-09-52Z_Dramarrator_Object_BasedAudioEditingforAudioDramaP.md
Saved: 2026-08-10 23:10
Source: 2026-08-08_22-09-52Z_Dramarrator_Object_BasedAudioEditingforAudioDramaP.md
Model: None

---

## Summary  
This paper introduces Dramarrator, an object‑based audio editing tool designed to streamline the creation of audio dramas from books. By treating narrative elements such as characters, scenes, and sound cues as editable objects, Dramarrator automatically generates linked speech, effects, and music tracks that can be edited in a single timeline. The system eliminates manual re‑synchronization after changes, reducing the labor required for adaptation. Experimental studies demonstrate that Dramarrator lowers task load for professional creators and produces output comparable to high‑quality productions using existing tools.

## Key Contributions  
- Finding 1: Dramarrator represents story elements as object‑based assets, enabling automatic generation of linked audio components.  
- Finding 2: The tool’s edit‑propagation mechanism ensures that modifications to any object instantly update all dependent assets without manual intervention.  
- Finding 3: User and listener studies show a significant reduction in task load for creators and comparable narrative quality for audiences.

## Methodology  
The authors approached the problem by first mapping the book’s narrative structure into a set of reusable objects, then using an audio generation pipeline to synthesize speech, sound effects, and music that are linked through object references. The system was integrated with a timeline editor where each object can be edited independently; changes trigger updates across all related assets via a dependency graph. Experiments were conducted in two phases: (1) a user study measuring task load for eight professional creators, and (2) listener studies comparing output quality.

## Results  
In the creator study, Dramarrator reduced average editing time by 45 % compared to manual assembly of separate audio tracks. The listener study with 300 participants found that drama scores were statistically indistinguishable between Dramarrator‑refined productions and those created with traditional professional tools (p > 0.2). An exploratory study with three creators indicated lower perceived learning curve and broader applicability beyond pure audio dramas.

## Significance  
Dramarrator addresses a persistent bottleneck in audio‑drama production by automating the interdependent workflow of asset creation and editing, thereby accelerating adaptation from text to sound. Its object‑based paradigm offers a scalable solution that could be extended to other media‑rich storytelling formats, fostering faster iteration and lower entry barriers for creators.

## Related Concepts  
object‑based audio editing, dependency graph, automatic asset generation, timeline authoring tool, audio drama production, edit propagation, user study, listener study, narrative mapping.
