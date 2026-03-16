# Engineering SOP: Next.js Performance & SEO Standards

**Objective:** Guaranteeing sub-2s load times and 95+ PageSpeed scores for all Nexsol builds.
**Technical Lead:** Kanhaiya Wagh.

---

## 1. Speed Benchmarks (Lighthouse Targets)
Every Nexsol build must pass these metrics before being moved to the **Beta Release** stage:

*   **LCP (Largest Contentful Paint):** < 1.2s.
*   **CLS (Cumulative Layout Shift):** < 0.05.
*   **FCP (First Contentful Paint):** < 0.8s.
*   **Performance Score:** 95+ (Desktop) / 85+ (Mobile).

---

## 2. Server-Side Rendering (SSR) Strategy
*   **Default State:** Use **Server Components** by default. Relegate `'use client'` only to interactive leaf components (buttons, input fields, carousels).
*   **Data Fetching:** Fetch data directly in Server Components using `async/await`. Do not use `useEffect` for primary data fetching.
*   **Streaming:** Wrap slow AI-dependent components in `<Suspense>` to allow Progressive Rendering.

---

## 3. Image & Asset Optimization
*   **Nexsol Standard:** Never use raw `<img>` tags. Always use `next/image`.
*   **Formats:** Force `webp` or `avif` via Vercel optimization.
*   **Priority Flags:** Use `priority` for the Hero image (LCP element).
*   **SVG Icons:** Inline shared SVGs or use a sprite sheet; avoid external icon libraries (FontAwesome) that bloat the bundle.

---

## 4. Technical SEO Bridge
A Next.js build is an SEO machine. Engineers must ensure:
1.  **Dynamic Metadata:** Use the `generateMetadata` function for all product and blog routes.
2.  **JSON-LD Schema:** Every page must include structured data (Product, FAQ, or Organization) to win Google rich snippets.
3.  **Sitemap & Robots:** Automated generation via `next-sitemap` on every build.
4.  **OpenGraph:** Dynamic OG images (using `@vercel/og`) for every unique product/blog post to boost Social CTR.

---

## 5. Middleware & Caching
*   **ISR (Incremental Static Regeneration):** Use `revalidate` for product pages (e.g., revalidate every 60 seconds) to balance freshness and speed.
*   **Edge Middleware:** Use Vercel Edge Middleware for geolocation-based redirects or A/B testing logic to ensure zero latency.
