import os
from pypdf import PdfReader
from datetime import datetime


FORMATS = ["%Y-%m-%d", "%m/%d/%Y", "%b %d, %Y", "%m/%d/%y"]

def clean_date(raw):
    for fmt in FORMATS:
        try:
            return datetime.strptime(raw, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return None

seen = set()
duplicates = []
clean = []

for filename in os.listdir("invoices"):
    if filename.endswith(".pdf"):
        invoice = {}
        path = "invoices/" + filename
        text = PdfReader(path).pages[0].extract_text()
        clean_text = text.splitlines()
        if not text.strip():
            print(f"{filename} has no text layer, needs OCR")
            continue
        print(filename, repr(text))
        for line in clean_text:
            if line.startswith("Vendor:"):
                vendor = line.replace("Vendor:", "").strip().title()
                invoice["vendor"] = vendor
            elif line.startswith("Total:"):
                total = float(line.replace("Total:", "").replace("$", "").replace(",", "").strip())
                invoice["total"] = total
            elif line.startswith("Invoice Number:"):
                invoice_number = line.replace("Invoice Number:", "").strip()
                if invoice_number in seen:
                    duplicates.append(invoice_number)
                else:
                    seen.add(invoice_number)
                invoice["invoice number"] = invoice_number
            elif line.startswith("Date:"):
                raw_date = line.replace("Date:", "").strip()
                invoice["date"] = clean_date(raw_date)
        if invoice["invoice number"] not in duplicates:
            clean.append(invoice)

import sqlite3

conn = sqlite3.connect("invoices.db")
conn.execute("""CREATE TABLE IF NOT EXISTS invoices (
    number TEXT PRIMARY KEY, date TEXT, vendor TEXT, total REAL)""") 
for inv in clean:
    conn.execute(
        "INSERT OR IGNORE INTO invoices VALUES (?, ?, ?, ?)",
        (inv["invoice number"], inv["date"], inv["vendor"], inv["total"])
    )
conn.commit()

print(conn.execute("SELECT COUNT(*), SUM(total) FROM invoices").fetchone())