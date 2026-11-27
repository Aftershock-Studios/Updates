# World Materials & Meshes

- New World Library with 1,024 deterministic original procedural PBR materials: 64 families, 16 independently seeded variations per family.
- 4,096 colour, OpenGL normal, roughness and height maps at 1K in the complete collection. Generate selected materials locally at 512, 1024 or 2048 pixels, no download required.
- 128 dimensioned textured GLB props: 16 groups with eight variations, including rocks, concrete barriers, kerbs, bollards, pots, timber, logs and drainage grates.
- Search, save, preview generated colour maps, apply to existing world slots, and generate meshes into the persistent Project Asset Library with existing collision modes.
- Optional checksummed 128-material ZIP pack import, preserving existing generated assets.
- CC0 original procedural content, not photographic scans. Use Marketplace for scanned materials.
- The active world renderer still uses shared 1K material slots; applying a material changes all objects using that slot after restart. 2K and height maps are authoring data; no new displacement shader.
- Requires v0.0.23. Ten targeted tests passed, all 128 mesh geometries validated and the complete 1K texture collection compiled. Native macOS performance and UI are not yet tested.
