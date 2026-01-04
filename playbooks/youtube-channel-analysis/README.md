# YouTube Channel Analysis Playbook

> **Version:** 1.0.0  
> **Last Updated:** December 30, 2025  
> **Purpose:** Systematically analyze YouTube channels using data to understand content patterns and generate actionable insights

---

## What This Skill Does

Analyzes a YouTube channel's content strategy using metadata and transcripts (not videos) to:
- Identify successful content patterns
- Understand delivery style and structure
- Generate personalized content ideas based on proven patterns
- Extract reusable strategic insights

**Key Principle:** Data-driven analysis, not guessing.

---

## When to Use This Skill

**Use when:**
- ✅ Researching successful creators in your niche
- ✅ Planning content strategy for YouTube channel
- ✅ Understanding what content formats perform best
- ✅ Generating video ideas based on proven patterns
- ✅ Analyzing competitor strategies
- ✅ Learning from adjacent niches

**Don't use when:**
- ❌ You just want to watch videos casually
- ❌ You need real-time/live content analysis
- ❌ Video quality/production analysis is the goal (this focuses on content)
- ❌ You lack basic data about target channel (need public metadata)

---

## Prerequisites

Before starting this analysis, you need:

1. **Target channel identified** - YouTube channel URL
2. **Your context prepared:**
   - Your own channel URL (if applicable)
   - Your niche and content focus
   - Your goals (audience building, monetization, education, etc.)
   - What content has worked for you so far
3. **Tools available:**
   - `yt-dlp` for downloading metadata/subtitles
   - SQLite for data storage
   - Python environment
   - AI coding assistant (Claude, Cursor, etc.)

---

## The Analysis Process

### Phase 1: Data Collection

#### Step 1: Set Up Environment
```bash
# Create isolated environment
uv venv  # or python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install required tools
pip install yt-dlp sqlite3
```

#### Step 2: Download Channel Data

**Critical:** Download metadata and subtitles ONLY, not videos.

**Why:**
- Videos are huge (gigabytes), subtitles are tiny (kilobytes)
- Analysis only needs text content and metadata
- 100x faster than downloading videos
- More efficient use of bandwidth and storage

**Command:**
```bash
yt-dlp \
  --skip-download \
  --write-auto-sub \
  --write-info-json \
  --sub-format vtt \
  --output "%(uploader)s/%(title)s.%(ext)s" \
  [CHANNEL_URL]
```

**What you'll get:**
- Video titles
- Upload dates
- View counts
- Durations
- Descriptions
- Transcripts/subtitles (the actual spoken content)
- Thumbnail URLs
- Chapter markers (if available)

#### Step 3: Create SQLite Database

**Why SQLite:**
- Local, no server required
- Structured data with proper types
- Easy to query with SQL
- Professional data organization
- Handles relationships well

**Database Schema:**

```sql
-- Videos table: main metadata
CREATE TABLE videos (
    id TEXT PRIMARY KEY,
    title TEXT,
    uploader TEXT,
    upload_date DATE,
    duration INTEGER,
    view_count INTEGER,
    like_count INTEGER,
    description TEXT,
    thumbnail_url TEXT
);

-- Subtitle segments: transcribed content
CREATE TABLE subtitle_segments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id TEXT,
    start_time REAL,
    end_time REAL,
    text TEXT,
    FOREIGN KEY (video_id) REFERENCES videos(id)
);

-- Thumbnails: multiple sizes per video
CREATE TABLE thumbnails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id TEXT,
    url TEXT,
    width INTEGER,
    height INTEGER,
    FOREIGN KEY (video_id) REFERENCES videos(id)
);
```

**Task for AI:**
- "Parse the downloaded metadata files and create a SQLite database with this schema"
- "Load all subtitle files into the subtitle_segments table"

---

### Phase 2: Analysis Planning

#### Step 1: Provide Context to AI

