# Cursor Rule: YouTube Channel Analysis

> **Adapter for:** `playbooks/youtube-channel-analysis/`  
> **Version:** 1.0.0  
> **Tool:** Cursor IDE

---

## Quick Reference

When analyzing YouTube channels in Cursor, follow the canonical playbook:

**Playbook location:** `/Users/eriksjaastad/projects/agent-skills-library/playbooks/youtube-channel-analysis/README.md`

---

## How to Use This Skill in Cursor

### Step 1: User Provides Context

User will provide:
- Target YouTube channel URL
- Their own channel/niche context
- Their goals (audience building, monetization, etc.)
- Database path (if data already collected)

### Step 2: Check Current Phase

**If data NOT collected yet:**
1. Guide user through `yt-dlp` setup
2. Help create SQLite database schema
3. Parse downloaded metadata into database
4. Verify data loaded correctly

**If data already collected:**
1. Verify database exists and is accessible
2. Check data quality (sample queries)
3. Proceed to analysis

### Step 3: Create Analysis Plan

**Always create a plan first for complex analysis:**

```markdown
# YouTube Analysis Plan for [CHANNEL]

## Phase 1: Descriptive Analytics
- [ ] Channel overview stats
- [ ] Growth trajectory
- [ ] Upload patterns
- [ ] Output: reports/01-descriptive-analytics.md

## Phase 2: Pattern Recognition
- [ ] Content evolution
- [ ] Duration vs performance
- [ ] Top/bottom performers
- [ ] Content type correlation
- [ ] Output: reports/02-pattern-recognition.md

## Phase 3: Strategic Synthesis
- [ ] Why patterns work
- [ ] Strategic positioning
- [ ] Reusable principles
- [ ] Output: reports/03-strategic-synthesis.md

## Phase 4: Personalized Recommendations
- [ ] 20+ video ideas
- [ ] Prioritization matrix
- [ ] 30/90/180-day roadmap
- [ ] Output: reports/04-content-roadmap.md

## Phase 5: (Optional) Deep Dive
- [ ] Delivery style analysis
- [ ] Course structure patterns
- [ ] Output: reports/05-delivery-style.md

**Estimated time:** 2-3 hours
```

**Present plan to user, get approval before proceeding.**

### Step 4: Execute Analysis Phases

Follow the playbook's 4-stage pipeline:

**Stage 1: Descriptive Analytics**
- Run SQL queries for channel overview
- Calculate growth metrics
- Create markdown report with findings
- Save to `reports/01-descriptive-analytics.md`

**Stage 2: Pattern Recognition**
- Analyze content evolution timeline
- Duration vs performance analysis
- Top 20 and bottom 20 performers
- Extract patterns into report
- Save to `reports/02-pattern-recognition.md`

**Stage 3: Strategic Synthesis**
- Synthesize WHY patterns work
- Identify strategic positioning
- Extract reusable principles
- Save to `reports/03-strategic-synthesis.md`

**Stage 4: Personalized Recommendations**
- Generate 20+ specific video ideas
- Apply patterns to user's context
- Prioritize by effort/impact
- Create content roadmap
- Save to `reports/04-content-roadmap.md`

### Step 5: Optional Deep Dive

If user requests delivery style analysis:
- Analyze opening hooks from top videos
- Extract teaching patterns
- Study course structure (if applicable)
- Create style guide
- Save to `reports/05-delivery-style.md`

---

## Cursor-Specific Considerations

### Working with SQLite in Cursor

```python
# Use Python to query database
import sqlite3

conn = sqlite3.connect('youtube_data.db')
cursor = conn.cursor()

# Example query
cursor.execute("""
    SELECT title, view_count 
    FROM videos 
    ORDER BY view_count DESC 
    LIMIT 20
""")

results = cursor.fetchall()
```

### Creating Reports

**Format:** Markdown with tables and charts

```markdown
# Descriptive Analytics: [Channel Name]

## Overview
- **Total videos:** 252
- **Date range:** 2020-01-15 to 2025-12-01
- **Total views:** 12.5M
- **Average views:** 49,603

## Growth by Year

| Year | Videos | Total Views | Avg Views |
|------|--------|-------------|-----------|
| 2020 | 12     | 45K         | 3,750     |
| 2021 | 48     | 1.2M        | 25,000    |
| 2022 | 96     | 6.8M        | 70,833    |
| 2023 | 64     | 3.2M        | 50,000    |
| 2024 | 32     | 1.3M        | 40,625    |

## Key Findings
- Peak activity: 2022 (96 videos)
- Peak performance: 2022 (highest avg views)
- Current state: Quality over quantity (fewer videos, consistent performance)
```

### Progress Updates

