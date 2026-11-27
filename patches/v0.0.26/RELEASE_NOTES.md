# Architect & Spatial Planning

- Detailed procedural exteriors for houses, shops and apartments: pitched roofs, triangular gables, framed glazing, doors, entry steps, gutters, awnings and parapets.
- New neighbourhood operation lays out two to six houses along a road with doors facing the street, footpaths and kerbs.
- Ground snapping and sampled foundation checks, water and terrain limits, conservative transformed bounds and road/footpath clearance. Trees retry valid candidate positions rather than scattering through buildings.
- Imported assets retain their native proportions by default and use actual mesh extents for ground placement.
- AI plans are preflighted on a detached scene. An invalid plan gets one corrective AI request; invalid corrected plans are rejected. Revalidation before a single undoable edit.
- 13 targeted automated tests passed; six-house fixture produces 263 new entities. Patch hashes and the v0.0.25 base inventory fingerprint verified. Full engine installation and live Ollama/macOS rendering not tested in this environment.
- Existing 40-action and 500-entity budgets retained. No new model download; Qwen 2.5 3B remains the default. Exterior shells are solid, with decorative doors/windows, not enterable interiors. Placement bounds and terrain samples are conservative approximations. Requires v0.0.25.
