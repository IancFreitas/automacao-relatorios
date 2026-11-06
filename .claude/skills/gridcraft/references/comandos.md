# Comandos do GridCraft

341 entradas, geradas automaticamente pela própria CLI. Procure com grep pelo id ou pelo rótulo.

## file

- `file.new` — New Workbook (File) [Cmd+N]
  - params: `{sample?: "budget"|"sales"|"grades"}`
- `file.open` — Open… (File) [Cmd+O]
  - params: `{path} | {name, base64}, plus {password} for a password-protected workbook and {csvAsText?: bool} to keep every csv/tsv/txt field as text, with no number or date conversion (xlsx, xlsm, xls import, xlsb and ods data import, csv, tsv, txt, json)`
- `file.save` — Save (File) [Cmd+S]
  - params: `{path?} (xlsx by default; .csv/.tsv/.json/.html/.pdf by extension)`
- `file.saveAs` — Save As… (File) [Cmd+Shift+S]
  - params: `{path} (.xlsx, .csv, .tsv, .json, .html, or .pdf: a PDF of the active sheet)`
- `file.saveBytes` — Encode Workbook
  - params: `{format?: xlsx|csv|tsv|json|html} → {base64}`
- `file.close` — Close (File) [Cmd+W]
  - params: `{force?: bool}`
- `file.exportCsv` — Export as CSV (File > Export)
  - params: `{path, sheet?}`
- `file.exportHtml` — Save as Web Page (File > Export)
  - params: `{path}`
- `file.properties` — Properties (File)
  - params: `{title?, subject?, author?, company?, keywords?, description?}`
- `file.options` — Options (File)
  - params: `{} → {calculation: {mode, iterative, maxIterations, maxChange}} for the active workbook (the interface opens File › Options; change settings with their own commands, e.g. formulas.calculationOptions, view.theme, app.language.set)`
- `file.exportPdf` — Export as PDF (File > Export)
  - params: `{path?, sheets?: active|all, range?: "A1:F40" (active sheet), fitToPage?: bool} → {pages, bytes, path} or {pages, bytes, base64} when no path. Honours each sheet's Page Setup.`
- `file.print` — Print… (File) [Cmd+P]
  - params: `{path?, sheets?: active|all, range?, fitToPage?: bool} → {pages, bytes, base64} — the PDF the UI hands to the system print dialog`
- `file.printPreview` — Print Preview (File)
  - params: `{page? (1-based), sheets?: active|all, range?, fitToPage?} → {pages, pageList: [{page, sheet, range, rows, columns, scale, paper, orientation, width, height}]}`

## window

- `window.activate` — Switch Window (Window)
  - params: `{index}`

## cell

- `cell.set` — Enter Cell
  - params: `{cell?: "B2", input: "text, number or =formula", sheet?, array?: bool}`
- `cell.get` — Get Cell
  - params: `{cell?, sheet?} → value, formula, display text, style, comment, link`
- `cell.toggleCheckbox` — Toggle Checkbox [Space]
  - params: `{cell?}`

## range

- `range.setValues` — Set Values
  - params: `{range?: "A1", values: [[...]] (rows of numbers/strings/bools/null; strings starting with = are formulas)}`
- `range.fill` — Fill Range With Input [Ctrl+Enter]
  - params: `{range?, input}: enters the same input in every selected cell (relative formulas adjust)`

## selection

- `selection.set` — Select
  - params: `{range: "A1:B2,D4" | cell, active?: "A1", sheet?}`
- `selection.move` — Move Selection
  - params: `{dr, dc, extend?: bool, jump?: bool (Ctrl+arrow), page?: bool}`
- `selection.next` — Next Cell in Selection
  - params: `{forward?: true, byRow?: false} (Enter/Tab inside a selection)`
- `selection.currentRegion` — Select Current Region [Ctrl+Shift+8]
- `selection.row` — Select Entire Row [Shift+Space]
- `selection.column` — Select Entire Column [Ctrl+Space]
- `selection.stats` — Selection Statistics
  - params: `{} → count, sum, average, min, max`

## edit

- `edit.selectAll` — Select All (Edit) [Cmd+A]
  - params: `{} (current region first, then the whole sheet)`
- `edit.goTo` — Go To… (Home > Editing > Find & Select) [Ctrl+G]
  - params: `{reference: "B5" | "Sheet2!A1:C3" | name}`
- `edit.goToSpecial` — Go To Special… (Home > Editing > Find & Select)
  - params: `{kind: blanks|constants|formulas|comments|lastCell|currentRegion|visible|conditionalFormats|dataValidation|errors|numbers|text}`
- `edit.undo` — Undo (Edit) [Cmd+Z]
  - params: `{steps?: 1}`
- `edit.redo` — Redo (Edit) [Cmd+Y]
  - params: `{steps?: 1}`
- `edit.copy` — Copy (Home > Clipboard) [Cmd+C]
  - params: `{range?, html?: bool} → {range, text, html?} (html: a styled HTML table, only when requested and small enough)`
- `edit.cut` — Cut (Home > Clipboard) [Cmd+X]
  - params: `{range?, html?: bool} → {range, text, html?} (html: a styled HTML table, only when requested and small enough)`
- `edit.paste` — Paste (Home > Clipboard) [Cmd+V]
  - params: `{at?: "C3", text?: "tab-separated text from the system clipboard", html?: "the clipboard's HTML flavour; cells the source recorded as numbers (x:num, sdval) stay numbers"}`
- `edit.pasteSpecial` — Paste Special… (Home > Clipboard) [Ctrl+Cmd+V]
  - params: `{what: all|formulas|values|formats|comments|validation|allExceptBorders|columnWidths|formulasAndNumberFormats|valuesAndNumberFormats, operation?: none|add|subtract|multiply|divide, skipBlanks?, transpose?, link?}`
- `edit.clearClipboard` — Cancel Copy [Escape]
- `edit.clearAll` — Clear All (Home > Editing > Clear)
  - params: `{range?}`
- `edit.clearFormats` — Clear Formats (Home > Editing > Clear)
  - params: `{range?}`
- `edit.clearContents` — Clear Contents (Home > Editing > Clear) [Delete]
  - params: `{range?}`
- `edit.clearComments` — Clear Comments and Notes (Home > Editing > Clear)
  - params: `{range?}`
- `edit.clearHyperlinks` — Clear Hyperlinks (Home > Editing > Clear)
  - params: `{range?}`
- `edit.fillDown` — Fill Down (Home > Editing > Fill) [Cmd+D]
  - params: `{range?}`
- `edit.fillRight` — Fill Right (Home > Editing > Fill) [Cmd+R]
  - params: `{range?}`
- `edit.fillUp` — Fill Up (Home > Editing > Fill)
  - params: `{range?}`
- `edit.fillLeft` — Fill Left (Home > Editing > Fill)
  - params: `{range?}`
- `edit.autoFill` — AutoFill
  - params: `{source: "A1:A2", target: "A1:A10", mode?: series|alternate|copy|formats|values}: the fill-handle drag (alternate = Ctrl+drag: a lone number counts up, any other series copies)`
