# AstroPaper Project Documentation Index

## 📋 Quick Reference

| **Project** | AstroPaper |
|-------------|------------|
| **Version** | 5.4.3 |
| **Framework** | Astro 5.10.0 |
| **Type** | Blog Theme |
| **Language** | TypeScript |
| **Styling** | TailwindCSS v4 |

---

## 🏗️ Architecture Overview

### 📁 Core Directory Structure
```
src/
├── assets/          # Static assets (icons, images)
├── components/      # Reusable Astro components
├── data/blog/       # Markdown blog posts
├── layouts/         # Page layout templates
├── pages/           # Route definitions
├── styles/          # Global CSS styles
└── utils/           # Utility functions
```

### 🔧 Configuration Files
- `astro.config.ts` - Astro framework configuration
- `src/config.ts` - Site-specific settings
- `src/content.config.ts` - Content schema definition
- `package.json` - Dependencies and scripts

---

## 📚 Component Library

### 🧩 Core Components
| Component | Purpose | Location |
|-----------|---------|----------|
| `Header.astro` | Navigation header | `src/components/` |
| `Footer.astro` | Site footer | `src/components/` |
| `Card.astro` | Post preview card | `src/components/` |
| `Breadcrumb.astro` | Navigation breadcrumbs | `src/components/` |
| `Pagination.astro` | Page navigation | `src/components/` |
| `Tag.astro` | Post tag display | `src/components/` |

### 📄 Layout Templates
| Layout | Purpose | File |
|--------|---------|------|
| `Layout.astro` | Base HTML structure | `src/layouts/` |
| `Main.astro` | Main content wrapper | `src/layouts/` |
| `PostDetails.astro` | Blog post template | `src/layouts/` |
| `AboutLayout.astro` | About page template | `src/layouts/` |

---

## 🛠️ Utility Functions

### 📊 Content Management
| Function | Purpose | File |
|----------|---------|------|
| `getSortedPosts` | Sort posts by date | `src/utils/getSortedPosts.ts` |
| `getUniqueTags` | Extract unique tags | `src/utils/getUniqueTags.ts` |
| `getPostsByTag` | Filter by tag | `src/utils/getPostsByTag.ts` |
| `postFilter` | Filter posts | `src/utils/postFilter.ts` |
| `slugify` | Generate URL slugs | `src/utils/slugify.ts` |

### 🎨 Image & OG Generation
| Function | Purpose | File |
|----------|---------|------|
| `generateOgImages` | Generate OG images | `src/utils/generateOgImages.ts` |
| `loadGoogleFont` | Load fonts | `src/utils/loadGoogleFont.ts` |

---

## 🚀 Routing System

### 📍 Page Routes
| Route | File | Purpose |
|-------|------|---------|
| `/` | `src/pages/index.astro` | Homepage |
| `/about/` | `src/pages/about.md` | About page |
| `/posts/` | `src/pages/posts/[...page].astro` | Post listing |
| `/posts/[slug]/` | `src/pages/posts/[...slug]/index.astro` | Individual post |
| `/tags/` | `src/pages/tags/index.astro` | Tag listing |
| `/tags/[tag]/` | `src/pages/tags/[tag]/[...page].astro` | Tagged posts |
| `/search/` | `src/pages/search.astro` | Search page |
| `/archives/` | `src/pages/archives/index.astro` | Archive page |

### 🔗 Dynamic Routes
- **Posts**: `[...slug]/index.astro` - Dynamic post routing
- **Tags**: `[tag]/[...page].astro` - Tag-based pagination  
- **Pagination**: `[...page].astro` - Paginated listings
- **OG Images**: `[...slug]/index.png.ts` - Dynamic OG image generation

---

## ⚙️ Configuration Guide

### 🌐 Site Configuration (`src/config.ts`)
```typescript
export const SITE = {
  website: "https://astro-paper.pages.dev/",
  author: "Sat Naing",
  title: "云触角（重庆）科技有限公司",
  desc: "A minimal, responsive and SEO-friendly Astro blog theme.",
  postPerIndex: 4,
  postPerPage: 4,
  scheduledPostMargin: 15 * 60 * 1000, // 15 minutes
  showArchives: true,
  dynamicOgImage: true,
  // ... more options
}
```

### 📝 Content Schema (`src/content.config.ts`)
```typescript
schema: z.object({
  author: z.string().default(SITE.author),
  pubDatetime: z.date(),
  modDatetime: z.date().optional().nullable(),
  title: z.string(),
  featured: z.boolean().optional(),
  draft: z.boolean().optional(),
  tags: z.array(z.string()).default(["others"]),
  ogImage: image().or(z.string()).optional(),
  description: z.string(),
  canonicalURL: z.string().optional(),
  // ... more fields
})
```

