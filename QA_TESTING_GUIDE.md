# QA Testing Guide for Team Leader (Rahul Sir)

This document provides a standard test case to verify the API and UI functionality.

## Instructions
1. Open the application in your browser (e.g., `http://localhost:5000/`).
2. Copy the **Context** below and paste it into the "Context" text area in the UI.
3. Copy each **Question** one by one, paste it into the "Question" box, and click "Ask".
4. Verify that the **Actual Answer** matches the **Expected Answer**.

---

## 1. Context
**Paste this into the Context box:**

```text
The attendance dashboard shows a user’s workday summary. The user clocked in at 10:00 AM and the current time shown is 03:02 PM on Mon, 01 Dec 2025. The dashboard reports Gross Hours: 5h 2m which is the total time from clock-in to now including breaks. It reports Effective Hours: 4h 15m which is the actual working time after excluding breaks and away time. On the same screen the team summary shows My Team: 8h 34m average hours and On Time Arrival: 52% for the team while the user shows AVG HRS / DAY: 0h and ON TIME ARRIVAL: 0%. The UI also displays a “Web Clock-out” action and a note that the user is 0:02:30 late on arrival for that day.
```

---

## 2. Test Questions

| Question | Expected Answer |
|----------|-----------------|
| **What time did the user clock in?** | 10:00 AM |
| **What is the Gross Hours value?** | 5h 2m |
| **What is the Effective Hours value?** | 4h 15m |
| **How long was the user’s break?** | 47 minutes (or similar calculation) |
| **What is the team average hours?** | 8h 34m |
| **What percentage is the team’s on time arrival?** | 52% |
| **What is the user’s on time arrival percentage?** | 0% |
| **What action button is available for logging out or finishing the shift?** | Web Clock-out |
| **What is the user’s arrival lateness for that day?** | 0:02:30 late |
| **Summarize why Effective Hours differ from Gross Hours.** | Effective Hours exclude breaks and away time whereas Gross Hours is total time from clock-in to clock-out including breaks. |

---

## Notes for Tester
- The model (FLAN-T5) is generative, so the exact wording might vary slightly, but the core information should be correct.
- If the "Summarize" question works, it confirms the generative capabilities are active.