- `edit.fillSeries` — Series… (Home > Editing > Fill)
  - params: `{range?, direction?: columns|rows, type?: linear|growth|date|autofill, step?: 1, stop?, dateUnit?: day|weekday|month|year}`
- `edit.flashFill` — Flash Fill (Home > Editing > Fill) [Ctrl+E]
  - params: `{range?}`
- `edit.find` — Find… (Home > Editing > Find & Select) [Cmd+F]
  - params: `{what, matchCase?, wholeCell?, lookIn?: formulas|values, byColumns?, all?: bool, within?: sheet|workbook}`
- `edit.replace` — Replace… (Home > Editing > Find & Select) [Ctrl+H]
  - params: `{what, with, matchCase?, wholeCell?, all?: true, within?: sheet|workbook}`
- `edit.formatPainter` — Format Painter (Home > Clipboard)
  - params: `{sticky?: bool} — first call picks up the selection's formats; with {apply: "C3:D4"} pastes them`
- `edit.beginEdit` — Edit Cell [F2]

## home

- `home.bold` — Bold (Home > Font) [Cmd+B]
  - params: `{range?, on?: bool}`
- `home.italic` — Italic (Home > Font) [Cmd+I]
  - params: `{range?, on?}`
- `home.underline` — Underline (Home > Font) [Cmd+U]
  - params: `{range?, on?, style?: single|double|singleAccounting|doubleAccounting}`
- `home.doubleUnderline` — Double Underline (Home > Font)
  - params: `{range?}`
- `home.strikethrough` — Strikethrough (Home > Font) [Cmd+Shift+X]
  - params: `{range?, on?}`
- `home.superscript` — Superscript (Home > Font)
  - params: `{range?, on?}`
- `home.subscript` — Subscript (Home > Font)
  - params: `{range?, on?}`
- `home.fontName` — Font (Home > Font)
  - params: `{range?, name: "Calibri"}`
- `home.fontSize` — Font Size (Home > Font)
  - params: `{range?, size: 11}`
- `home.increaseFontSize` — Increase Font Size (Home > Font) [Cmd+Shift+>]
  - params: `{range?}`
- `home.decreaseFontSize` — Decrease Font Size (Home > Font) [Cmd+Shift+<]
  - params: `{range?}`
- `home.fontColor` — Font Color (Home > Font)
  - params: `{range?, color: "#C00000" | "auto" | {theme: 4, tint: -0.25}}`
- `home.fillColor` — Fill Color (Home > Font)
  - params: `{range?, color: "#FFFF00" | "none" | {theme, tint}}`
- `home.borders` — Borders (Home > Font)
  - params: `{range?, preset: bottom|top|left|right|none|all|outside|thickOutside|thickBottom|doubleBottom|topBottom|topThickBottom|topDoubleBottom|insideHorizontal|insideVertical|inside|diagonalDown|diagonalUp, style?: thin|medium|thick|dashed|dotted|double|hair…, color?}`
- `home.formatCells` — Format Cells… (Home > Cells > Format) [Cmd+1]
  - params: `{range?, style: {font?, fill?, borders?, align?, numFmt?, protection?}} (partial Style JSON merged in)`
- `home.alignLeft` — Align Left (Home > Alignment) [Cmd+L]
  - params: `{range?}`
- `home.alignCenter` — Center (Home > Alignment) [Cmd+E]
  - params: `{range?}`
- `home.alignRight` — Align Right (Home > Alignment)
  - params: `{range?}`
- `home.justify` — Justify (Home > Alignment)
  - params: `{range?}`
- `home.alignTop` — Top Align (Home > Alignment)
  - params: `{range?}`
- `home.alignMiddle` — Middle Align (Home > Alignment)
  - params: `{range?}`
- `home.alignBottom` — Bottom Align (Home > Alignment)
  - params: `{range?}`
- `home.wrapText` — Wrap Text (Home > Alignment)
  - params: `{range?, on?}`
- `home.shrinkToFit` — Shrink to Fit
  - params: `{range?, on?}`
- `home.increaseIndent` — Increase Indent (Home > Alignment) [Ctrl+Alt+Tab]
  - params: `{range?}`
- `home.decreaseIndent` — Decrease Indent (Home > Alignment) [Ctrl+Alt+Shift+Tab]
  - params: `{range?}`
- `home.orientation` — Orientation (Home > Alignment)
  - params: `{range?, angle: -90..90 | "vertical" | "counterclockwise" | "clockwise" | "up" | "down" | 0}`
- `home.mergeCenter` — Merge & Center (Home > Alignment)
  - params: `{range?}`
- `home.mergeAcross` — Merge Across (Home > Alignment)
  - params: `{range?}`
- `home.mergeCells` — Merge Cells (Home > Alignment)
  - params: `{range?}`
- `home.unmergeCells` — Unmerge Cells (Home > Alignment)
  - params: `{range?}`
- `home.numberFormat` — Number Format (Home > Number)
  - params: `{range?, format: "General"|"Number"|"Currency"|"Accounting"|"Short Date"|"Long Date"|"Time"|"Percentage"|"Fraction"|"Scientific"|"Text" | code: "0.00"}`
- `home.accounting` — Accounting Number Format (Home > Number)
  - params: `{range?, symbol?: "$"}`
- `home.percent` — Percent Style (Home > Number) [Ctrl+Shift+%]
  - params: `{range?}`
- `home.comma` — Comma Style (Home > Number)
  - params: `{range?}`
- `home.increaseDecimal` — Increase Decimal (Home > Number)
  - params: `{range?}`
- `home.decreaseDecimal` — Decrease Decimal (Home > Number)
  - params: `{range?}`
- `home.cellStyle` — Cell Styles (Home > Styles)
  - params: `{range?, name: "Good"|"Bad"|"Neutral"|"Heading 1"|"Title"|"Total"|"Accent1"…|"Normal"}`
- `home.rowHeight` — Row Height… (Home > Cells > Format)
  - params: `{rows?: "2:5" | "2:2,4:5", height: 20 (points on screen)}`
- `home.columnWidth` — Column Width… (Home > Cells > Format)
  - params: `{cols?: "B:D" | "B:B,D:F", width: 64 (points) | chars: 8.43}`
- `home.autofitRowHeight` — AutoFit Row Height (Home > Cells > Format)
  - params: `{rows?}`
- `home.autofitColumnWidth` — AutoFit Column Width (Home > Cells > Format)
  - params: `{cols?}`
- `home.defaultWidth` — Default Width… (Home > Cells > Format)
  - params: `{width: 64}`
- `home.hideRows` — Hide Rows (Home > Cells > Format > Hide & Unhide) [Cmd+9]
  - params: `{rows?}`
- `home.hideColumns` — Hide Columns (Home > Cells > Format > Hide & Unhide) [Cmd+0]
  - params: `{cols?}`
