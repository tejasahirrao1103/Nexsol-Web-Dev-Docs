# AI Automation SOP: Workflow Orchestration (n8n, Make, Zapier)

**Objective:** Creating seamless data flow between silos to eliminate manual business overhead.
**Core Tool:** n8n (Self-hosted) for complex logic; Make/Zapier for rapid SME deployments.

---

## 1. Tool Selection Logic
Choose the engine based on the client's scale and complexity:

| Requirement | Preferred Tool | Reason |
| :--- | :--- | :--- |
| High-Volume Data (>5k records/mo) | **n8n** | Cost-effective (No per-task fee), JS nodes for custom logic. |
| SME Lead Capture (Simple) | **Zapier** | Instant integration with 5000+ apps, easy client handover. |
| Visual Logic & Complex APIs | **Make (Integromat)** | Better visual error handling, advanced mapping. |

---

## 2. Standard Automation Blueprints
Every Enterprise client gets these 3 core "High-ROI" loops:

### A. The "Order-to-WhatsApp" Loop
*   **Trigger:** New Order on ONDC/Shopify.
*   **Action 1:** Send personalized invoice via WhatsApp.
*   **Action 2:** Update Google Sheets for fulfillment team.
*   **Action 3:** Add customer to "Re-purchase" nurture sequence.

### B. The "Lead-Scraping & qualification" Loop
*   **Trigger:** New lead on Instagram/Facebook/Website.
*   **Action 1:** Scrub LinkedIn for "Job Title" and "Company Size."
*   **Action 2:** Use GPT-4o to score the lead (1-10).
*   **Action 3:** Post high-score leads (8+) directly to the Sales Team's Slack/WhatsApp.

### C. The "Fulfillment Sync" Loop
*   **Trigger:** Status change in Logistics Provider (Delhivery/BlueDart).
*   **Action 1:** Update order status in the Brand Store DB.
*   **Action 2:** SMS/WhatsApp update to the customer with real-time tracking link.

---

## 3. Error Handling & Monitoring
*   **The "Dead Letter" Trigger:** If an automation fails, the system must IMMEDIATELY notify the Nexsol Support Lead via Discord/Slack.
*   **Data Integrity:** Always use "Verify Step" (checking if data actually exists) before triggering destructive actions (like deleting records or sending final invoices).
*   **Rate Limiting:** Implement "Wait" steps in Zapier/Make to stay within API limits of Shopify/Google.

---

## 4. Security Standards
*   **Secret Management:** Never paste raw API keys into Make/n8n. Use environment variables or their native vault systems.
*   **Audit Log:** Maintain a central log of all automated transactions for the Finance Ops team at the end of each month.
