# Operations SOP: 50-Point Pre-Launch QA Audit

**Objective:** Ensuring every Nexsol site is functionally perfect and high-performance.
**Auditor:** Operations QA Lead.

---

## 1. Visual & Aesthetic Integrity
- [ ] **Cross-Browser:** Verified on Chrome, Safari, and Brave.
- [ ] **Responsive:** Zero layout shifts on iPhone 13, iPad Pro, and 1920x1080 Monitor.
- [ ] **Typography:** Correct "Outfit" and "Inter" weights applied.
- [ ] **Glassmorphism:** Blur effects correctly rendered on mobile browsers.
- [ ] **Favicon:** Correct Nexsol/Brand favicon appearing in all tabs.

---

## 2. Functional Performance
- [ ] **Add to Cart:** Real-time feedback without page reload.
- [ ] **Checkout Logic:** Tax and shipping calculated correctly based on pincode.
- [ ] **AI Support Bot:** Answers "What is your shipping policy?" and "Price of [Product]" correctly.
- [ ] **Form Submissions:** All lead forms (ROI Audit, Contact) successfully deliver emails to the client.
- [ ] **Searching:** Dynamic search filters return results in <500ms.

---

## 3. Technical Core (Vercel/Next.js)
- [ ] **Lighthouse Performance:** Score 90+ on Mobile.
- [ ] **Images:** All images using `next/image` with proper `priority` flags.
- [ ] **Env Variables:** No local dev URLs left in production code.
- [ ] **SSL:** HTTPS active and non-WWW redirected.
- [ ] **404 Page:** Custom brand-aligned error page functional.

---

## 4. SEO & Analytics
- [ ] **Meta Titles:** Unique and keyword-optimized for every product.
- [ ] **JSON-LD Schema:** Validated via Schema.org for all products.
- [ ] **Sitemap:** `/sitemap.xml` active and contains all live routes.
- [ ] **Analytics:** GA4 (Google Analytics) tag firing on all pages.

---

## 5. ONDC / Backend Integration
- [ ] **Inventory Sync:** Changing a value in the backend reflects on the frontend in <60 seconds.
- [ ] **Order Webhooks:** Successful JSON payload received on test order.
- [ ] **Payment Gateway:** Final live test (₹1 transaction) completed and verified.