- `home.unhideRows` — Unhide Rows (Home > Cells > Format > Hide & Unhide) [Cmd+Shift+9]
  - params: `{rows?}`
- `home.unhideColumns` — Unhide Columns (Home > Cells > Format > Hide & Unhide) [Cmd+Shift+0]
  - params: `{cols?}`
- `home.lockCell` — Lock Cell (Home > Cells > Format)
  - params: `{range?, on?}`
- `home.insertRows` — Insert Sheet Rows (Home > Cells > Insert) [Ctrl+Shift+=]
  - params: `{rows?: "3:5", count?}`
- `home.insertColumns` — Insert Sheet Columns (Home > Cells > Insert)
  - params: `{cols?: "B:C"}`
- `home.deleteRows` — Delete Sheet Rows (Home > Cells > Delete) [Cmd+-]
  - params: `{rows?}`
- `home.deleteColumns` — Delete Sheet Columns (Home > Cells > Delete)
  - params: `{cols?}`
- `home.insertCells` — Insert Cells… (Home > Cells > Insert)
  - params: `{range?, shift: right|down|row|column}`
- `home.insertCopiedCells` — Insert Copied Cells (Home > Cells > Insert)
  - params: `{at?: "B3", shift?: down|right}: inserts the copied cells at `at` (the active cell) and pastes them there. Whole copied rows or columns insert whole rows or columns; other blocks shift the cells at `at` down (default) or right. A cut of whole rows or columns moves them (Insert Cut Cells)`
- `home.deleteCells` — Delete Cells… (Home > Cells > Delete)
  - params: `{range?, shift: left|up|row|column}`
- `home.insertSheet` — Insert Sheet (Home > Cells > Insert) [Shift+F11]
  - params: `{name?, before?: index}`
- `home.deleteSheet` — Delete Sheet (Home > Cells > Delete)
  - params: `{sheet?}`
- `home.formatAsTable` — Format as Table (Home > Styles)
  - params: `{range?, style: "TableStyleMedium2", header?}`
- `home.conditionalFormat` — Conditional Formatting (Home > Styles)
  - params: `{range?, rule: {type: cellIs|expression|containsText|beginsWith|endsWith|blanks|noBlanks|errors|noErrors|duplicate|unique|top10|aboveAverage|timePeriod|colorScale|dataBar|iconSet, operator?, value?, value2?, formula?, text?, rank?, bottom?, percent?, below?, period?, colors?: [..], color?, set?, style?: {font..fill..}|preset: lightRedFill|redText|yellowFill|greenFill|redBorder|lightRedFillDarkRedText…}}`
- `home.clearRules` — Clear Rules (Home > Styles > Conditional Formatting)
  - params: `{range?|sheet: true}`
- `home.manageRules` — Manage Rules… (Home > Styles > Conditional Formatting)
  - params: `{delete?: index, moveUp?: index, moveDown?: index}`
- `home.drawBorder` — Draw Border (Home > Font)
  - params: `{range, edge: top|bottom|left|right|grid, style?, color?}`
- `home.newCellStyle` — New Cell Style… (Home > Styles)
  - params: `{name, fromCell?: "A1" (default: active cell)}`
- `home.addIns` — Add-ins (Home > Add-ins)
  - params: `{} → GridCraft extends through MCP and scripts instead of add-ins`

## sheet

- `sheet.moveColumns` — Move Columns
  - params: `{cols?: "B:C", before: zero-based column index}`
- `sheet.rename` — Rename Sheet (Home > Cells > Format)
  - params: `{sheet?, name}`
- `sheet.move` — Move or Copy Sheet… (Home > Cells > Format)
  - params: `{sheet?, to: index, copy?: bool}`
- `sheet.tabColor` — Tab Color (Home > Cells > Format)
  - params: `{sheet?, color: "#FF0000"|"none"}`
- `sheet.hide` — Hide Sheet (Home > Cells > Format > Hide & Unhide)
  - params: `{sheet?}`
- `sheet.unhide` — Unhide Sheet… (Home > Cells > Format > Hide & Unhide)
  - params: `{sheet}`
- `sheet.activate` — Activate Sheet
  - params: `{sheet: index | name}`
- `sheet.next` — Next Sheet [Ctrl+PageDown]
- `sheet.previous` — Previous Sheet [Ctrl+PageUp]
- `sheet.read` — Read Range
  - params: `{range?: "A1:D10" (default: used range), sheet?, formulas?: bool, formatted?: bool} → rows of values`

## insert

- `insert.table` — Table (Insert > Tables) [Cmd+T]
  - params: `{range?, header?: true, style?: "TableStyleMedium2", name?}`
- `insert.chart` — Insert Chart (Insert > Charts)
  - params: `{range?, type?: column|bar|line|pie|doughnut|area|scatter|bubble|radar|combo|histogram|waterfall|funnel|treemap|sunburst|boxWhisker|stock, subtype?: clustered|stacked|stacked100|markers, title?, at?: "H2", width?, height?}`
- `insert.recommendedCharts` — Recommended Charts (Insert > Charts)
  - params: `{range?, type?, subtype?} (no type: the first of insert.chartRecommendations; the ribbon button opens the dialog)`
- `insert.chartRecommendations` — Chart Recommendations
  - params: `{range?} → [{type, subtype, label}] chart types that suit the data's shape, best first`
- `insert.sparkline` — Sparklines (Insert > Sparklines)
  - params: `{range: "B2:M2", location: "N2", type?: line|column|winLoss, markers?}`
- `insert.picture` — Picture (Insert > Illustrations)
  - params: `{path? | base64?: "...", mime?, at?: "B2", width?, height?, alt?, mode?: moveOnly|moveAndSize|absolute, placement?: cell|overCells}`
- `insert.shape` — Shapes (Insert > Illustrations)
  - params: `{kind: rectangle|roundedRectangle|ellipse|triangle|line|arrow|textBox, at?, width?, height?, text?, fill?, line?}`
- `insert.icons` — Icons (Insert > Illustrations)
  - params: `{name: chart|table|sum|filter|lock|comment|picture|book|folder|search|calc|check|… , at?, size?: 48, color?: hex}`
- `insert.textBox` — Text Box (Insert > Text)
  - params: `{at?, width?, height?, text?}`
- `insert.link` — Link (Insert > Links) [Cmd+K]
  - params: `{cell?, target: "https://…" | "Book.xlsx" | "Sheet2!A1" | "mailto:…", text?, tooltip?, remove?: bool}`
- `insert.symbol` — Symbol (Insert > Symbols)
  - params: `{char: "€"} (inserted at the end of the active cell's text)`
- `insert.checkbox` — Checkbox (Insert > Cell Controls)
  - params: `{range?} (TRUE/FALSE and empty cells draw as checkboxes, empty ones become FALSE, other values show as they are; click or Space toggles; Delete unchecks, then removes; Clear Formats removes and keeps the values)`