**Template:**
```
I want to analyze [TARGET CHANNEL] to improve my own YouTube strategy.

My Context:
- My channel: [YOUR_CHANNEL_URL or "I'm starting from scratch"]
- My niche: [DESCRIPTION]
- My expertise: [WHAT YOU'RE GOOD AT]
- My goals: [AUDIENCE BUILDING / MONETIZATION / EDUCATION / etc.]
- Content that's worked for me: [EXAMPLES or "None yet"]
- Monetization plan: [COMMUNITY / COACHING / SPONSORSHIPS / etc.]

Target Channel Context:
- Channel: [TARGET_CHANNEL_NAME]
- Why analyzing them: [REASON - similar niche, adjacent niche, aspirational, etc.]
- Database path: [PATH_TO_SQLITE_DB]

Task: Create an analysis plan that will help me understand what works for this channel 
and generate actionable content ideas for MY specific situation.
```

**Why this matters:**
- AI can tailor recommendations to YOUR situation
- Not generic advice - personalized insights
- Combines AI's data processing with your domain knowledge

#### Step 2: Request Multi-Stage Analysis Plan

**For complex tasks, ALWAYS plan before executing.**

**Ask AI to create a 4-stage pipeline:**

1. **Descriptive Analytics** - What IS happening?
2. **Pattern Recognition** - What patterns exist?
3. **Strategic Synthesis** - WHY does it work?
4. **Personalized Recommendations** - How can YOU apply this?

**Review the plan, adjust if needed, then approve execution.**

---

### Phase 3: Descriptive Analytics (Stage 1)

**Goal:** Get high-level overview of the channel

**Analysis includes:**

#### Channel Overview
- Total video count
- Date range (first video to most recent)
- Upload frequency by period (daily/weekly/monthly)
- Average views per video
- Total views across channel

#### Growth Trajectory
- Videos per year
- Views per year
- Growth rate over time
- Peak activity periods
- Quiet periods

#### Content Volume Patterns
- Upload frequency changes
- Seasonality (if any)
- Content sprint patterns
- Consistency metrics

**SQL Query Examples:**
```sql
-- Basic stats
SELECT 
    COUNT(*) as total_videos,
    MIN(upload_date) as first_video,
    MAX(upload_date) as latest_video,
    AVG(view_count) as avg_views,
    SUM(view_count) as total_views
FROM videos;

-- Videos per year
SELECT 
    strftime('%Y', upload_date) as year,
    COUNT(*) as video_count,
    SUM(view_count) as total_views
FROM videos
GROUP BY year
ORDER BY year;

-- Peak upload months
SELECT 
    strftime('%Y-%m', upload_date) as month,
    COUNT(*) as uploads
FROM videos
GROUP BY month
ORDER BY uploads DESC
LIMIT 10;
```

**Output:** Markdown report with charts/tables showing channel overview.

---

### Phase 4: Pattern Recognition (Stage 2)

**Goal:** Identify what actually works

#### Analysis 1: Content Evolution

**Questions to answer:**
- How has the channel's focus changed over time?
- Which topic pivots occurred?
- Which pivots led to growth spurts?
- What were the breakthrough moments?

**Approach:**
- Group videos by time period
- Extract topics from titles/descriptions
- Correlate topic changes with view spikes
- Identify strategic pivots

**Example findings:**
```
2020: Initial experiments (low views)
2021: Focused on Tool X (audience building)
2022: Pivoted to Tool Y (explosion in views)
2023-2025: Broader niche focus (consistent performance)
```

#### Analysis 2: Duration vs Performance

**Questions:**
- Do longer or shorter videos perform better?
- Is there an optimal duration?
- Do outliers exist (very long videos with high views)?

**SQL Query:**
```sql
-- Performance by duration buckets
SELECT 
    CASE 
        WHEN duration < 300 THEN '0-5 min'
        WHEN duration < 900 THEN '5-15 min'
        WHEN duration < 1800 THEN '15-30 min'
        WHEN duration < 3600 THEN '30-60 min'
        ELSE '60+ min'
    END as duration_bucket,
    COUNT(*) as video_count,
    AVG(view_count) as avg_views,
    MAX(view_count) as max_views
FROM videos
GROUP BY duration_bucket;
```

**Look for:**
- Patterns that contradict conventional wisdom
- Example: "3-6 hour mega courses" might outperform short content
- Content format preferences of the audience

#### Analysis 3: Top Performers

**Identify top 10-20 videos by views:**

