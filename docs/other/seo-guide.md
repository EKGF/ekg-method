# SEO Guide for Content Authors

This guide explains how to optimize your content for search engines when writing documentation for the EKG/Method site.

## Page-Specific Meta Descriptions

Every page should have a unique, descriptive meta description. Add it in the frontmatter at the top of your Markdown file:

```yaml
---
description: "A clear, concise description of what this page covers (150-160 characters recommended)"
keywords:
  - keyword1
  - keyword2
  - keyword3
schema_type: "Article"  # or "WebPage", "HowTo", etc.
---
```

### Best Practices for Descriptions

- **Length**: Aim for 150-160 characters (Google typically shows up to 160)
- **Be specific**: Describe what the reader will learn, not generic marketing copy
- **Include keywords**: Naturally incorporate relevant search terms
- **Action-oriented**: Use active voice when possible
- **Unique**: Each page must have a different description

### Example

```yaml
---
description: "Learn how outcomes define the business value and success criteria for use cases in the EKG Method. Outcomes provide the 'why' behind every requirement."
keywords:
  - outcome
  - business outcome
  - use case outcome
  - EKG method
schema_type: "Article"
---
```

## Keywords

Add relevant keywords as a list in the frontmatter. These help search engines understand your content:

```yaml
keywords:
  - primary keyword
  - secondary keyword
  - related term
```

### Keyword Best Practices

- **3-5 keywords**: Don't overdo it
- **Relevant**: Only include terms actually discussed on the page
- **Natural**: Use terms your audience would search for
- **Specific**: Prefer specific terms over generic ones

## Schema.org Structured Data

The `schema_type` field determines the type of structured data (JSON-LD) added to the page:

- **`Article`**: For documentation pages, tutorials, guides
- **`WebPage`**: For general pages
- **`HowTo`**: For step-by-step instructions
- **`FAQPage`**: For FAQ pages

## Page Titles

Page titles are automatically generated from your H1 heading. Best practices:

- **Clear and descriptive**: The H1 should clearly state what the page is about
- **Include keywords**: Naturally incorporate important search terms
- **Unique**: Each page should have a distinct title
- **Concise**: Keep it under 60 characters when possible

## Content Optimization

### Headings Structure

Use proper heading hierarchy:

```markdown
# H1 - Page Title (only one per page)
## H2 - Main Sections
### H3 - Subsections
```

### Internal Linking

Link to related pages within the documentation:

```markdown
Learn more about [Use Cases](use-case.md) and [Outcomes](outcome.md).
```

### Images

- Use descriptive alt text for all images
- Include relevant keywords in filenames when appropriate
- Optimize image file sizes for faster loading

### Summary Sections

The `<!--summary-start-->` and `<!--summary-end-->` comments create summary sections that can be used for SEO. Make sure summaries are:

- Clear and concise
- Include key concepts
- Naturally incorporate keywords

## Social Media Optimization

Open Graph and Twitter Card tags are automatically generated from your page metadata. To customize:

### Custom Images

Add a custom image for social sharing:

```yaml
---
description: "..."
image: "/assets/images/custom-page-image.png"
---
```

### Custom Titles

The page title is used for social sharing. Make sure it's compelling and descriptive.

## Technical SEO

The following are handled automatically:

- ✅ Canonical URLs
- ✅ Sitemap generation
- ✅ Mobile-responsive design
- ✅ Fast page loading
- ✅ Structured data (JSON-LD)
- ✅ Open Graph tags
- ✅ Twitter Card tags
- ✅ robots.txt (located at `/docs/robots.txt` and copied to site root during build)

## Checklist for New Pages

When creating a new page, ensure you have:

- [ ] Unique meta description (150-160 chars)
- [ ] Relevant keywords (3-5 terms)
- [ ] Appropriate schema_type
- [ ] Clear, descriptive H1 title
- [ ] Proper heading hierarchy
- [ ] Internal links to related pages
- [ ] Alt text for images
- [ ] Summary section (if applicable)

## Examples

### Concept Page

```yaml
---
description: "Learn how [concept] works in the EKG Method. [Specific benefit or learning outcome]."
keywords:
  - concept-name
  - related-term
  - EKG method
schema_type: "Article"
---
# Concept Name
```

### Process Page

```yaml
---
description: "Step-by-step guide to [process name] in the EKG Method. Learn how to [specific action]."
keywords:
  - process-name
  - workflow
  - EKG method
schema_type: "HowTo"
---
# Process Name
```

## Questions?

If you have questions about SEO optimization, please refer to:
- [Google's SEO Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide)
- [Schema.org Documentation](https://schema.org/)

