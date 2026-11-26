# Studio Controls & Navigation

- Move: click and drag an object directly on the camera-facing plane, or drag the red X, green Y or blue Z arrow for world-axis translation.
- Scale: drag coloured square handles to resize independently along the object's local X, Y and Z axes.
- Rotate: drag coloured rotation rings to rotate independently around X, Y or Z.
- Hold Control and drag with the left mouse button in the scene viewport to rotate the camera without moving or selecting objects.
- Select an object or group and press F to frame its bounds from an elevated three-quarter perspective (35 degrees above).
- Constant apparent gizmo sizing, drag threshold, one undo entry per completed transform and corrected movement under transformed parents.
- A direct patch for v0.0.19.9 includes the v0.0.20 textured asset importer and persistent asset library.

No new dependencies or project format changes. Tested with 202 passing CPU-side tests, including eight new viewport interaction tests. Eleven native tests skipped; Mac mouse, trackpad and visual feel still need hardware testing.
