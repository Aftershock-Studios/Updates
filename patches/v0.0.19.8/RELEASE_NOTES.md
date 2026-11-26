# Real World Renderer I

- Three distance-based instanced grass meshes with deterministic density thinning and expanded quality-dependent ranges.
- Near broadleaf and pine leaf geometry, branched trunks, mid-detail clusters and inexpensive far crowns.
- Dual-scale ground material sampling to reduce repeats, distance-faded normal map sampling, and more natural material tint.
- Wind-dependent ocean shading, more varied shoreline foam and shallow-water caustic-style lighting.
- Depth-aware, world-position-based rain at three distances; multiscale puddle masks and retained wetness, ripples and drying.
- Opt-in Poly Haven CC0 scanned PBR material importer in Graphics. It checks the optional GitHub library first, then the provider directly, verifies checksums and preserves existing project overrides.
- Existing terrain LOD, swimming and buoyancy retained.

Requires v0.0.19.7. No additional dependencies. Built-in geometry and textures remain procedural; actual scanned materials are separate optional downloads, not included in this patch. The separate material archive build has not completed successfully yet. Native macOS GPU appearance and performance require hardware testing.