```sql
SELECT 
    title,
    view_count,
    duration,
    upload_date,
    description
FROM videos
ORDER BY view_count DESC
LIMIT 20;
```

**Then analyze for common patterns:**
- Title structure (question? tutorial? course?)
- Topics covered
- Duration patterns
- Keywords used
- Thumbnail patterns (if analyzing images)
- Upload timing

**Create a "Top Performer Pattern Template":**
```
Common patterns in top 20 videos:
- Titles: [PATTERN]
- Topics: [PATTERN]
- Format: [PATTERN]
- Length: [PATTERN]
- Keywords: [PATTERN]
```

#### Analysis 4: Bottom Performers

**Identify bottom 10-20 videos:**

```sql
SELECT 
    title,
    view_count,
    duration,
    upload_date
FROM videos
ORDER BY view_count ASC
LIMIT 20;
```

**Analyze what DOESN'T work:**
- Topics that didn't resonate
- Format experiments that failed
- Timing issues
- What to avoid

#### Analysis 5: Content Type Correlation

**Categorize videos by type:**
- Long-form courses
- Quick tutorials
- Tool reviews
- Opinion/commentary
- Live streams
- Shorts

**Measure performance by category:**
- Which types get most views?
- Which types get best engagement (likes/comments)?
- Which types have best view-to-subscriber conversion?

**Output:** Markdown report identifying clear patterns of what works and what doesn't.

---

### Phase 5: Strategic Synthesis (Stage 3)

**Goal:** Understand WHY patterns work

#### Combine Insights

Take patterns from Stage 2 and synthesize into strategic insights:

**Example synthesis:**
```
Pattern: Long-form comprehensive courses (3-6 hours) perform exceptionally well

Why this works:
- Audience values depth over quick tips
- Course format = high perceived value
- YouTube algorithm favors watch time
- Positions creator as authority
- Searchable for specific tools

Strategic implication:
- Invest time in comprehensive tutorials
- Don't compete on quick tips (saturated)
- Build "definitive guides" for tools in your niche
```

#### Identify Strategic Positioning

**Questions to answer:**
- How does this creator differentiate?
- What unique angle do they take?
- What audience need are they serving?
- How do they monetize?
- What's their core value proposition?

**Example:**
```
Nick Saraev's positioning:
- Focus: Business applications, not just technical details
- Angle: "Make money with automation" not just "learn automation"
- Audience: Entrepreneurs and freelancers, not developers
- Differentiation: Practical, monetization-focused tutorials
```

#### Extract Reusable Principles

**From patterns → principles:**

Example principles:
- "Mention monetization in first 30 seconds to hook audience"
- "Fewer, meatier chapters > many small segments"
- "Title format: [Tool] + [Transformation] performs best"
- "Upload consistently during growth phase, then quality > quantity"

**Output:** Strategic synthesis document with actionable principles.

---

### Phase 6: Personalized Recommendations (Stage 4)

**Goal:** Generate specific content ideas for YOUR channel

#### Content Idea Generation

**Input:**
- Top performer patterns (from Stage 2)
- Strategic principles (from Stage 3)
- Your context (provided in Phase 2)
- Your unique expertise

**Process:**
Ask AI to generate 20+ video ideas that:
1. Apply proven patterns from target channel
2. Adapt to YOUR niche and expertise
3. Fit YOUR goals (audience building, monetization, etc.)
4. Leverage YOUR unique advantages

**Output format for each idea:**
```markdown
### Video Idea #1: [TITLE]

**Format:** [Course / Tutorial / Review / etc.]
**Length:** [Estimated duration]
**Pattern applied:** [Which top performer pattern this uses]
**Why this will work:** [Strategic reasoning]
**Your unique angle:** [What makes this different/valuable from you]
**Monetization hook:** [How to present this]
**Prerequisites:** [What you need to create this]
```