- `insert.pivotTable` — PivotTable (Insert > Tables)
  - params: `{source?: "Sheet1!$A$1:$E$200" | table name (default: the table or current region of the selection), destination?: "new" (default: new sheet before the current one, report at A3) | "Sheet1!H3", name?, rows?: [field | {field, group?: years|quarters|months|days}], columns?: [..], values?: [field | {field, func?, name?}], filters?: [field], replace?: bool} → {id, name, sheet, anchor, fields}`
- `insert.recommendedPivotTables` — Recommended PivotTables (Insert > Tables)
  - params: `{source?, apply?: index, destination?} → suggestions [{index, title, rows, columns, values}]; with apply, creates that one`
- `insert.pivotChart` — PivotChart (Insert > Charts)
  - params: `{pivot?: name | id | a cell of the report ("Sheet2!B5"; default: the PivotTable at the active cell), type?: column|bar|line|pie|area|… (default column), subtype?, title?, at?: "H2", width?, height?} adds a chart bound to the PivotTable's report: categories are the innermost row items, series the column items × value fields; it follows refreshes and layout changes → {chart, pivot, series}`
- `insert.slicer` — Slicer (Insert > Filters)
  - params: `{table?, column?: "Region", columns?: 1, at?: "H2", width?, height?}`

## table

- `table.totalRow` — Total Row (Table > Table Style Options)
  - params: `{table?, on?: bool}`
- `table.bandedRows` — Banded Rows (Table > Table Style Options)
  - params: `{table?, on?}`
- `table.bandedColumns` — Banded Columns (Table > Table Style Options)
  - params: `{table?, on?}`
- `table.headerRow` — Header Row (Table > Table Style Options)
  - params: `{table?, on?}`
- `table.firstColumn` — First Column (Table > Table Style Options)
  - params: `{table?, on?}`
- `table.lastColumn` — Last Column (Table > Table Style Options)
  - params: `{table?, on?}`
- `table.style` — Table Styles (Table > Table Styles)
  - params: `{table?, style}`
- `table.rename` — Table Name (Table > Properties)
  - params: `{table?, name}`
- `table.convertToRange` — Convert to Range (Table > Tools)
  - params: `{table?}`
- `table.totalFunction` — Totals Function
  - params: `{table?, column: "Sales", function: sum|average|count|countNums|max|min|stdDev|var|none}`
- `table.resize` — Resize Table (Table Design > Properties)
  - params: `{table?, range: "A1:F20"}`
- `table.removeDuplicates` — Remove Duplicates (Table Design > Tools)
  - params: `{table?, columns?}`
- `table.summarizePivot` — Summarize with PivotTable (Table Design > Tools)
  - params: `{table?, destination?} creates a PivotTable from the table`
- `table.insertSlicer` — Insert Slicer (Table > Tools)
  - params: `{table?, column?: "Region", columns?: 1, at?, width?, height?}`

## chart

- `chart.set` — Chart Properties (Chart Design)
  - params: `{chart?: id, type?, title?, legend?: none|bottom|top|left|right, dataLabels?, gridlines?, style?, xTitle?, yTitle?, at?, width?, height?, dx?, dy?}`
- `chart.switchRowColumn` — Switch Row/Column (Chart Design > Data)
  - params: `{chart?}`
- `chart.delete` — Delete Chart
  - params: `{chart?}`
- `chart.addElement` — Add Chart Element (Chart Design > Chart Layouts)
  - params: `{chart?, element: title|legend|dataLabels|gridlines|axisTitles|smooth|trendline, on?: bool, position?: bottom|top|left|right; trendline: series?: index (default all), type?: linear|exponential|linearForecast|movingAverage|logarithmic|power|polynomial, order?: 2..6, period?: 2..255, forward?, backward?, displayEquation?, displayRSquared?}`
- `chart.quickLayout` — Quick Layout (Chart Design > Chart Layouts)
  - params: `{chart?, layout: 1..6}`
- `chart.changeColors` — Change Colors (Chart Design > Chart Styles)
  - params: `{chart?, palette: colorful|monochrome|accent1..accent6 | colors: [hex…]}`
- `chart.selectData` — Select Data… (Chart Design > Data)
  - params: `{chart?, range?: "Sheet1!A1:D7", byRows?: bool, categories?: "Sheet1!A2:A7" (Horizontal (Category) Axis Labels for every series; "" clears), removeSeries?: [index…]}`
- `chart.changeType` — Change Chart Type… (Chart Design > Type)
  - params: `{chart?, type, subtype?}`
- `chart.move` — Move Chart… (Chart Design > Location)
  - params: `{chart?, sheet?: name (moves to that sheet), at?: "B2"}`
- `chart.formatSelection` — Format Selection (Format > Current Selection)
  - params: `{chart?, series?: index, color?: hex}`
- `chart.shapeFill` — Shape Fill (Format > Shape Styles)
  - params: `{chart? | kind: shape, id?, series?, color: hex}`
- `chart.shapeOutline` — Shape Outline (Format > Shape Styles)
  - params: `{kind: shape, id?, color: hex}`

## shape

- `shape.setText` — Edit Text Box
  - params: `{id: textBox id, text: string}`

## object

- `object.delete` — Delete Object
  - params: `{kind: chart|image|shape, id}`
- `object.move` — Move Object
  - params: `{kind: chart|image|shape, id, at?: "C3", dx?, dy?, width?, height?}`
- `object.setAnchorMode` — Object Properties
  - params: `{kind: chart|image|shape, id, mode: moveAndSize|moveOnly|absolute}`

## link

- `link.open` — Open Hyperlink
  - params: `{url?: "https://…" | "mailto:…" | "Sheet2!A1", cell?} (default: the cell's link); only http, https and mailto are opened, any other scheme is an error; the UI asks before opening`

## review

- `review.newNote` — New Note (Review > Notes) [Shift+F2]
  - params: `{cell?, text, author?}`
- `review.newComment` — New Comment (Review > Comments) [Cmd+Shift+F2]
  - params: `{cell?, text, author?}`
- `review.replyComment` — Reply
  - params: `{cell?, text, author?}`
- `review.resolveComment` — Resolve Thread
  - params: `{cell?, resolved?: true}`
- `review.deleteComment` — Delete Comment (Review > Comments)
  - params: `{cell?}`
- `review.showNote` — Show/Hide Note (Review > Notes)
  - params: `{cell?}`
- `review.protectSheet` — Protect Sheet… (Review > Protect)
  - params: `{password?, formatCells?, formatColumns?, formatRows?, insertRows?, insertColumns?, deleteRows?, deleteColumns?, sort?, autofilter?}`
- `review.unprotectSheet` — Unprotect Sheet (Review > Protect)
  - params: `{password?}`
- `review.protectWorkbook` — Protect Workbook (Review > Protect)
  - params: `{on?: bool (default: toggle), password?} (structure protection; unprotecting needs the password when one was set)`
- `review.workbookStatistics` — Workbook Statistics (Review > Proofing)
- `review.allowEditRanges` — Allow Edit Ranges… (Review > Protect)
  - params: `{action?: list (default) | add | modify | delete | unlock, title?, range?, password?, newTitle?, sheet?} → ranges`
