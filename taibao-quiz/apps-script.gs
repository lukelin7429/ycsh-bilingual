/**
 * Taibao Quiz — Google Apps Script backend (container-bound)
 * ==========================================================
 * Receives quiz submissions from /taibao-quiz/ and appends one row per
 * student to THIS Google Sheet. Self-contained: no SHEET_ID needed because
 * the script is bound to the spreadsheet it lives in.
 *
 * SETUP (one time, ~3 minutes) — see SETUP.md:
 *   1. Create a new Google Sheet (name it e.g. "永慶 太保小測驗 Taibao Quiz").
 *   2. Extensions → Apps Script. Delete the sample code, paste THIS file.
 *   3. Deploy → New deployment → type "Web app".
 *        - Execute as: Me
 *        - Who has access: Anyone            (required for anonymous POST)
 *      Deploy, authorise, and COPY the Web app URL.
 *   4. Paste that URL into ENDPOINT in /taibao-quiz/index.html, then redeploy
 *      the website.
 *
 * After editing this script you must redeploy:
 *   Deploy → Manage deployments → (edit) → Version: New version → Deploy.
 */

var TAB   = 'Responses';                       // sheet tab to write into
var TOTAL = 10;                                // number of questions

var HEADERS = ['Time 時間', 'Class 班級', 'Name 姓名', 'Score 分數', 'Total 滿分',
               'Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10', 'Browser 瀏覽器'];

function doPost(e) {
  try {
    var data = JSON.parse(e.postData.contents);
    var sheet = getSheet_();
    var answers = data.answers || [];
    var row = [
      new Date(),
      String(data.cls  || ''),
      String(data.name || ''),
      Number(data.score || 0),
      Number(data.total || TOTAL),
    ];
    for (var i = 0; i < TOTAL; i++) row.push(String(answers[i] != null ? answers[i] : ''));
    row.push(String(data.user_agent || ''));
    sheet.appendRow(row);
    return jsonOut_({ ok: true });
  } catch (err) {
    return jsonOut_({ ok: false, error: err.toString() });
  }
}

function doGet() {
  return ContentService.createTextOutput('Taibao Quiz endpoint OK.');
}

function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(TAB) || ss.insertSheet(TAB);
  // keep header row in sync
  sheet.getRange(1, 1, 1, HEADERS.length).setValues([HEADERS]).setFontWeight('bold');
  sheet.setFrozenRows(1);
  var maxRows = sheet.getMaxRows();
  if (maxRows >= 2) sheet.getRange(2, 1, maxRows - 1, 1).setNumberFormat('yyyy/MM/dd HH:mm:ss');
  return sheet;
}

function jsonOut_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
                       .setMimeType(ContentService.MimeType.JSON);
}

/* Run this once from the editor to verify a row appears in the Sheet. */
function _smokeTest() {
  doPost({ postData: { contents: JSON.stringify({
    form_id: 'ycsh_taibao_quiz', cls: '101', name: 'Test Student',
    score: 8, total: 10,
    answers: ['A ✓','A ✓','A ✓','A ✓','A ✓','A ✓','A ✓','A ✗','A ✓','A ✗'],
    user_agent: 'smoke-test'
  }) } });
}

/**
 * Live stats tab — run ONCE from the editor (select setupStats → Run).
 * Creates a "Stats" tab with LIVE formulas: respondent count, average score,
 * and per-question correct rate (with a bar). They auto-update as new rows
 * arrive — no redeploy needed, because this only reads the Responses tab.
 */
function setupStats() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var st = ss.getSheetByName('Stats') || ss.insertSheet('Stats');
  st.clear();
  var R = TAB;                                  // 'Responses'
  var cols = ['F','G','H','I','J','K','L','M','N','O'];  // Q1..Q10 columns

  st.getRange('A1').setValue('即時統計 Live Stats').setFontSize(18).setFontWeight('bold').setFontColor('#b5392e');
  st.getRange('A2').setValue('作答人數 Respondents');
  st.getRange('B2').setFormula('=COUNTA(' + R + '!C2:C1000)');
  st.getRange('A3').setValue('平均分 Average (／10)');
  st.getRange('B3').setFormula('=IFERROR(ROUND(AVERAGE(' + R + '!D2:D1000),1),0)');

  st.getRange('A5').setValue('題號 Q').setFontWeight('bold');
  st.getRange('B5').setValue('答對率 Correct %').setFontWeight('bold');
  st.getRange('C5').setValue('長條 Bar').setFontWeight('bold');

  for (var i = 0; i < 10; i++) {
    var r = 6 + i, c = cols[i];
    st.getRange('A' + r).setValue('Q' + (i + 1));
    st.getRange('B' + r).setFormula(
      '=IFERROR(ROUND(SUMPRODUCT(--ISNUMBER(SEARCH("✓",' + R + '!' + c + '2:' + c + '1000)))' +
      '/COUNTA(' + R + '!' + c + '2:' + c + '1000)*100,0),0)');
    st.getRange('C' + r).setFormula('=IFERROR(REPT("█",ROUND(B' + r + '/5,0)),"")');
  }
  st.getRange('B2:B3').setFontWeight('bold');
  st.setColumnWidth(1, 170); st.setColumnWidth(2, 150); st.setColumnWidth(3, 280);
  st.setFrozenRows(1);
}