**Example:**
```markdown
### Video Idea #1: Claude Code Complete Course - Zero to Advanced

**Format:** Long-form comprehensive course
**Length:** 3-5 hours
**Pattern applied:** Nick's "mega course" format (3-6 hours = high views)
**Why this will work:** 
- Tool is new and growing (like n8n was for Nick in 2022)
- No definitive course exists yet
- High search potential
- Builds authority
**Your unique angle:** 
- You have ML/econ background, can show research applications
- Can show practical business use cases
**Monetization hook:** 
"Learn to use Claude Code to automate your entire research workflow"
**Prerequisites:** 
- 20+ hours of examples to record
- Chapter structure planned
- Community to promote to
```

#### Prioritization

Rank ideas by:
1. **Effort required** (low/medium/high)
2. **Potential impact** (views/subscribers/revenue)
3. **Your readiness** (can you create this now?)
4. **Time sensitivity** (is the topic trending?)

**Create a content roadmap:**
```
Next 30 days:
- [Quick win ideas - low effort, good impact]

Next 90 days:
- [Medium effort ideas - building momentum]

Next 6 months:
- [High effort ideas - authority builders]
```

**Output:** Prioritized content roadmap with 20+ specific ideas.

---

### Phase 7: Deep Dive Analysis (Optional)

#### Transcript Analysis: Delivery Style

**Goal:** Understand HOW they deliver content, not just WHAT they cover

**Analysis areas:**

1. **Opening Hooks**
   - First 30 seconds of top videos
   - Common patterns in openings
   - How they capture attention

2. **Teaching Patterns**
   - How do they explain concepts?
   - Use of examples
   - Pacing and structure
   - Repetition patterns

3. **Transition Phrases**
   - How do they move between topics?
   - Signposting techniques
   - Energy management

4. **Closing Patterns**
   - How do they end videos?
   - Call-to-action patterns
   - What makes viewers want more?

**SQL Query for Opening Analysis:**
```sql
-- Get first subtitle segment of top 10 videos
SELECT 
    v.title,
    v.view_count,
    s.text as opening_text
FROM videos v
JOIN subtitle_segments s ON v.id = s.video_id
WHERE s.start_time < 30  -- First 30 seconds
ORDER BY v.view_count DESC
LIMIT 10;
```

**Analyze:**
- Common words/phrases
- Tonality (casual/formal/energetic)
- Promises made
- Hooks used

#### Course Structure Analysis

**For long-form content specifically:**

**Extract chapter structure:**
- YouTube metadata often includes chapters
- Or extract from video description
- Or identify from subtitle patterns

**Analyze chapter patterns:**
```sql
-- If chapters are in metadata
SELECT 
    video_id,
    chapter_title,
    chapter_duration,
    chapter_order
FROM chapters
WHERE video_id IN (
    SELECT id FROM videos 
    ORDER BY view_count DESC 
    LIMIT 10
);
```

**Questions:**
- How many chapters per course?
- Average chapter length?
- What makes chapters effective?
- How are chapters titled?

**Key findings to look for:**
- "Fewer, meatier chapters" vs "many small segments"
- Optimal chapter count (e.g., 8-12 chapters for 4-hour course)
- Chapter naming conventions
- How comprehensive vs modular

**Output:** Delivery style guide and course structure template.

---

## Outputs You Should Have

After completing this analysis, you should have:

### 1. Descriptive Analytics Report
- Channel overview stats
- Growth trajectory
- Upload patterns
- Saved as: `reports/01-descriptive-analytics.md`

### 2. Pattern Recognition Report
- Content evolution timeline
- Duration vs performance analysis
- Top performer patterns
- Bottom performer anti-patterns
- Content type correlations
- Saved as: `reports/02-pattern-recognition.md`

### 3. Strategic Synthesis Document
- Why patterns work
- Strategic positioning insights
- Reusable principles
- Saved as: `reports/03-strategic-synthesis.md`

### 4. Personalized Content Roadmap
- 20+ specific video ideas
- Prioritization matrix
- 30/90/180-day roadmap
- Saved as: `reports/04-content-roadmap.md`

### 5. (Optional) Delivery Style Guide
- Opening hooks analysis
- Teaching pattern insights
- Course structure template
- Saved as: `reports/05-delivery-style.md`

---

## Best Practices

### 1. Download Metadata, Not Videos
**Always:** Use `--skip-download` with `yt-dlp`  
**Why:** 100x faster, saves bandwidth, subtitles contain all the text

