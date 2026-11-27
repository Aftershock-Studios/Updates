# AI World Builder

- New AI Chat toolbar panel with a local Ollama connection, defaulting to qwen2.5:3b. Choose another installed local model using Change model.
- Describe a world in natural language. The AI receives a limited scene and asset summary, then proposes structured construction actions.
- Create building shells, roads on flat terrain, boxes and props, trees and forests, terrain when none exists, player spawn when absent, weather and population settings. Place models already saved in the project library.
- Review the proposed actions and click Apply plan; the whole batch is undoable. No arbitrary code execution, deletion, or replacement of existing terrain. Reject stale or invalid plans and enforce 40-action / 500-new-entity limits.
- Background local inference keeps Studio responsive. Discard ignores the pending response; chat history is session-only.
- Install Ollama separately and run `ollama pull qwen2.5:3b`. The model is not bundled and no paid API key is needed.
- 11 targeted tests passed, including mocked Ollama requests, transactional edits, undo/redo and UI rendering. Full native macOS and live model inference remain untested. Requires v0.0.24.
