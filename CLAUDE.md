# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HI Spatial is a **Jekyll-based static blog** focused on Geospatial and WebGIS tutorials in Indonesian (Bahasa Indonesia). It combines traditional static site generation with AI-powered content automation using Groq.

## Development Commands

```bash
# Install dependencies (Ruby/Bundler)
bundle install

# Development server (localhost:4000)
bundle exec jekyll serve

# Production build
bundle exec jekyll build

# Python script: Generate blog post manually
python scripts/generate_post.py
```

**Note**: After modifying `_config.yml`, restart the Jekyll server as it's not auto-reloaded.

## Architecture

### Content Management

**Blog Posts**: Located in `_posts/` with naming convention `YYYY-MM-DD-title.md`. All posts use YAML frontmatter:

```yaml
---
layout: post
title: "Article Title"
date: YYYY-MM-DD HH:MM:SS +0700
categories: [Category1, Category2]
tags: [keyword1, keyword2]
author: HI Spatial
---
```

**Important**: Dates should use WIB timezone (UTC+7) which is `+0700` in the frontmatter.

### AI Content Generation System

The blog includes an automated content generation system:

- **`scripts/generate_post.py`**: Python script that generates blog posts using Groq AI
  - Requires `GROQ_API_KEY` environment variable
  - Reads from `scripts/topics.json` for available topics
  - Moves used topics to `used_topics` array to prevent duplicates
  - Generates posts with WIB timestamps
  - Outputs post URL for deployment

- **`scripts/topics.json`**: Topic database with structure:
  ```json
  {
    "topics": [
      {"title": "...", "category": "...", "keywords": ["...", "..."]}
    ],
    "used_topics": [...]
  }
  ```

### CI/CD Pipelines

**`.github/workflows/jekyll.yml`**: Deploys site to GitHub Pages
- Triggered on push to master, workflow completion, or manually
- Builds with `JEKYLL_ENV=production`
- Uploads artifact and deploys to GitHub Pages

**`.github/workflows/auto-post.yml`**: Automated content generation
- Scheduled: 3x daily at 07:30, 12:30, 20:00 WIB
- Generates posts using Python script
- Auto-commits with `🤖 Auto-generated blog post` message
- Sends Discord notifications via `DISCORD_WEBHOOK_URL`
- Triggers Jekyll deploy automatically

### Site Configuration

**`_config.yml`** key settings:
- `permalink: /:categories/:title/` - URL structure
- `paginate: 6` - Posts per page
- `future: true` - Allows future-dated posts
- `locale: id_ID` - Indonesian locale for SEO
- Plugins: `jekyll-feed`, `jekyll-paginate`, `jekyll-seo-tag`, `jekyll-sitemap`

### Theming and Styling

- Black & white minimal design
- Fonts: Inter (headings), Merriweather (body), JetBrains Mono (code)
- Custom CSS in `assets/css/`
- Client-side search functionality in `assets/js/`

## Important Notes

- **Language**: All blog content is in Bahasa Indonesia
- **Author**: Default author is "HI Spatial" (configurable per post)
- **Timezone**: WIB (UTC+7) - consistent throughout the blog
- **No JavaScript package manager**: Pure Ruby/Jekyll stack (no package.json)
- **No formal tests**: Manual testing via `bundle exec jekyll serve`
- **AI-generated posts**: Tagged with "AI" and "Auto-Generated" tags, authored by "Kodibot"

## Adding New Content

When writing new blog posts:
1. Create file in `_posts/` as `YYYY-MM-DD-title.md`
2. Use WIB time for date: `YYYY-MM-DD HH:MM:SS +0700`
3. Start content with `##` (h2), not `#` (h1)
4. Include relevant categories and tags
5. Author defaults to "HI Spatial" unless specified otherwise
