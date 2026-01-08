# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview
AstroPaper is a minimal, responsive, and SEO-friendly Astro blog theme. Built with Astro 5.10.0, TypeScript, and TailwindCSS v4.

## Essential Commands

### Development
```bash
pnpm run dev          # Start dev server at localhost:4321
pnpm run build        # Build for production (includes TypeScript check)
pnpm run preview      # Preview production build
```

### Code Quality
```bash
pnpm run format       # Format code with Prettier
pnpm run format:check # Check code formatting
pnpm run lint         # Lint with ESLint
```

### Type Generation
```bash
pnpm run sync         # Generate TypeScript types for Astro modules
```

## Architecture Overview

### Content System
- Blog posts stored as Markdown files in `src/data/blog/`
- Content schema defined in `src/content.config.ts` with Zod validation
- Frontmatter fields: title, pubDate, modDate, author, slug, featured, draft, tags, ogImage, description, canonicalURL, readingTime

### Routing Structure
- `/` - Homepage with featured and recent posts
- `/about/` - About page
- `/posts/` - All blog posts with pagination
- `/posts/[slug]/` - Individual blog post
- `/tags/` - All tags page
- `/tags/[tag]/` - Posts filtered by tag
- `/search/` - Search page powered by Pagefind
- `/og-image/[slug].png` - Dynamic OG images

### Component Architecture
- Layouts: `BaseLayout.astro` (root), `MainLayout.astro` (with Breadcrumb), `PostLayout.astro` (blog posts)
- Key components: `Header.astro`, `Footer.astro`, `Card.tsx` (React), `Breadcrumbs.astro`
- Utilities in `src/utils/`: `datetime.ts`, `getSortedPosts.ts`, `generateOgImages.tsx`, `postFilter.ts`

### Configuration
- Site config: `src/config.ts` - Modify SITE object for title, author, social links
- Astro config: `astro.config.ts` - Integrations and build settings
- Theme: Automatic light/dark mode with manual toggle

### Styling
- TailwindCSS v4 with custom configuration in `tailwind.config.js`
- Global styles in `src/styles/base.css`
- Typography plugin for prose content
- Custom CSS variables for theming

### Search Implementation
- Pagefind integration builds search index during production build
- Search UI in `src/components/Search.tsx` (React component)
- Automatic indexing of all blog content

### Key Features to Maintain
1. **SEO**: Sitemap, RSS feed, canonical URLs, structured data
2. **Performance**: Lazy loading images, optimized builds
3. **Accessibility**: Keyboard navigation, ARIA labels, semantic HTML
4. **Type Safety**: Full TypeScript coverage, strict mode
5. **Future Posts**: Scheduled posts with 15-minute publication margin

## Testing Approach
No automated tests are configured. Manual testing recommended for:
- Build process: `pnpm run build` should complete without errors
- TypeScript: No type errors during build
- Formatting/Linting: `pnpm run format:check && pnpm run lint`
- Search functionality: Test after build with `pnpm run preview`

## Development Tips
- When adding new blog posts, follow the schema in `src/content.config.ts`
- OG images are generated automatically; custom ones go in `public/og-images/`
- To modify site metadata, edit `src/config.ts`
- For component changes, check both `.astro` and `.tsx` files as the project uses both
- Pagefind search index is only built in production (`pnpm run build`)