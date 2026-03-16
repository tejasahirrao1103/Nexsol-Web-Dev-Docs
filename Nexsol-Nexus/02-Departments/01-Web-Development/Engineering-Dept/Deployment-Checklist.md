# Engineering SOP: Production Deployment & QA Checklist

**Objective:** Ensuring zero-downtime launches and high-integrity code handovers.
**Platform:** Vercel (Production) / GitHub (Version Control).

---

## 1. Pre-Deployment (Code Quality)
*   **Linting:** Run `npm run lint` and resolve all warnings.
*   **Env Variables:** Verify all `.env.local` keys are also present in Vercel Settings (Production vs Preview).
*   **Unused Code:** Remove all `console.log` statements and unused imports.
*   **Typescript:** Ensure `npm run build` completes with zero TS errors.

---

## 2. Technical Infrastructure
*   **Custom Domain:** Verify SSL (HTTPS) is active and the "non-www" to "www" (or vice versa) redirect is configured.
*   **AI API Limits:** Ensure OpenAI/Anthropic keys have sufficient credits for launch.
*   **Vector DB:** For RAG-enabled sites, verify the Pinecone/Supabase index is populated with the final production data.
*   **Webhooks:** For ONDC/Shopify integration, verify the live webhook URLs are pointing to the production domain.

---

## 3. SEO & Analytics (Verification)
*   **Google Search Console:** Verify domain ownership and submit the sitemap.
*   **GA4/Pixel:** Ensure Google Analytics 4 and Meta Pixels are firing correctly on the "Success" pages.
*   **404 Handling:** Custom 404 page is functional and brand-aligned.
*   **Favicon:** Integrated Nexsol/Client logo for all device sizes (16x16, 32x32, and Apple Touch Icon).

---

## 4. Final Handover (Post-Launch)
*   **Snapshot:** Record a sub-2s PageSpeed report and share it with the Client Success lead.
*   **Repository Transfer:** (If applicable) Invite the client or transfer the GitHub repo.
*   **Documentation:** Update the `README.md` with specific API configuration steps for the client’s team.
*   **Post-Mortem:** Brief the Marketing team on any unique technical challenges solved (for the blog).

---

## 5. Emergency Rollback Strategy
*   **Vercel Instant Rollback:** In case of a critical CSS/Logic break, use the Vercel Dashboard to revert to the previous successful deployment immediately.
*   **Feature Flags:** If used, kill the specific feature through the dashboard rather than a new build.