- `review.checkAccessibility` — Check Accessibility (Review > Accessibility)
  - params: `{} → issues`
- `review.previousComment` — Previous Comment (Review > Comments)
  - params: `{} → {sheet, cell}`
- `review.nextComment` — Next Comment (Review > Comments)
  - params: `{} → {sheet, cell}`
- `review.showComments` — Show Comments (Review > Comments)
  - params: `{on?: bool} (toggles the Comments pane)`
- `review.showAllNotes` — Show All Notes (Review > Notes)
  - params: `{on?: bool}`
- `review.convertToComments` — Convert to Comments (Review > Notes)
  - params: `{} (every note in the workbook) → {converted}`
- `review.spelling` — Spelling (Review > Proofing) [F7]
  - params: `{range?, sheet?} → misspelled words with cells and suggestions`
- `review.addToDictionary` — Add to Dictionary
  - params: `{word}`
- `review.changeSpelling` — Change
  - params: `{cell, word, to, all?: bool}`
- `review.thesaurus` — Thesaurus (Review > Proofing)
  - params: `{word} → related words (words sharing the stem in the dictionary)`

## data

- `data.sortAscending` — Sort A to Z (Data > Sort & Filter)
  - params: `{range?, column?: "B"}`
- `data.sortDescending` — Sort Z to A (Data > Sort & Filter)
  - params: `{range?, column?}`
- `data.sort` — Sort… (Data > Sort & Filter)
  - params: `{range?, header?: bool, keys: [{column: "B", order: asc|desc, by?: values|cellColor|fontColor, customList?: [..]}], orientation?: rows|columns, matchCase?}`
- `data.filter` — Filter (Data > Sort & Filter) [Ctrl+Shift+L]
  - params: `{range?} toggles AutoFilter on the current region`
- `data.filterBy` — Filter Column
  - params: `{column: "B" (or 0-based offset), values?: [..], blanks?: bool, custom?: {op: ">", value: "10", op2?, value2?, and?}, top?: {count, bottom?, percent?}, aboveAverage?: bool, clear?: bool}`
- `data.clearFilter` — Clear (Data > Sort & Filter)
- `data.reapply` — Reapply (Data > Sort & Filter)
- `data.removeDuplicates` — Remove Duplicates (Data > Data Tools)
  - params: `{range?, columns?: ["A","C"], header?: bool}`
- `data.textToColumns` — Text to Columns (Data > Data Tools)
  - params: `{range?, delimiters?: [",", "\t", " ", ";"], other?: "|", fixedWidths?: [5, 10], treatConsecutive?: bool, textQualifier?: "\"", destination?: "B1"}`
- `data.validation` — Data Validation… (Data > Data Tools)
  - params: `{range?, type: any|whole|decimal|list|date|time|textLength|custom, operator?: between|notBetween|equal|notEqual|greater|less|greaterOrEqual|lessOrEqual, formula1, formula2?, ignoreBlank?, dropdown?, inputTitle?, inputMessage?, errorStyle?: stop|warning|information, errorTitle?, errorMessage?, clear?: bool}`
- `data.validate` — Check Value Against Validation
  - params: `{cell?, input} → {ok, message?}`
- `data.circleInvalid` — Circle Invalid Data (Data > Data Tools > Data Validation)
  - params: `{} → invalid cells`
- `data.group` — Group (Data > Outline) [Alt+Shift+Right]
  - params: `{rows?: "2:5" | cols?: "B:C" | by?: rows|cols (the selection's rows or columns; a block of cells groups rows by default)}`
- `data.ungroup` — Ungroup (Data > Outline) [Alt+Shift+Left]
  - params: `{rows? | cols? | by?: rows|cols}`
- `data.hideDetail` — Hide Detail (Data > Outline)
  - params: `{rows? | cols? | by?, level?: 1-7} (the innermost group, or the one at `level`, holding the lines or summarised by them)`
- `data.showDetail` — Show Detail (Data > Outline)
  - params: `{rows? | cols? | by?, level?: 1-7}`
- `data.showLevels` — Show Outline Levels
  - params: `{rows?: 1-8, cols?: 1-8} (1 shows only the top-level summaries, as the outline's level buttons)`
- `data.subtotal` — Subtotal (Data > Outline)
  - params: `{range?, groupBy: "A", function?: sum|count|average|max|min|product, columns: ["C"], header?: true}`
- `data.flashFill` — Flash Fill (Data > Data Tools)
  - params: `{range?}`
- `data.fromTextCsv` — From Text/CSV (Data > Get & Transform Data)
  - params: `{path | text, delimiter?: ",", sheet?: new sheet name} → imports into a new sheet as a table`
- `data.getData` — Get Data (Data > Get & Transform Data)
  - params: `{path | text} (CSV/TSV/JSON array of objects) → new sheet table`
- `data.fromTableRange` — From Table/Range (Data > Get & Transform Data)
  - params: `{range?} → copies the table/range to a new sheet as a table`
- `data.queriesConnections` — Queries & Connections (Data > Queries & Connections)
  - params: `{} → imported tables`
- `data.solver` — Solver… (Data > Analysis)
  - params: `{objective: "B10" (formula cell), goal?: max|min|value (default max), value?: number (for goal value), variables: "B2:B4,D1" (≤200 constant cells, same sheet), constraints?: ["B5 <= 10", "B2:B4 >= C2:C4", "B2 int", "B3 bin", {lhs: "B6", op: "=", rhs: 3 | "C6"}], nonNegative?: bool (default true: variables without a lower bound get 0), method?: grg|simplex|evolutionary (default grg), populationSize?: 100, mutationRate?: 0.075, randomSeed?: 0 (a fixed seed, so runs repeat), convergence?: 0.0001, generationsWithoutImprovement?: 50, requireBounds?: bool (default true: every variable needs both bounds; false searches within ±100 of the start) (Evolutionary options), keep?: bool (default true; false restores the original values), saveModel?: bool (default true: hidden solver_* names), maxEvaluations?: 20000, integerOptimality?: percent (default 0), saved?: bool (solve the sheet's saved model; other params override), reports?: [answer|limits] (written on new sheets when a solution is found)} → {status: optimal|converged|cannotImprove|iterationLimit|infeasible|unbounded|notLinear, message, objective, values: {cell: value}, original: {cell: value}, model: the model as params, evaluations, changed, reports?: [sheet names]}. No `objective` → {model: the saved model} (the menu opens the dialog).`
- `data.solverReport` — Solver Reports
  - params: `{reports: [answer|limits], values?: {cell: number} (the solution; default the variable cells' current values), original?: {cell: number} (the values before solving; default `values`), message?: text (the result line), model?: data.solver params (default the sheet's saved model, with any data.solver params given here over it)} → {sheets: [names]}. Writes Answer and Limits reports on new sheets before the model's sheet; Limits needs Simplex LP or GRG Nonlinear and no integer constraints. data.solver's result can be passed as is.`
