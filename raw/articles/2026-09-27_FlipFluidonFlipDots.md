---
title: Flip Fluid on Flip Dots
date: 2026-09-27
url: https://mitxela.com/projects/flipflip
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://mitxela.com/projects/flipflip
source_feed: Hacker News
ai_relevance: include
ai_topic: model-release
ai_reason: watchlist match: Meta Muse
scraped: 2026-09-27 09:12
---

# Flip Fluid on Flip Dots

## Full Article

[Back to Hardware]
FLIP Fluid on Flip Dots
24 Sep 2026
Progress: Complete
Here's the story of how I put a FLIP fluid simulation on a flipdot electromechanical display. FLIP stands for Fluid Implicit Particle, and yes, the primary motivation behind doing this was the wordplay.
It was built as an installation for EMF2026. This page will mostly focus on the technical details, but for the overview and demo of it working, watch the following youtube video.
Intro
Path to Some Panels
Connect the Dots
To KiCad
Second Circuit
Mounting Dreams
Panel Preparations
Prototype Polish
Framework
Decoder Boards
Power Supply
Joystick
Motherboard and Power Bus
Logo
The Event
Conclusion
Flippin' fluid simulations
For the last few years I've been building all kinds of fluid simulations, though the only things I've made videos about are the
volumetric display
and the
fluid pendant
.
While most of them are still secret (I'll publish them eventually) they all have a common deficit, that is, the LED liquid is utterly silent. I'd been wondering whether I could simulate some swishing noises when it occurred to me that an electromechanical display, such as flipdots, would make the noise for us. Realising that it would also make a great pun sealed the deal.
[flipdot display example]
But flipdot displays are crazy expensive. From what I can gather, there's only one manufacturer still in existence, and they have exclusive deals with a small number of artistic studios. Breakfast Studio is probably the most well known, and they aren't interested in talking to anyone with a budget of less than $50,000.
By pure coincidence, at one point I did a bit of contract work for a company that happened to own a big flipdot display, and I tried to convince them to let me play with it. I genuinely offered to forfeit my salary in exchange for putting a fluid sim on their display, and to my astonishment they turned me down. I guess that sealed it: I would have to do it the hard way.
Path to some panels
Asking around, especially at hackercamps, led to a bunch of interesting conversations. A lot of people are interested in flipdots. There was even talk of forming a collective and ordering newly made flipdot panels from China. Surely if anyone can produce these displays for cheap, it's someone in China. But the manufacturing process is remarkably complicated. Even the disks themselves are a sandwich of maybe six different materials – here I've dismantled one of the disks I eventually used:
[flipdot disk peeled apart]
It's not as simple as just a coil moves a magnetic part. The dots are non-volatile, so they hold their position when the power is removed. There are two permanent magnets (one inside the dot, above, and one in the base) and two cores which can be polarised to set the state of the dot.
Some people I spoke to had some of the new flipdot displays from AlfaZeta, but most people had old ones from eBay almost exclusively manufactured by Hanover, who still exist but no longer make these types of displays.
Aside: a number of my projects have been copied by people in China. If, after publishing this, some company in China starts churning out cheap flipdot displays I think we'll call that a win.
Eventually I got in contact with Sam, aka Look Mum No Computer. His
museum of obsolete technology
has put him in the enviable position of occasionally receiving cool donations of weird old tech, and one of these donations was an enormous pile of old flipdot displays. It's unclear if they are reclaimed from old buses, or were new-old-stock. A lot of them are in pretty poor condition, but that may just be from how they were stored. Sam's plan was to turn them all into one huge display, but doing that would be a monumental amount of work, for reasons that will become clear in a moment. He was very happy to let me have a few panels to play with, with the promise of more if I could come up with a good way of driving them.
Here's one of the panels:
[One of the starting flipdot panels]
I kept this one for spare parts as it had some impact damage near the edge. At the top right I've managed to unsolder one group of dots.
The date code is 2007, which is younger than I expected.
[Rear of the panel with protective sheet removed]
The rear of the panel had a protective sheet, which I've removed here.
Note the resolution is 13 by 28. The dots on this panel were manufactured in groups of seven, which is where the 28 comes from. The 13 is probably a result of the designer's affinity for prime numbers.
[Desoldered group of flipdots]
Connect the dots
The number one problem with these panels is that the circuit board protrudes over the edges, which means we can't tile them seamlessly in that direction.
The number two problem is that the existing drive circuitry is quite slow, taking about one second to update the display. The whole panel is wired up as one big matrix, which puts a limit on how fast we can update it.
Sam was able to get a bunch of the panels working with their original drive circuits, first building an
etch a sketch
and then a
bigger display
using a few of the panels. He mentioned that at least one other person had got them working with the original circuitry as well. But building one very wide display isn't enough, we want to tile them vertically too!
The person who got furthest is Mike from mikeselectricstuff, and
his flipdot video
was extremely informative, acting as my primary reference on how the dots work. The most interesting point is that while it takes around 60 milliseconds for a dot to flip over, it only needs a very short pulse to polarise the cores, maybe a millisecond at most.
Longer and higher voltage pulses can get the dot to flip slightly faster, but not significantly. One thought is that by using higher voltages, we can use shorter pulses, which would let us scan through the matrix faster. Taken straight from Mike's video, the matrix layout is something like this:
[Diagram of matrix arrangement]
To set the first dot, you'd set the first column either high or low, and then pulse the relevant row line. As I understand it, the original driver circuit would hold the column line in one state, pulse through each dot that needs to be set one way, then change the polarity of the column line and pulse all the remaining dots in the column, and then advance to the next column.
It may be possible to build a faster matrix by pulsing all of the dots in the column in just two goes. Hold the column line high, simultaneously pulse all the relevant rows, then hold the column low and pulse the others. If the pulses are one millisecond, we could potentially update all 28 columns in as little as 56 milliseconds, which is about as long as it takes for a dot to flip anyway.
There are two problems with this approach. One is that the power requirements are substantial. Each coil has a resistance of about 18 ohms, which would be 666mA at 12V. For faster pulses we might be looking at 15, 20 or 24V, with over an amp per coil. For these panels with just 13 rows, having a driver circuit which can push and pull 13 amps for every column is going to be tricky. The bigger panels would need even beefier parts.
We might be able to split it into multiple smaller matrices, but the next issue is that
any
matrix will have visible artefacts. Even though it takes tens of milliseconds for a dot to flip over, if different dots start flipping even slightly out of sync, there is a visual glitch as they progressively change. Even with small matrices of say 8x8, or even 4x4, when you flip the whole display, there would briefly be a kind of checkerboard as each matrix wipes over. For what I want to do, that's not acceptable.
Logically the next avenue to explore is desoldering all of the dots, and mounting them onto new circuit boards.
[Closeup of underside of group of dots showing the fine magnet wire]
We had some discussions about fast ways to do this but ultimately concluded that it's just not worth the time. The dots are so delicate, with tiny magnet wires and soft plastic that can melt, that it has to be done very carefully. Even with the very best desoldering equipment it would take forever. It's possible that pre-sawing the PCB into pieces would help; it's possible that a specific jig to melt a whole group of 14 pins at once would help; it's possible that we could try to abuse a wave soldering setup to speed it up... but remember, what we're trying to do here is build a fast flipdot display that's cheaper than the commercial offerings. After desoldering we've got the added labour of soldering them again to the new board. Unless our time has no value at all, this is going to end up very expensive.
[Closeup of the desoldered group of flipdots, with diodes on the row connections visible]
Mike's idea was to build a new circuit board that could solder directly onto the back of the existing boards. He found some very cheap H-bridge chips designed for driving small electric motors, which can run from 12V, don't need level shifting, and have built-in protection diodes. The parts have names like MX6208, BE6208, and LK6208, and one of them can drive a dot directly.
[MX6208 diagram from datasheet]
As you may expect if you've used motor driver chips before, the two inputs A and B are used to drive the outputs, with logic high and low corresponding to push and pull, but if A and B match then it either applies the brakes (setting both outputs to low) or allows it to freewheel (disabling both outputs). The datasheets conveniently give us the internal schematic and a truth table.
[MX6208 internal schematic and truth table]
These parts are SOIC-8 and rated for 0.5A continuous, so they can comfortably handle our pulses. The only real disadvantage of using them is that we'd need to cut all the column tracks on the existing PCB before soldering them down. Otherwise, the pulses would interfere with each other. (The diodes on the row connections mean we don't need to cut those.)
Mike was kind enough to give me his prototype boards as a starting point, and I spent a while studying them and thinking about our options.
[Mike's PCB on the back of a flipdot panel]
Typical of his designs it's filled with clever little details, like doubling up of the connector footprint so any of them can act as an input or output. Each shift register controls four dots, with the two inputs of each H-bridge directly controlled by the 8-bit shift registers. The latch and OE signals are tied together for simplicity.
The plan for these was to mount the whole panel in a small CNC mill, and use it to cut all the traces. Given that the edges need to be cut off too, this wouldn't be too inconvenient, if not for the fact I don't have a small CNC mill. Before cutting all the traces manually I tried to explore some more options.
Another technique for driving the dots involves using a series capacitor. There's a
nice project here
that uses the technique to build a new filpdot display. The advantage is that you don't need a full H-bridge per dot, only a single half-bridge.
[Schematic of capacitor technique]
When the bridge goes high, a pulse is sent through the capacitor which flips the dot. The capacitor then stays (or is held) fully charged, until the bridge pulls it low again, creating an inverse pulse that flips it back.
Of course it's not actually as simple as that, to control the high side from logic level signals we'd need another transistor.
[Schematic of capacitor technique with level shifting]
Naturally we'd use mosfets for the real thing. The linked project uses three mosfets and three pull resistors for every dot, in addition to the big capacitor. The biggest risk with building your own half bridge is the chance of turning both top and bottom switches on at the same time, which would cause it to explode. Another big downside is that having multiple discrete components takes up a lot of board space. The linked project uses a dedicated microcontroller for each group of seven, on a four layer board, and doesn't need to contend with soldering onto the back of an existing board.
In contrast the H-bridge chips are a self-contained solution, and combined with the very cheap 595 shift registers, Mike's board is much cheaper and simpler than the capacitor technique above.
But one thing about it really appealed to me: if one pin of each dot is grounded, we won't need to cut any traces. All of the column lines can be connected to ground. This also means we won't need to do as much soldering.
I did some test board layouts and found that we really don't have much space to work with. Certain areas of the PCB need to be empty to avoid shorting with pads on the original board, and we also need to leave space for mounting holes. Even if I wanted to do it with discrete components I'm not sure I could fit it. Thus began my search for a
cheap
, small half-bridge.
The first thing I looked at were gate drivers, these are dedicated devices for overcoming the capacitance of big mosfet gates. They usually have level shifting for us, and work like an isolated half-bridge that can momentarily deliver a huge pulse of current. Unfortunately, even the very cheapest ones are about twenty times the cost of those H-bridge chips. That'll compound when we scale up to thousands of dots.
Some of those gate drivers are available in SOT-23 packages, which would help a lot when it comes to board layout. There are also H-bridge chips available in SOT-23, but unlike the SOIC-8 parts they don't seem to have a standardised footprint. I compared dozens of them and found that nothing was perfect, nothing gave me confidence. I also looked at various "relay drivers" which had their own pros and cons.
Some shift registers have built-in output FETs that let them low-side switch a load directly. What I'd love would be a shift register with high-current push-pull outputs at a suitable voltage, but as far as I can tell nothing like that exists. There are high voltage shift registers if we go back in time to early CMOS technology like the 4000 series. A CD4094 shift register could work at 12V, but, the output capability is negligible, we'd be lucky to pull 10mA from it.
More options: there are buffer chips that could work in the ranges we expect. I found a few that would work electrically, but again, the price made them impractical, and most of them have footprints that'd be difficult to work with.
The idea of using one H-bridge to control a pair of dots was appealing but unfortunately not possible, because of their brake and freewheel conditions. However, given that the parts are so cheap, and we were planning on using one per dot originally anyway, would it be crazy to use them in a single ended fashion, ignoring one of the outputs?
[Truth table for MX6208 again]
It's not as easy as it sounds. Studying that truth table, if we send our signal to AIN, and hold BIN low, then AOUT would go high-impedance when AIN is LOW. If we hold BIN high, then AOUT would only ever be low. But if we send our signal to BIN, and keep AIN high, then the output will toggle high and low correctly (even if the part thinks this is a brake condition).
To see if this was even close to viable I built a test setup on some protoboard.
[Prototype dots on a breadboard with protoboard shift register and H-bridge chips driving it]
We have a 595 shift register, the H-bridge chips wired in single ended fashion wth AIN tied high. The capacitors are multilayer ceramic 100uF which were all I had to hand in the right ballpark. A nice bonus of wiring it up this way is that we can now drive eight dots from one shift register, so that's half the number of shift registers and half the data that needs to be clocked out.
[Closeup of driver chips and capacitors]
One of the lesser concerns with the capacitor method is that of self-discharge. I assumed this wouldn't be a problem because we can simply leave the outputs powered. No current should flow through the capacitor except enough to keep it at full charge. Unfortunately these chips are not built from FETs, but BJTs, so I soon realised that that was a mistake. When an output is enabled, even if unconnected, the chip consumes about 24mA simply because of the base currents through the transistors. Multiply that by a few thousand dots and we have a quiescent current that could kill the project.
Evidently we still need to pulse the signal then. If capacitor discharge is an issue, we can always periodically re-pulse it. Again looking at the truth table, we can use the AIN signal as an enable pin. I decided to tie this to the latch signal for the shift register. A minor benefit of the BJT inputs is that we don't need pulldown resistors: when the shift register's output is disabled, the H bridge inputs are effectively low.
[Breadboard prototype with OE/latch signal added]
With this I felt like we were finally getting somewhere.
A neat thing about the series capacitor is that it comes with some inherent safety. If a glitch occurred with the direct drive method, it could hang with full current flowing through the coils, eventually overheating, maybe combusting. This circuit comes with far fewer ways in which it could conflagrate.
The choice of capacitor is important, those big ceramic ones weren't going to fit on our PCB. I adapted the prototype so I could stick various different capacitors in and see how they compare. An interesting thing about the 100uF ones is that only after the fact did I notice they were rated for 6.3V, and I'd been pulsing 12V through them. Using some 10uF, 16V rated ones gave a noticeably worse performance. I can't say I really understand the physics of ceramic capacitors, I know that the capacitance is a function of the bias voltage so already it's a bit of a mind screw. If we pulse a capacitor above its voltage rating does it reduce its lifetime? Probably. Cost is a factor here, with standard sized capacitors being significantly cheaper than speciality ones, and it's really gonna add up later on. I concluded that two 10uF capacitors in parallel would probably be enough, and then we can use standard 0805 packages for them.
Another thought: does the series resistance of a ceramic capacitor depend on its physical dimensions? A 10uF ceramic is available in various footprints at different costs, so there must be some difference in the technology used to shrink them. Instead of idly wondering, it was time to throw our first PCB together.
To KiCad
These flipdot panels have a pin pitch of 15.24mm, or six tenths of an inch. The board supporting them has test pads or an unpopulated footprint in the corner next to each one, so we'll stick a keepout around that. I created a flipdot symbol and footprint which we can lock into position on the board.
But KiCad is really not very good at this sort of design, where we have lots of repetition. Unlike some other EDA software, there isn't a clear idea about forwards and backwards annotation. The original process was to create a schematic, export a netlist, and then import that netlist to the PCB editor. Newer versions have streamlined it to add an "update PCB from schematic" button, and in the latest versions there is even some attempt to add UUIDs to symbol-component pairs, but so far it's still a little janky.
The fundamental problem as I see it is that the auto annotation is useless. If you copy and paste some schematic symbols, you have a choice to leave them unannotated (so resistors have labels like R? instead of R3, etc) or to reannotate them based on their position (so resistors would be annotated based on the first free identifiers, in a left-to-right, top-to-bottom fashion). If you copy and paste parts on the PCB, you get the same options, but those are almost never helpful choices, because it's unlikely that the schematic and PCB will have the same physical layout. The effect is that if you copy and paste anything but the most trivial circuits, the schematic and PCB get annotations that don't match.
I did file an issue about this but I think I failed to convey exactly what I wanted and it got buried among a thousand other issues. The way it should behave – by default, if you ask me – is to re-annotate based on a predicable method that is independent of geographic layout. The most simple option would be to re-annotate in the same order as the source parts. So if you had R1, R2 and R3, they would become R4, R5 and R6 regardless of which one is to the left or the right.
There is a plugin for duplicating layouts, but the approach they use is different to what I wanted to achieve here. What I wanted, and what KiCad
can
do once it was fought into submission, is a single schematic file that describes one row of dots, and a single hierarchical file that links copies of that row together. If we edit the row, all of them change and the netlist used by the PCB editor reflects that.
Frustratingly, the newly added UUID system makes it even harder to get this to work, but with enough wrangling and a little bit of python I got there in the end. The overview looks like this:
[Hierarchical arrangement of dot rows]
And the
dotrow.kicad_pcb
is of this sort of persuasion:
[Partial schematic for one row of dot drivers]
There I've highlighted the latch signal going to AIN of each driver. The two 10uF capacitors are in parallel before each dot. If we open the same schematic for the next row, the layout is identical but the annotations are all different.
I based the PCB layout loosely on what Mike did, adding the dual footprints for serial data and some mounting holes, which I carefully checked would not interfere with any tracks on the underlying PCB. I extended this to 13 rows, so it would cover the full height of a panel.
[KiCad Screenshot of first PCB design]
Horizontally, we cover eight dots, so we'll need three and a half of these to drive one full panel of 28 columns. That's a bit awkward but we can deal with it later, for now I just wanted to confirm the ideas. While I waited for the circuit boards to arrive I made this 3D printed fence for a dremel with a diamond wheel, so we can efficiently cut away the old driver circuitry.
[Using the dremel with 3d printed fence to cut off excess circuit board]
The cut distance is different for the top and bottom of the circuit, which is slightly awkward but when it comes to preparing all of the panels, we can do all of the tops first, readjust, and then do all the bottoms.
When the circuit boards arrived, we held our breath as we soldered the 117 pins necessary (13 x 8, plus 13 grounds).
[First PCB soldered onto the back of a flipdot panel]
Initial results were mixed.
Flipping individual dots worked, but flipping all of them at once would fail. If each dot needs a pulse of around half an amp to flip, then flipping all of those would be about 50 amps, if only for a millisecond. As the power supply couldn't cope, the voltage drops, and the pulses become weaker. Instead of polarising the cores, they simply demagnetise the cores, and the dots go slack.
I noticed early on that the behaviour at lower voltages was significantly different with different series capacitors. Limiting our selection to 0805 ceramics, even doubled up, was probably a mistake, as they seem to suffer more from the undervoltage condition than a single big capacitor.
Another issue is that the inputs to the H-bridge chips draw significant current. The input is the base of a BJT, so unlike CMOS parts it will draw a few milliamps, and multiplied by a few hundred means the latch signal now needs more current than can be provided by a simple GPIO pin. I was driving this from a basic CH32V003 breakout board that was struggling to keep up. No worries, we can bodge in a mosfet to boost the current.
[P-channel mosfet fitted to latch signal]
That's a P-channel mosfet (FDN338P) on one of the unused connector footprints, with its gate connected to the OE signal. This suits me fine, we were already toggling the OE and latch signals alternately. This also saves us one pin on the connector.
I went with JST ZH connectors (1.5mm pitch) partly because I already had a pile of ready-made cables. These cables turned out to be just slightly too short, and I had to manually extend them...
[First three boards soldered onto the back of the panel]
The white wire is the former latch signal, which I've disconnected as it made sense to stick a mosfet on each of the panels.
I noticed an asymmetry: it's easier to flip in one direction than the other. You might think it's to do with the capacitor arrangement, but counterintuitively flipping from high to low is faster. Simply due to the physics of transistors, the low-side switching can sink more current than the high side can source. Another way of thinking about it is if we'd driven the coils directly from the H-bridge, the flipping would be symmetrical, but only because both directions would be limited by how much current can be sourced on the high side.
With more of the dots active, the dependency on a decent power supply w

## Metadata
- **Source**: [Original Article](https://mitxela.com/projects/flipflip)
