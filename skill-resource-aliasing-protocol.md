# Skill: Resource Aliasing Protocol

## 🎯 Goal
Prevent "Future Self" amnesia and AI context-window confusion by mapping human-centric nicknames (aliases) to technical infrastructure in central governance logs.

## 🛠 Context
In complex multi-project ecosystems, infrastructure often acquires nicknames (e.g., "Fat AI", "Mission Control") or generic functional names (e.g., "Image Generator"). Standard documentation often only lists the service provider (e.g., "RunPod", "Cloudflare R2"), creating a searchability gap.

## 📋 The Protocol

### 1. Identify the Gap
When a user or AI agent asks "Where is X?" and the term "X" does not appear in the canonical `EXTERNAL_RESOURCES.md`, an alias gap exists.

### 2. Map the Relationship
Identify the relationship between the Nickname, the Tool, and the Project.
- **Nickname:** "Fat AI"
- **Tool:** `mission_control.py`
- **Project:** `3D Pose Factory`
- **Service:** RunPod / Cloudflare R2

### 3. Update the Registry
Add an `aliases:` array to the YAML registry and a bulleted list to the Markdown log.

```yaml
projects:
  3d-pose-factory:
    aliases: ["Image Generation", "Fat AI", "Mission Control"]
```

### 4. Search Verification
Verify that a global search for "Image Generation" now returns the specific project path and the `mission_control.py` script.

## ✅ Impact
- Eliminates "hunt and peck" time for returning developers.
- Enables autonomous agents to find specialized pipelines without human hand-holding.
- Maintains high-speed momentum during "Clean Slate" project launches.
