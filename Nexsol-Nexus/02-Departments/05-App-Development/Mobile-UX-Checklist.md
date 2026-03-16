# App Development SOP: Thumb-Friendly UX Checklist

**Objective:** Ensuring every Nexsol mobile app is intuitive, accessible, and high-conversion.

---

## 1. Ergonomic Design (The "Thumb Zone")
*   **Primary Actions:** All CTAs (Buy Now, Cart, Search) must be within the bottom 30% of the screen.
*   **Navigation:** Use a Bottom Tab Bar for primary navigation; avoid "Hamburger" menus on the top-left unless absolutely necessary.
*   **Touch Targets:** Minimum 48dp x 48dp for all interactive elements to prevent "Fat-Finger" errors.

---

## 2. Speed & Perceived Performance
*   **Skeleton Screens:** Use skeleton loaders instead of generic spinning wheels to show progress.
*   **Optimistic UI:** When a user clicks "Like" or "Add to Cart," update the UI immediately before the server confirms the action.
*   **Image Lazy Loading:** Use `react-native-fast-image` for smooth scrolling of product lists.

---

## 3. Transactional Flow (The "One-Tap" Goal)
*   **UPI Integration:** Deep-linking directly to PhonePe/GPay/Google Pay without manual input.
*   **Auto-OTP:** Implement native SMS listeners for one-click login (SME users hate manual OTP typing).
*   **Address Auto-complete:** Use Google Places API to minimize typing for delivery details.

---

## 4. Engagement & Retention
*   **Rich Push Notifications:** Notifications must include product images and action buttons (e.g., "Review Now").
*   **Deep Linking:** Every marketing SMS/WA must open the specific product page inside the app, not just the homepage.
*   **Offline Support:** Crucial for Indian urban/semi-urban areas. Product data must be cached for offline viewing.

---

## 5. QA Verification
- [ ] Tested on a budget Android device (<₹10,000) for performance.
- [ ] "Dark Mode" tested for contrast and readability.
- [ ] App size verified to be <25MB (Post-obfuscation).
- [ ] Splash screen duration <1.5s.
