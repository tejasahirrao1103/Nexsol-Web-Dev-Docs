# Crisis Response SOP: Technical & Client Emergency

**Objective:** Maintaining 99.5% uptime and client trust during failures.

---

## 1. Scenario A: Production Site Down
**Primary Goal:** 15-minute diagnosis, 1-hour resolution.
1. **Detection:** Alerts from monitoring tools (BetterStack/Uptime Robot).
2. **Action:** Engineering Team acknowledges on Slack `#crisis-control`.
3. **Communication:** Account Manager sends "Incident Detected" email to the client within 30 mins.
4. **Fix:** Revert to last stable Git commit or scale server resources.
5. **Post-Mortem:** Document the cause and the permanent fix.

---

## 2. Scenario B: AI Hallucinations/Security Breach
1. **Immediate:** Kill the AI Agent API key.
2. **Security:** Reset all environmental variables and rotation keys.
3. **Disclosure:** Inform affected clients with a clear "Remediation Plan."

---

## 3. Scenario C: Client Conflict / Dispute
1. **Refer to MSA:** The Account Manager points to the signed Master Service Agreement.
2. **Escalation:** If unresolved, move to a "Strategic Pivot Call" with the Agency CEO.
3. **Resolution:** Aim for a win-win (Bonus feature vs. Refund balance) to protect Nexsol's reputation.
