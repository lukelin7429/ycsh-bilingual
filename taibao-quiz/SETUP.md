# Taibao Quiz — connect it to a Google Sheet (one-time, ~3 min)

The quiz page already works on its own (students see their score). To make
answers flow into a Google Sheet you control, do this once.

## 1. Make the Sheet
1. Create a new Google Sheet, e.g. **「永慶 太保小測驗 Taibao Quiz」**.

## 2. Add the script
2. In that Sheet: **Extensions → Apps Script**.
3. Delete the sample code, then paste everything from **`apps-script.gs`** (this folder).
4. Save (💾).

## 3. Deploy as a Web App
5. **Deploy → New deployment**. Click the gear → choose **Web app**.
6. Set:
   - **Execute as:** Me (your account)
   - **Who has access:** **Anyone**  ← required, so students' phones can post anonymously
7. **Deploy** → authorise when prompted → **copy the Web app URL**
   (looks like `https://script.google.com/macros/s/AKfyc…/exec`).

## 4. Point the page at it
8. Open **`index.html`** in this folder. Near the top of the `<script>`:
   ```js
   const ENDPOINT = "PASTE_YOUR_APPS_SCRIPT_WEB_APP_URL_HERE";
   ```
   Replace the placeholder with the URL you copied.
9. Commit & push (the site redeploys automatically).

## Test it
- In the Apps Script editor, run `_smokeTest` once — a test row should appear in the Sheet's **Responses** tab.
- Then open the live page, answer, and submit — you should see a new row arrive instantly.

## During the talk
- Project **<https://ycsh.taiwan-bilingual.org/taibao-quiz/>** — the page shows a QR code.
- Teachers scan it, answer on their phones, and you switch to the Google Sheet to show rows landing live.

## Notes
- The page grades in the browser, so it shows a score even if the backend is not connected yet (it will say "Demo mode").
- Columns written: Time, Class, Name, Score, Total, Q1–Q10 (each like `A ✓` / `C ✗`), Browser.
- If you edit `apps-script.gs` later, redeploy: **Deploy → Manage deployments → edit → Version: New version → Deploy** (the URL stays the same).
