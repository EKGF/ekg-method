# SEO Improvement Plan for method.ekgf.org

## Current Situation Analysis

Based on Google Search Console data (16 months):

- **7 total queries** with impressions
- **0 clicks** on almost all pages
- **Very low impressions** (17 max for one page)
- Pages are indexed but not ranking well

## Root Causes

1. **Poor title optimization** - Titles like "A: Interoperability" aren't search-friendly
2. **Missing freshness signals** - No `date_published` fields
3. **Weak internal linking** - Limited "related content" sections
4. **Low click-through potential** - Descriptions may not be compelling enough
5. **Niche/technical content** - May not match broader search intent
6. **Limited backlinks** - External sites likely not linking to content

## Action Plan

### 1. Fix Page Titles (HIGH PRIORITY)

**Problem**: Titles like "A: Interoperability" don't help SEO
**Solution**: Use `title:` in front-matter to override H1 for search

**Examples to fix**:

- `objective/interoperability.md`: "A: Interoperability" → "Enterprise Interoperability with Knowledge Graphs"
- Other objective pages with "A:", "B:", etc. prefixes

### 2. Add Date Published Fields (HIGH PRIORITY)

**Why**: Google uses freshness as a ranking signal
**Action**: Add `date_published` to all key pages

```yaml
date_published: "2022-06-23"  # Use actual publication date
```

### 3. Improve Descriptions (MEDIUM PRIORITY)

**Current**: "Enable interoperability across the enterprise..."
**Better**: "Learn how to achieve enterprise-wide interoperability using the Use Case Tree Method. Practical guide to semantic standards and data integration."

**Guidelines**:

- Start with action words: "Learn", "Discover", "Get started"
- Include specific benefits
- Keep 150-160 characters
- Make it compelling to click

### 4. Add Related Content Sections (HIGH PRIORITY)

**Current**: Some pages have "Relationship to Other Concepts" (good!)
**Action**: Add to ALL concept and objective pages

**Template**:

```markdown
## Related Content

- **[Related Concept](link.md)** - Brief why it's related
- **[Related Objective](link.md)** - Brief why it's related
- **[Related Process Step](link.md)** - Brief why it's related
```

### 5. Optimize for Search Intent (MEDIUM PRIORITY)

**Problem**: Content may be too technical/niche
**Solution**: 

- Add "What is..." sections for key concepts
- Include "How to..." sections for processes
- Add "Why..." sections explaining benefits

### 6. Internal Linking Strategy (HIGH PRIORITY)

**Current**: Some internal links exist but not systematic
**Action**: 

- Add 3-5 internal links per page
- Link from high-traffic pages to important content
- Use descriptive anchor text (not "click here")

### 7. Content Freshness (MEDIUM PRIORITY)

**Action**: 

- Add `date_modified` when content is updated
- Consider a "Last updated" indicator
- Regular content updates signal freshness

### 8. Backlink Strategy (LONG TERM)

**Actions**:

- Link from main EKGF site (ekgf.org)
- Link from related sites (principles.ekgf.org, maturity.ekgf.org)
- Share on LinkedIn/Twitter with links
- Submit to relevant directories
- Guest posts on related blogs

### 9. Keyword Optimization (MEDIUM PRIORITY)

**Research needed**: What do people actually search for?
**Potential keywords**:

- "enterprise knowledge graph method"
- "knowledge graph methodology"
- "EKG implementation guide"
- "use case tree method"
- "semantic data modeling"

**Action**: Ensure these appear naturally in content

### 10. Technical Improvements (LOW PRIORITY - Already Good)

✅ Sitemap exists
✅ robots.txt configured
✅ Canonical URLs
✅ Structured data (JSON-LD)
✅ Mobile responsive
✅ Fast loading

## Implementation Priority

1. **Week 1**: Fix titles, add date_published to top 10 pages
2. **Week 2**: Add related content sections to all concept/objective pages
3. **Week 3**: Improve descriptions for top 20 pages
4. **Week 4**: Enhance internal linking throughout site
5. **Ongoing**: Backlink building, content updates

## Metrics to Track

- Impressions (target: 10x increase in 3 months)
- Clicks (target: 5% CTR)
- Average position (target: top 20 for key terms)
- Pages indexed (should stay at current level)
- Backlinks (target: 10+ quality links)

## Quick Wins

1. Fix "A:", "B:" titles → Immediate improvement
2. Add date_published → Freshness signal
3. Add related content sections → Better internal linking
4. Improve homepage description → Better first impression

## Completed Actions

✅ Created SEO improvement plan document
✅ Fixed ALL 13 objective page titles (removed "A:", "B:", "C:" prefixes)
✅ Added date_published to all objective pages
✅ Improved homepage description to be more action-oriented
✅ Added date_published to `vocab/ekg.md`
✅ Added related content sections to interoperability, composable-business, and ekg pages

## Easy Wins Completed ✅

1. ✅ **Fixed all objective page titles** - All 13 pages now have search-friendly titles
2. ✅ **Improved homepage description** - More action-oriented and keyword-rich
3. ✅ **Added date_published** - Added to all objective pages and key vocab pages

## Next Easy Wins (Do These Next)

1. **Add date_published to concept pages** (5 min)
   - `concept/use-case.md`
   - `concept/use-case-tree.md`
   - `concept/ontology.md`
   - `concept/data-product.md`
   - `concept/persona.md`
   - `concept/story.md`
   - `concept/outcome.md`
   - `concept/workflow.md`

2. **Add related content sections** (15 min)
   - Add to remaining objective pages (10 pages)
   - Add to concept pages that don't have them

3. **Improve descriptions** (10 min)
   - Make them start with "Learn" or "Discover"
   - Ensure 150-160 characters
   - Make them more compelling

