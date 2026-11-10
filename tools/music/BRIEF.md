# Pipeline: nine stage songs (brief for the composer agents)

The 404 page of enCloud9's new site has a Snake-style game called Pipeline. You steer a pipe that catches leads (people icons) and deals (white diamonds).
It has nine levels, named after the stages of a sales pipeline. Each stage gets its own song:
1 Prospecting, 2 Qualifying, 3 Discovery, 4 Demo, 5 Proposal, 6 Negotiation, 7 Contract, 8 Closing, 9 Closed won.

## The sound Michael wants
Inspired by the FEEL of "The Rain Formerly Known as Purple" by Chris Christodoulou (Risk of Rain 2 soundtrack):
electronic, synth-heavy, a bit prog: driving arpeggiated synth sequences, a thick filtered saw bass, punchy electronic drums,
big pads, builds that open up, cool and moody rather than cute. He said earlier versions were "too high pitched": keep it
mid and low; nothing shrill. Use web search to understand the style if you like.
STYLE ONLY. Do not copy or quote any melody, riff or chord sequence from that track, from Prince's "Purple Rain", or from any
other existing song. Every melody, bassline and progression must be your own.

## The arc across the nine stages
Each stage is its own song with its own key, tempo, groove and character, but they belong to one soundtrack.
Stage 1 is the calmest and most open; each stage adds energy and density; stage 9 is the big finale.
Tempo range overall about 100 to 150 bpm. Odd meters (7/8, 5/4) are welcome on one or two stages if they groove.

## Technical contract (must follow exactly)
- Write one file per stage: /tmp/songs/stageN.js containing exactly one assignment `SONGS[N]={...}` (N = 1..9). Plain ES5 JavaScript, no imports, no globals other than SONGS, no Math.random-free requirement (randomness is fine for variation but the song must sound good every loop).
- See /tmp/songs/stage0.js for the shape and /tmp/songs/engine.js for exactly what the helpers do. Read both fully before writing.
- Fields: name (the stage name above), title (your track's own title), bpm, steps (loop length in sixteenths; make the loop 8 to 16 bars long so it does not feel repetitive; a song may also vary itself across loops by tracking a counter on the object), play(i,t,d,h).
- play is called once per sixteenth note, ahead of time. Schedule only at time t or later (t + k*d is fine). Never touch the AudioContext directly; use only h.synth, h.hit, h.chord, h.deal, h.intensity.
- h.chord([...]) once per chord change, with the chord as absolute MIDI notes in the 57 to 76 range: the game plays its pickup sounds on those notes.
- h.deal is true while a deal is on the board: add a recognisable extra layer (a bright arpeggio or counter-line) while it is true.
- h.intensity rises from 0 to 1 as the player's pipe gets longer: use it to open filters or add a part.
- Ranges: bass MIDI 28 to 48; melody and leads 52 to 79; never above 84. Per-voice volume: bass up to .12, leads up to .08, pads up to .04, drums: kick up to .5, others up to .15. Keep the mix balanced; the engine has a compressor but do not lean on it.
- Use the buses: 'dry' (bass, drums), 'pump' (pads: ducks under every kick, the sidechain pump), 'fx' (leads and arps that should echo).

## Test before you hand back
Render each song: `export PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers NODE_PATH=/home/claude/lb/node_modules; node /tmp/songs/render.js N 40` and also with `--deal`.
It must report errors: [], pageErrors: [], notes.bad: 0, notes.hi <= 84, and an rmsPer2s with no long silence. brightnessPer2s is a rough
treble measure: keep it near or below 0.05 (the example is about 0.02); higher means shrill. You cannot listen, so reason carefully about
the music itself: scale degrees, voice leading, rhythm, and how the loop sounds on its tenth repeat.

## Hand back
For each stage: the file path, title, key, bpm, meter, loop length, one line on its character and what h.deal and h.intensity do,
and the render stats line (errors, notes lo/hi, peakRaw, brightness max). Do not edit any other file.
