# Skill: Social Dispatcher Logic (Multi-Platform Distillation)

## 🎯 Goal
Efficiently cross-post high-authority niche content across multiple social platforms (Pinterest, Instagram, Twitter/X, TikTok) by "distilling" a single Markdown source into platform-specific formats.

## 🛠 Context
Manually writing unique posts for every platform is a scalability bottleneck. The "Social Dispatcher" pattern treats the Recipe Markdown as the "Source of Truth" and uses AI reasoning to adapt it for different "Vibe" requirements.

## 📋 The Distillation Protocol

### 1. The Source (Markdown)
Input is the canonical `slug-of-recipe.md` containing the schema (Ingredients, Instructions, Why Muffin Pans?).

### 2. Platform Distillation Rules
- **Pinterest (Visual Authority):**
    - **Format:** Vertical 2:3 Image.
    - **Logic:** Overlay Title + 1 Key Ingredient.
    - **Description:** SEO-heavy, focusing on "Easy Meal Prep" and "Muffin Tin."
- **Instagram (Aesthetic Vibe):**
    - **Format:** Square/Portrait image.
    - **Logic:** 1-sentence punchy hook + Emoji-heavy ingredient list.
    - **Hashtags:** Focused on #MuffinTinMeals #MealPrep #CleanKitchen.
- **Twitter/X (Utility Hook):**
    - **Format:** Text + Image.
    - **Logic:** "Stop cooking large batches. The Muffin Tin is the Docker for your food. Here's how to build [Recipe Name]."
- **TikTok/YouTube Shorts (Process Flow):**
    - **Format:** 9:16 Video Script.
    - **Logic:** Frame-by-frame "Build" sequence (Empty -> Base -> Fill -> Done).

### 3. Execution (The Dispatcher)
The AI agent reads the Markdown and outputs a JSON object containing all platform variants in one pass.

```json
{
  "pinterest": { "text": "...", "overlay": "..." },
  "instagram": { "caption": "..." },
  "video_script": [ "Frame 1: ...", "Frame 2: ..." ]
}
```

## ✅ Impact
- $0 cost platform distribution.
- High-volume social presence with near-zero manual overhead.
- Maintains a consistent brand voice while respecting platform-specific cultures.

## Related Documentation

- [Cost Management](Documents/reference/MODEL_COST_COMPARISON.md) - cost management
- [AI Team Orchestration](patterns/ai-team-orchestration.md) - orchestration
- [Safety Systems](patterns/safety-systems.md) - security
- [analyze-youtube-videos/README](../ai-model-scratch-build/README.md) - YouTube Analyzer