- `data.refreshAll` — Refresh All (Data > Queries & Connections) [Cmd+Alt+F5]
  - params: `{replace?} refreshes every PivotTable → {refreshed, errors}`
- `data.goalSeek` — Goal Seek… (Data > Forecast > What-If Analysis)
  - params: `{set: "B5" (formula cell), to: number, changing: "B2" (constant cell)} → {value, result, iterations, converged}. Secant search with bisection once the answer is bracketed; stops within Maximum Change (0.001) or after Maximum Iterations (100) from File › Options › Formulas. Writes the found value into `changing`.`
- `data.scenarioManager` — Scenario Manager… (Data > Forecast > What-If Analysis)
  - params: `{sheet?} → {scenarios: [{name, sheet, changing, values, comment}]} (scenarios of the active sheet; `sheet: "*"` lists all)`
- `data.scenarioAdd` — Add Scenario
  - params: `{name, changing: "B2:B4" or "B2,B4" (≤32 cells, active sheet), values?: [..] (default: the cells' current values), comment?, replace?: bool}`
- `data.scenarioShow` — Show Scenario
  - params: `{name} writes the scenario's values into its changing cells`
- `data.scenarioDelete` — Delete Scenario
  - params: `{name}`
- `data.scenarioSummary` — Scenario Summary
  - params: `{resultCells?: "B10" or "B10:B12,D4"} inserts a "Scenario Summary" sheet: changing cells and result cells for the current values and each scenario`
- `data.dataTable` — Data Table… (Data > Forecast > What-If Analysis)
  - params: `{range: "D2:E10", rowInput?: "B1", columnInput?: "B2"} one-variable (values down the first column with columnInput, or across the top row with rowInput; formulas in the other edge) or two-variable (formula in the top-left corner). Computes every result by substitution and writes static values (a snapshot, not a live {=TABLE()}); ≤100,000 cells.`
- `data.advancedFilter` — Advanced… (Data > Sort & Filter)
  - params: `{range? (list with headers; default current region), criteria: "H1:I3" (header row of field names; rows OR'ed, columns AND'ed; ">100", "=abc", "a*", "<>"; blank-headed formula cells are computed criteria for the first data row), copyTo?: "K1" (else filter in place by hiding rows), unique?: bool}`
- `data.consolidate` — Consolidate… (Data > Data Tools)
  - params: `{sources: ["Sheet2!A1:C10", ..], destination?: "A1" (default active cell), function?: sum|count|countNums|average|max|min|product, topRow?: bool, leftColumn?: bool (consolidate by labels; else by position)}`
- `data.forecastSheet` — Forecast Sheet (Data > Forecast)
  - params: `{timeline?: "A2:A25", values?: "B2:B25" (default: the first two columns of `range`, the selection or the current region; a text first cell is the header), end?: timeline value or date text | periods?: n (default: a third of the history, at least 1; ≤10,000 and history × periods ≤ 500,000; history ≤ 10,000 rows), forecastStart?: a timeline value or date text on the history, before its last point (hindcast: the model is fit to the points before it, the forecast columns start there and run over the actuals; default and the last point: forecast after the history), confidenceInterval?: bool (default true), confidence?: 0.95 or 95, seasonality?: "auto" | 0 (none) | 2–8,760, fillMissing?: interpolate|zeros, aggregate?: average|count|counta|max|median|min|sum, statistics?: bool, chart?: line|column} → {sheet, table, chart, history, periods}. Inserts a sheet before the active one: timeline, values, Forecast (FORECAST.ETS), Lower/Upper Confidence Bound (FORECAST.ETS.CONFINT), optional FORECAST.ETS.STAT table, and a chart.`
- `data.analysisToolPak` — Data Analysis… (Data > Analysis)
  - params: `{tool: anovaSingle|correlation|covariance|descriptive|exponentialSmoothing|fTest|histogram|movingAverage|rankPercentile|regression|tTestPaired|tTestEqual|tTestUnequal (or the tool's label), output?: "E1" (top-left of the report; default a new sheet), newSheet?: name, outputTo?: range|newSheet (picks between the two), overwrite?: bool (else non-empty output cells are refused), labels?: bool (first row/column holds names), groupedBy?: columns|rows, …tool params} — range tools take `range`; descriptive: summary? (default true), confidence?: 95, kthLargest?, kthSmallest?; histogram: bins?: range (default evenly spaced), pareto?, cumulative?; regression: inputY, inputX, constantZero?, confidence?: 95, residuals?, standardizedResiduals?, normalProbability?; movingAverage: interval? (3), standardErrors?; exponentialSmoothing: damping? (0.3), standardErrors?; t-tests and fTest: range1, range2, alpha? (0.05), hypothesizedDifference? (0); anovaSingle: alpha?. Writes static values. No `tool` → {tools} (the menu opens the dialog).`

## formulas

- `formulas.autoSum` — AutoSum (Formulas > Function Library) [Cmd+Shift+T]
  - params: `{function?: SUM|AVERAGE|COUNT|MAX|MIN, range?}`
- `formulas.insertFunction` — Insert Function… (Formulas > Function Library) [Shift+F3]
  - params: `{name?: "VLOOKUP"} (UI opens the dialog; with a name, starts the formula in the active cell)`
- `formulas.functions` — List Functions
  - params: `{category?, search?} → [{name, category, signature, description}]`
- `formulas.defineName` — Define Name… (Formulas > Defined Names)
  - params: `{name, refersTo?: "=Sheet1!$A$1:$A$10" (default: the selection), scope?: "Workbook"|sheet name, comment?, oldName?, oldScope?} (oldName: edit that name (Name Manager › Edit); a new name also renames it in formulas)`
- `formulas.deleteName` — Delete Name
  - params: `{name, scope?: "Workbook"|sheet name (default: every scope)}`
- `formulas.nameManager` — Name Manager (Formulas > Defined Names) [Cmd+F3]
  - params: `{} → names with values`
- `formulas.createFromSelection` — Create from Selection (Formulas > Defined Names) [Cmd+Shift+F3]
  - params: `{range?, top?: true, left?: false, bottom?: false, right?: false, replace?: false (existing names are kept and listed in `skipped`)}`
- `formulas.tracePrecedents` — Trace Precedents (Formulas > Formula Auditing)
  - params: `{cell?} → ranges`
- `formulas.traceDependents` — Trace Dependents (Formulas > Formula Auditing)
  - params: `{cell?} → cells`