After each phase, show user:
- Summary of findings
- Path to saved report
- Ask if they want to proceed to next phase or deep-dive on something

**Example:**
```
✅ Phase 1 Complete: Descriptive Analytics

Key findings:
- 252 videos analyzed
- Peak upload period: April 2022
- Growth trajectory: Early experimentation → Focus on Tool X → Pivot to Tool Y → Diversification

📄 Report saved: reports/01-descriptive-analytics.md

Next: Phase 2 (Pattern Recognition) - analyze what content performs best?
Or would you like to explore any Phase 1 findings deeper first?
```

---

## Output Format

### File Structure

```
analyze-youtube-videos/
├── youtube_data.db          ← SQLite database
├── reports/
│   ├── 01-descriptive-analytics.md
│   ├── 02-pattern-recognition.md
│   ├── 03-strategic-synthesis.md
│   ├── 04-content-roadmap.md
│   └── 05-delivery-style.md (optional)
└── data/
    └── [raw downloaded files from yt-dlp]
```

### Report Template

Each report should have:

```markdown
# [Phase Name]: [Channel Name]

**Date:** [Today's date]
**Analyzed by:** [User name] with AI assistance
**Channel:** [Channel URL]
**Videos analyzed:** [Count]

---

## Summary

[2-3 sentence summary of key findings]

---

## Detailed Findings

[Phase-specific content]

---

## Key Takeaways

- [Takeaway 1]
- [Takeaway 2]
- [Takeaway 3]

---

## Recommendations

[If applicable]

---

*Generated using agent-skills-library/playbooks/youtube-channel-analysis v1.0.0*
```

---

## Best Practices for Cursor

1. **Show SQL queries before running them**
   - Let user verify query logic
   - Explain what you're looking for

2. **Create reports incrementally**
   - Don't generate all reports at once
   - Let user review each phase before proceeding

3. **Use code blocks for reproducibility**
   - User should be able to re-run queries
   - Document all analysis code

4. **Visualize when helpful**
   - Tables for comparisons
   - Text-based charts for trends
   - Keep it markdown-friendly

5. **Save work frequently**
   - Each phase = separate file
   - User can reference later
   - Builds a knowledge base

---

## Common User Requests

### "Analyze this channel"
→ Start with context gathering (Phase 2, Step 1 of playbook)

### "I already have the database"
→ Skip to analysis planning (Phase 2, Step 2)

### "Just give me video ideas"
→ Explain that recommendations work best with full analysis, but offer to do Phase 4 only if they insist

### "Why does this work?"
→ This is Phase 3 (Strategic Synthesis) - make sure Phase 2 is done first

### "How do they structure their videos?"
→ This is Phase 5 (Deep Dive) - optional transcript analysis

---

## Cursor Tool Usage

When working in Cursor:

- ✅ Use terminal commands for `yt-dlp`
- ✅ Write Python scripts for data processing
- ✅ Create markdown reports as separate files
- ✅ Use file operations to save/read reports
- ✅ Show progress after each phase

- ❌ Don't try to download videos (just metadata/subtitles)
- ❌ Don't skip the planning step
- ❌ Don't generate all reports in one go (do incrementally)
- ❌ Don't forget to save user's context for personalization

---

## Example Cursor Workflow

```
User: "I want to analyze Ali Abdaal's channel for my productivity content"

AI: "Great! Let me gather some context to personalize the analysis.

Context questions:
1. Your channel: Do you have an existing channel, or starting fresh?
2. Your niche: What specific angle on productivity? (work, study, life, business?)
3. Your expertise: What's your background/unique angle?
4. Your goals: Audience building, monetization, or both?
5. Data: Have you already downloaded Ali's channel data, or should I help with that?

This context will help me generate recommendations tailored to YOU, not generic advice."

User: [Provides context]

AI: "Perfect. Here's the analysis plan:
[Shows 4-phase plan]

Estimated time: 2-3 hours

Should I proceed? Or would you like to adjust the plan?"

User: "Looks good, let's do it"

AI: [Executes Phase 1]
"✅ Phase 1 complete. Key finding: Ali uploads 2-3x per week consistently..."
[Shows summary, saves report]
"Ready for Phase 2?"

[Continue through phases...]
```

---

## Version History

**1.0.0** (December 30, 2025)
- Initial Cursor adapter created
- Maps to playbook v1.0.0
- Includes Cursor-specific file operations and workflow

---

## Related

- **Canonical Playbook:** `/agent-skills-library/playbooks/youtube-channel-analysis/README.md`
- **Claude Adapter:** `/agent-skills-library/claude-skills/youtube-channel-analysis/SKILL.md`

---

*Part of agent-skills-library - see README for versioning and testing guidelines*
