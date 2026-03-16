# Engineering SOP: Frontend Aesthetics & Design System

**Objective:** Standardizing the "Nexsol Premium" look across all projects.
**Design Philosophy:** Minimalist, High-Tech, High-Contrast (Glassmorphism).

---

## 1. Typography Standards
We use a two-font system for maximum legibility and authority:

*   **Headings:** `Outfit` (Sans-serif) - Geometric, modern, and high-impact.
*   **Body:** `Inter` (Sans-serif) - The industry standard for readability in SaaS and E-commerce.
*   **Mono:** `JetBrains Mono` - Used sparingly for technical data or code snippets.

---

## 2. The Color Palette (Nexsol Core)
Standard Tailwind configuration for all projects:

```javascript
colors: {
  primary: '#0f172a',    // Slate 900 (Deep Base)
  accent: '#3b82f6',     // Blue 500 (Interaction/CTAs)
  success: '#22c55e',    // Green 500 (Conversions)
  background: '#f8fafc', // Slate 50 (Clean contrast)
  surface: '#ffffff',    // Card/Card background
}
```

---

## 3. Glassmorphism Utilities
All Nexsol sites should include a "Glass" card component for premium feel:

```css
.nexsol-glass {
  background: rgba(255, 255, 255, 0.7);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
}
```

---

## 4. Interaction Standards
*   **Hovers:** Subtle transitions only. Use `transition-all duration-300 ease-in-out`.
*   **Buttons:** Standard CTA should have a subtle drop-shadow (`shadow-blue-500/20`) and scale on click (`active:scale-95`).
*   **Micro-Animations:** Use `framer-motion` for "Entrance" animations (Reveal on scroll) but keep them under 400ms.

---

## 5. Mobile-First Consistency
*   **Touch Targets:** Minimum 44px for all interactive elements.
*   **Horizontal Padding:** Use a standard `px-6` (24px) on mobile containers.
*   **Font Scaling:** Headings should scale down gracefully on mobile to prevent overflow (Use Tailwind's `text-2xl md:text-4xl`).