### 2. Use SQLite for Organization
**Always:** Structure data in database, not flat files  
**Why:** Makes querying easy, professional organization, handles relationships

### 3. Plan Before Executing (Complex Tasks)
**Always:** For multi-step analysis, ask AI to create plan first  
**Why:** Ensures structured approach, you can review/adjust, saves time

### 4. Provide Your Context
**Always:** Tell AI about your niche, goals, expertise  
**Why:** Enables personalized recommendations, not generic advice

### 5. Use Voice Commands (Optional)
**Consider:** Speech-to-text for faster prompting  
**Tools:** Super Whisper, Whisper Flow  
**Why:** Speaking is faster than typing for complex prompts

### 6. Embed Your Domain Knowledge
**Always:** Share what you already know about the channel/niche  
**Why:** Combines AI's data processing with your human insight = better results

### 7. Think Like a Researcher
**Process:** Describe → Pattern → Synthesize → Recommend  
**Why:** Systematic approach catches insights random analysis misses

### 8. Create Reusable Assets
**Goal:** Package this analysis into reusable process  
**Why:** Run on multiple channels, build competitive intelligence library

---

## Common Pitfalls to Avoid

### ❌ Downloading Full Videos
**Problem:** Wastes time and bandwidth  
**Solution:** Use `--skip-download` flag, get subtitles only

### ❌ Skipping the Planning Step
**Problem:** AI jumps straight to execution, results are scattered  
**Solution:** For complex tasks, always request plan first

### ❌ Generic Analysis (No Context)
**Problem:** AI gives generic insights that don't apply to you  
**Solution:** Provide YOUR context upfront (niche, goals, expertise)

### ❌ Only Analyzing One Channel
**Problem:** Can't separate universal patterns from channel-specific quirks  
**Solution:** Analyze 2-3 channels in niche for comparison

### ❌ Analysis Paralysis
**Problem:** Spend weeks analyzing, never create content  
**Solution:** Set time limit (e.g., 4 hours), then move to creation

### ❌ Ignoring Bottom Performers
**Problem:** Only look at what works, miss what to avoid  
**Solution:** Analyze failures too - knowing what doesn't work is valuable

### ❌ Not Adapting to Your Strengths
**Problem:** Copy what works for them, even if it doesn't fit you  
**Solution:** Use patterns as inspiration, adapt to YOUR unique advantages

---

## Success Metrics

**After completing this analysis, you should be able to answer:**

- [ ] What content formats perform best for this channel?
- [ ] What topics/angles get the most traction?
- [ ] How has their strategy evolved over time?
- [ ] What are their breakthrough moments?
- [ ] What delivery style patterns do they use?
- [ ] What should I avoid (based on their failures)?
- [ ] How can I adapt their patterns to MY niche?
- [ ] What 5 videos should I create in the next 90 days?

**Validation questions:**
- Can you explain WHY certain patterns work (not just that they work)?
- Do your recommendations fit YOUR specific context?
- Could you repeat this analysis on a different channel?
- Are your insights actionable (not just interesting)?

---

## Tool-Specific Adaptations

This playbook is tool-agnostic. Refer to tool-specific adapters for:
- **Cursor:** See `cursor-rules/youtube-channel-analysis/`
- **Claude Code:** See `claude-skills/youtube-channel-analysis/`
- **Other tools:** Adapt the instructions as needed

---

## Version History

**1.0.0** (December 30, 2025)
- Initial playbook created
- Based on Aniket Panjwani's Nick Saraev analysis methodology
- 4-stage analysis pipeline defined
- Includes optional deep-dive analysis
- Best practices and pitfalls documented

---

## Related Skills

- `content-analysis` - General content analysis patterns
- `data-collection` - Data scraping and organization
- `report-generation` - Formatting analysis outputs

---

## References

- **Source methodology:** "I Reverse Engineered Nick Saraev's YouTube Channel With Claude Code" by Aniket Panjwani (Dec 2025)
- **yt-dlp documentation:** https://github.com/yt-dlp/yt-dlp
- **SQLite documentation:** https://www.sqlite.org/docs.html

---

*This is a living document. Update as you learn better patterns.*

