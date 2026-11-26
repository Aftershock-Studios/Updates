# Human Generation I

- New seeded adult character generator for the player and NPCs, with varied height, build, face shapes, hairstyles, skin tones, iris colours and clothing.
- Sculpted procedural facial geometry with integrated nose, cheekbones, eye sockets and chin; separately modelled eyes, brows, lips and ears.
- Individual fingers, improved limb transitions, garment surface detail, eye blinking and wind-driven hair tufts.
- Three geometry LODs for crowds, with preset-based distance thresholds and a Detailed humans graphics toggle.
- Scene > Human Generator: randomise, set a seed or reset the player's appearance; the seed is saved with the scene and exported games.
- Existing character movement, animations, physics capsules, NPC interactions and swimming retained. Legacy weighted skinning remains available with Detailed humans disabled.

Compatibility: requires v0.0.22. This is an original procedural anatomical renderer, not a scanned human or a seamless skeletal mesh. 217 CPU-side tests passed; 11 native tests skipped. All 11 shader programs compiled and linked. Native macOS rendering, appearance and FPS still require hardware testing.