---

## 📋 Development Workflow

### 🔧 Essential Commands
```bash
# Development
pnpm run dev          # Start dev server
pnpm run build        # Build for production
pnpm run preview      # Preview build

# Code Quality
pnpm run format       # Format with Prettier
pnpm run lint         # Lint with ESLint
pnpm run sync         # Generate types
```

### 🧪 Build Process
1. **TypeScript Check** - `astro check`
2. **Static Generation** - `astro build` 
3. **Search Index** - `pagefind --site dist`
4. **Asset Copy** - `cp -r dist/pagefind public/`

---

## 🎯 Features

### ✨ Core Features
- **SEO Optimized** - Sitemap, RSS, structured data
- **Responsive Design** - Mobile-first approach
- **Dark/Light Theme** - Automatic system preference
- **Search Integration** - Pagefind search functionality
- **Dynamic OG Images** - Auto-generated social media images
- **Accessibility** - WCAG compliant, keyboard navigation
- **Performance** - Lighthouse score optimization

### 🔍 Search System
- **Search Engine**: Pagefind integration
- **Index Generation**: Build-time indexing
- **UI Component**: React-based search interface
- **Scope**: All blog content automatically indexed

### 📱 Responsive Features
- **Viewport Optimization** - Multiple breakpoints
- **Image Handling** - Responsive images with optimization
- **Touch Navigation** - Mobile-friendly interactions
- **Performance** - Optimized for mobile networks

---

## 🔗 Integration Points

### 🌐 External Services
- **Google Site Verification** - Optional integration
- **Sitemap Generation** - Automatic XML sitemap
- **RSS Feed** - Auto-generated feed
- **Social Sharing** - Built-in share buttons

### 🎨 Styling System
- **TailwindCSS v4** - Utility-first CSS framework
- **Typography Plugin** - Enhanced text styling
- **Custom Variables** - CSS custom properties
- **Theme System** - Dark/light mode support

---

## 🗂️ File Organization

### 📂 Assets Structure
```
src/assets/
├── icons/           # SVG icons
│   ├── IconSearch.svg
│   ├── IconMoon.svg
│   └── ... (navigation icons)
└── images/          # Static images
    └── ... (blog images)
```

### 📄 Content Structure
```
src/data/blog/
├── _releases/       # Version release posts
├── examples/        # Example blog posts
└── *.md            # Regular blog posts
```

---

## 🔧 Customization Guide

### 🎨 Theme Customization
1. **Colors**: Edit TailwindCSS config
2. **Typography**: Modify typography plugin settings  
3. **Layout**: Adjust component templates
4. **Branding**: Update `src/config.ts`

### 📝 Content Management
1. **New Posts**: Add Markdown files to `src/data/blog/`
2. **Frontmatter**: Follow schema in `content.config.ts`
3. **Tags**: Use array format in frontmatter
4. **Images**: Place in `src/assets/images/`

### 🔍 Search Configuration
- **Indexing**: Automatic during build
- **UI**: Customize in `src/components/Search.tsx`
- **Filters**: Modify Pagefind configuration
- **Styling**: Update search component styles

---

## 🚀 Deployment

### 📦 Build Output
- **Static Files** - `dist/` directory
- **Search Index** - `dist/pagefind/`
- **Assets** - Optimized and bundled
- **Sitemap** - Auto-generated XML

### 🌐 Platform Compatibility
- **Static Hosting** - Netlify, Vercel, GitHub Pages
- **CDN Integration** - Automatic asset optimization
- **SEO Ready** - Meta tags, structured data
- **Performance** - Optimized build output

---

## 📖 Reference Links

### 📚 Documentation
- [Project README](./README.md) - Basic setup and features
- [CLAUDE.md](./CLAUDE.md) - AI assistant guidance
- [CHANGELOG.md](./CHANGELOG.md) - Version history

### 🔧 Configuration Files
- [astro.config.ts](./astro.config.ts) - Framework configuration
- [package.json](./package.json) - Dependencies and scripts
- [tsconfig.json](./tsconfig.json) - TypeScript settings

### 🧩 Key Components
- [Header Component](./src/components/Header.astro) - Navigation
- [Layout Template](./src/layouts/Layout.astro) - Base layout
- [Site Config](./src/config.ts) - Site settings

---

*Generated on: ${new Date().toISOString().split('T')[0]}*
*Project Version: 5.4.3*