- `formulas.removeArrows` — Remove Arrows (Formulas > Formula Auditing)
- `formulas.showFormulas` — Show Formulas (Formulas > Formula Auditing) [Ctrl+`]
  - params: `{on?}`
- `formulas.errorChecking` — Error Checking (Formulas > Formula Auditing)
  - params: `{} → cells with errors`
- `formulas.evaluateFormula` — Evaluate Formula (Formulas > Formula Auditing)
  - params: `{cell?, formula?} → steps`
- `formulas.evaluate` — Evaluate
  - params: `{formula: "=SUM(A1:A3)", cell?} → value without changing the sheet`
- `formulas.calculateNow` — Calculate Now (Formulas > Calculation) [F9]
- `formulas.calculateSheet` — Calculate Sheet (Formulas > Calculation) [Shift+F9]
- `formulas.calculationOptions` — Calculation Options (Formulas > Calculation)
  - params: `{mode?: automatic|automaticExceptTables|manual, iterative?: bool (Enable iterative calculation), maxIterations?: 1–32767 (100), maxChange?: number (0.001)} → the settings. File › Options › Formulas › Calculation options; stored in the workbook.`
- `formulas.recentlyUsed` — Recently Used (Formulas > Function Library)
  - params: `{} → recently used functions in this workbook`
- `formulas.financial` — Financial (Formulas > Function Library)
- `formulas.logical` — Logical (Formulas > Function Library)
- `formulas.text` — Text (Formulas > Function Library)
- `formulas.dateTime` — Date & Time (Formulas > Function Library)
- `formulas.lookupReference` — Lookup & Reference (Formulas > Function Library)
- `formulas.mathTrig` — Math & Trig (Formulas > Function Library)
- `formulas.moreFunctions` — More Functions (Formulas > Function Library)
  - params: `{category?: Statistical|Engineering|Information|Database|Compatibility|Web|Cube}`
- `formulas.useInFormula` — Use in Formula (Formulas > Defined Names)
  - params: `{name} (inserts the name into the cell being edited)`
- `formulas.watchWindow` — Watch Window (Formulas > Formula Auditing)
  - params: `{add?: "Sheet1!B5", remove?: "…"} → watched cells with current values`

## view

- `view.freezePanes` — Freeze Panes (View > Window > Freeze Panes)
  - params: `{cell?: "B2" (rows above and columns left of it freeze)}`
- `view.freezeTopRow` — Freeze Top Row (View > Window > Freeze Panes)
- `view.freezeFirstColumn` — Freeze First Column (View > Window > Freeze Panes)
- `view.unfreezePanes` — Unfreeze Panes (View > Window > Freeze Panes)
- `view.gridlines` — Gridlines (View > Show)
  - params: `{on?}`
- `view.headings` — Headings (View > Show)
  - params: `{on?}`
- `view.showZeros` — Show Zeros
  - params: `{on?}`
- `view.rightToLeft` — Sheet Right-to-Left (Page Layout > Sheet Options)
  - params: `{on?}`
- `view.zoom` — Zoom (View > Zoom)
  - params: `{percent: 10..400}`
- `view.zoom100` — 100% (View > Zoom)
- `view.formulaBar` — Formula Bar (View > Show)
  - params: `{on?: bool}`
- `view.zoomToSelection` — Zoom to Selection (View > Zoom)
  - params: `{viewWidth?, viewHeight?}`
- `view.normal` — Normal (View > Workbook Views)
  - params: `{sheet?} → {view} (per sheet, saved with the file)`
- `view.pageLayout` — Page Layout (View > Workbook Views)
  - params: `{sheet?} → {view}: pages on paper with rulers; headers and footers are edited in place (per sheet, saved with the file)`
- `view.pageBreakPreview` — Page Break Preview (View > Workbook Views)
  - params: `{sheet?} → {view} (per sheet, saved with the file)`
- `view.customViews` — Custom Views… (View > Workbook Views)
  - params: `{save?: name, show?: name, delete?: name} → list`
- `view.split` — Split (View > Window)
  - params: `{} (toggles a split at the active cell; shown as frozen panes in this version)`
- `view.newWindow` — New Window (View > Window)
  - params: `{} opens a second window on the same workbook (a linked copy)`
- `view.arrangeAll` — Arrange All (View > Window)
- `view.hideWindow` — Hide (View > Window)
- `view.unhideWindow` — Unhide… (View > Window)
  - params: `{index?}`
- `view.switchWindows` — Switch Windows (View > Window)
  - params: `{} → open windows`
- `view.ruler` — Ruler (View > Show)
  - params: `{on?} → {on}: rulers in Page Layout view (an application option)`
- `view.macros` — Macros (View > Macros)
  - params: `{} → scripts`

## pageLayout

- `pageLayout.orientation` — Orientation (Page Layout > Page Setup)
  - params: `{orientation: portrait|landscape}`
- `pageLayout.size` — Size (Page Layout > Page Setup)
  - params: `{paper: Letter|Legal|A4|A3|A5|Tabloid|Executive}`
- `pageLayout.margins` — Margins (Page Layout > Page Setup)
  - params: `{preset?: normal|wide|narrow, left?, right?, top?, bottom?, header?, footer? (inches)}`
- `pageLayout.printArea` — Set Print Area (Page Layout > Page Setup > Print Area)
  - params: `{range?, clear?: bool}`
- `pageLayout.printTitles` — Print Titles (Page Layout > Page Setup)
  - params: `{rows?: "1:1", cols?: "A:A"}`
- `pageLayout.scaleToFit` — Scale to Fit (Page Layout > Scale to Fit)
  - params: `{scale?: 100, width?: pages, height?: pages}`
- `pageLayout.printGridlines` — Print Gridlines (Page Layout > Sheet Options)
  - params: `{on?}`
- `pageLayout.printHeadings` — Print Headings (Page Layout > Sheet Options)
  - params: `{on?}`
- `pageLayout.breaks` — Breaks (Page Layout > Page Setup)
  - params: `{insert?: bool, remove?: bool, reset?: bool, cell?}`
- `pageLayout.headerFooter` — Header & Footer (Insert > Text)
  - params: `{sheet?, header?: "&C&P", footer?: "&CPage &P of &N", differentFirst?: bool, differentOddEven?: bool, firstHeader?, firstFooter?, evenHeader?, evenFooter?} or one section: {sheet?, page?: odd|even|first, part: header|footer, section: left|center|right, text: "Page &[Page] of &[Pages]"} (field names or codes) → {header, footer, differentFirst, differentOddEven, firstHeader, firstFooter, evenHeader, evenFooter}`
- `pageLayout.theme` — Themes (Page Layout > Themes)
  - params: `{name: Craft|Slate|Meadow|Ember|Ocean|Orchid|Graphite, colors?: [12 hex], majorFont?, minorFont?}`
- `pageLayout.themeColors` — Colors (Page Layout > Themes)
  - params: `{name: theme name | colors: [12 hex]}`
- `pageLayout.themeFonts` — Fonts (Page Layout > Themes)
  - params: `{major, minor}`
- `pageLayout.themeEffects` — Effects (Page Layout > Themes)
  - params: `{name} (chart effects preset; stored with the theme name)`
- `pageLayout.background` — Background (Page Layout > Page Setup)
  - params: `{path? | clear?: bool} (sheet background picture)`
- `pageLayout.pageSetup` — Page Setup… (Page Layout > Page Setup)
  - params: `{sheet?, orientation?: portrait|landscape, paper?: Letter|Legal|A4|A3|A5|Tabloid|Executive|Ledger|B5, margins?: {left,right,top,bottom,header,footer} (inches; also accepted as top-level keys), scale?: 10..400, fitWidth?, fitHeight? (pages; 0 = automatic), fitToPage?: bool, centerH?, centerV?, gridlines?, headings?, header?: "&L&A&RPage &P of &N", footer?, printArea?: "A1:F50" ("" clears), titleRows?: "1:2", titleCols?: "A:A", rowBreaks?: [46, 91], colBreaks?: ["K"]} → the sheet's print settings`

## document

- `document.inspect` — Inspect Workbook
  - params: `{} → sheets, selection, names, tables, charts, dirty, history`

## history

- `history.list` — Undo History
  - params: `{} → undo/redo labels`

## app

- `app.commands` — List Commands
  - params: `{search?} → ids, labels, params`

## arrange

- `arrange.bringForward` — Bring Forward (Page Layout > Arrange)
  - params: `{kind: chart|image|shape, id, toFront?: bool}`
- `arrange.sendBackward` — Send Backward (Page Layout > Arrange)
  - params: `{kind: chart|image|shape, id, toBack?: bool}`
- `arrange.selectionPane` — Selection Pane (Page Layout > Arrange)
  - params: `{} → objects on the sheet in stacking order`
- `arrange.align` — Align (Page Layout > Arrange)
  - params: `{kind: chart|image|shape, ids: [..], align: left|center|right|top|middle|bottom}`
- `arrange.group` — Group (Page Layout > Arrange)
  - params: `{kind, ids} (moves objects together: aligns their anchors to the first)`
- `arrange.rotate` — Rotate (Page Layout > Arrange)
  - params: `{kind: shape, id, flip?: horizontal|vertical} (swaps width/height for 90° turns)`

## automate

- `automate.recordActions` — Record Actions (Automate > Scripting Tools)
  - params: `{stop?: bool, name?: script name when stopping}`
- `automate.newScript` — New Script (Automate > Scripting Tools)
  - params: `{name, commands: [{command, params}] }`
- `automate.allScripts` — All Scripts (Automate > Scripting Tools)
  - params: `{} → saved scripts`
- `automate.runScript` — Run Script
  - params: `{name}`
- `automate.deleteScript` — Delete Script
  - params: `{name}`

## draw

- `draw.pen` — Pen (Draw > Tools)
  - params: `{on?: bool, color?: hex, width?: 2}`
- `draw.eraser` — Eraser (Draw > Tools)
  - params: `{on?: bool}`
- `draw.lasso` — Lasso Select (Draw > Tools)
  - params: `{} (selects ink by dragging; same as Select Objects)`
- `draw.stroke` — Ink Stroke
  - params: `{points: [[x,y],…] in sheet points, color?: hex, width?: 2}`
- `draw.inkToShape` — Ink to Shape (Draw > Convert)
  - params: `{id?} converts an ink stroke (default: the last) into a rectangle, ellipse, triangle or line`

## pivot

- `pivot.calculatedField` — Calculated Field (PivotTable Analyze > Calculations)
  - params: `{pivot?, name, formula?: "=Sales*0.1" (fields bare or 'quoted'; evaluated on each cell's sums), delete?: bool, values?: bool (add a new field to Values, default true)} adds, changes or deletes a calculated field; without `name` opens the dialog → {name, formula, calculatedFields}`
- `pivot.fields` — PivotTable Fields
  - params: `{pivot?} → source fields (name, numeric, date, samples, areas) and the current layout`
- `pivot.fieldList` — Field List (PivotTable Analyze > Show)
  - params: `{pivot?} (same as pivot.fields)`
- `pivot.list` — PivotTables
  - params: `{} → every PivotTable in the workbook`
- `pivot.addField` — Add Field
  - params: `{pivot?, field, area: rows|columns|values|filters, func?: sum|count|average|max|min|product|countNumbers|stdDev|stdDevP|var|varP, name?, position?: index, replace?}`
- `pivot.removeField` — Remove Field
  - params: `{pivot?, field (or value caption), area?: rows|columns|values|filters, replace?}`
- `pivot.moveField` — Move Field
  - params: `{pivot?, field ("Σ Values" moves the value fields between rows and columns; in columns it stays after the last field), from: rows|columns|values|filters, to: rows|columns|values|filters, position?: index, replace?}`
- `pivot.valueSettings` — Value Field Settings (PivotTable Analyze > Active Field)
  - params: `{pivot?, field: caption or source field | index: n, func?, name?, showAs?: normal|percentOfGrandTotal|percentOfColumnTotal|percentOfRowTotal|runningTotal|rank, numberFormat?: "#,##0" | null, replace?}`
- `pivot.filter` — Filter Items
  - params: `{pivot?, field, selected: ["East", ..] | null (all), replace?}`
- `pivot.sort` — Sort Field
  - params: `{pivot?, field, order: asc|desc|none, replace?}`
- `pivot.group` — Group Field (PivotTable Analyze > Group)
  - params: `{pivot?, field, by: years|quarters|months|days|none, replace?}`
- `pivot.collapse` — Expand/Collapse Field (PivotTable Analyze > Active Field)
  - params: `{pivot?, field, items?: [labels] (default: all), collapse?: true, replace?}`
- `pivot.layout` — PivotTable Layout (PivotTable Design > Layout)
  - params: `{pivot?, layout?: compact|outline|tabular, grandTotalsRows?: bool, grandTotalsCols?: bool, subtotals?: bool|top|bottom|none, style?: "PivotStyleLight16", showHeaders?: bool, replace?}`
- `pivot.grandTotals` — Grand Totals (PivotTable Design > Layout)
  - params: `{pivot?, mode?: off|on|rows|columns, rows?: bool, cols?: bool}`
- `pivot.subtotals` — Subtotals (PivotTable Design > Layout)
  - params: `{pivot?, mode: none|top|bottom}`
- `pivot.reportLayout` — Report Layout (PivotTable Design > Layout)
  - params: `{pivot?, layout: compact|outline|tabular}`
- `pivot.style` — PivotTable Styles (PivotTable Design > PivotTable Styles)
  - params: `{pivot?, style: "PivotStyleMedium9"}`
- `pivot.refresh` — Refresh (PivotTable Analyze > Data) [Alt+F5]
  - params: `{pivot?, replace?}`
- `pivot.changeSource` — Change Data Source (PivotTable Analyze > Data)
  - params: `{pivot?, source: "Sheet1!$A$1:$E$300" | table name, replace?} (fields missing from the new source are removed)`
- `pivot.delete` — Delete PivotTable (PivotTable Analyze > Actions)
  - params: `{pivot?} clears the report and removes the PivotTable`

## slicer

- `slicer.toggle` — Toggle Slicer Value
  - params: `{slicer?: id, value: "East", multi?: false}`
- `slicer.selectAll` — Clear Slicer Filter
  - params: `{slicer?: id}`
- `slicer.clear` — Clear Slicer Filter
  - params: `{slicer?: id}`
- `slicer.delete` — Delete Slicer
  - params: `{slicer?: id}`

