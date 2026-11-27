# AI Architect Pro

- Fixes Player Spawn being incorrectly treated as a solid construction obstacle. Existing spawns are retained if safe, otherwise relocated to supported clear ground and reported in the preview.
- Bounded local placement recovery tries the requested site first, then nearby alternative sites for spatial conflicts, preserving dimensions and orientation. Explicit coordinates disable translation. Unsupported and invalid actions are skipped with explanations; valid actions remain reviewable.
- New deterministic blueprints work without Ollama: /blueprint neighbourhood, district, house, park, parking, plaza. Recognised requests can fall back to a labelled blueprint if local AI fails or returns no valid plan.
- Richer scene context with free-site samples, existing spawn and occupied bounds; rewritten architect instructions and examples. Up to 48 actions and 1,800 new entities per plan.
- Buildings have actual entry openings, independent walls, window sections, porch trim and interior partitions on qualifying houses. Mixed-use districts, front paths, parks, plazas and marked parking areas.
- Progress reports, stale scene protection, review before Apply and one undo transaction. Model preference persists; optional Qwen3 4B Instruct model, installed separately via Ollama. Existing Qwen2.5 3B remains usable.
- 24 targeted tests passed, including roads crossing the default spawn, partial recovery, six-house blueprint (527 new entities), model persistence and editor UI rendering. Patch hashes and base inventory fingerprint verified. Full native macOS installation, live model inference and rendering not tested here.
- Procedural geometry, not photorealistic scanned buildings. Upper floors lack stairs; road junctions and parking access are not automatically integrated into traffic routing. No artificial download padding. Requires v0.0.26.
