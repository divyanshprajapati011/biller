

import streamlit as st
from fpdf import FPDF
from datetime import date
import os

# ---- COMPANY DETAILS ----
COMPANY_NAME = "Prajapati Electronics & Furniture Showroom"
SLOGAN = "Style Your Space, Power Your Life!"
ADDRESS = "Main Road, Sukheda, District Ratlam (M.P.)"
PHONE = "+91 9977524020"
EMAIL = "prajapatifurnitures@gmail.com"
WEBSITE = ""

# ---- PDF CLASS ----
class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.set_text_color(220, 50, 50)
        self.cell(0, 10, COMPANY_NAME, ln=True, align="L")

        self.set_font("Helvetica", "", 10)
        self.set_text_color(0, 0, 0)
        self.cell(0, 6, SLOGAN, ln=True, align="L")
        self.cell(0, 6, ADDRESS, ln=True, align="L")
        self.cell(0, 6, f"Phone: {PHONE} | Email: {EMAIL}", ln=True, align="L")
        if WEBSITE:
            self.cell(0, 6, WEBSITE, ln=True, align="L")
        self.ln(10)

    def invoice_body(self, cust_name, cust_addr, cust_phone, invoice_no, invoice_date, items, warranty_details=None):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 10, "INVOICE", ln=True, align="R")
        self.set_font("Helvetica", "", 10)
        self.cell(100, 6, f"Invoice No: {invoice_no}", align="L")
        self.cell(0, 6, f"Date: {invoice_date}", ln=True, align="R")
        self.ln(5)

        # Customer info
        self.cell(0, 6, f"Customer Name: {cust_name}", ln=True)
        self.cell(0, 6, f"Address: {cust_addr}", ln=True)
        self.cell(0, 6, f"Phone: {cust_phone}", ln=True)
        self.ln(5)

        # Table Header
        self.set_font("Helvetica", "B", 10)
        self.cell(10, 8, "No", 1, 0, "C")
        self.cell(80, 8, "Description", 1, 0, "C")
        self.cell(25, 8, "Qty", 1, 0, "C")
        self.cell(35, 8, "Rate", 1, 0, "C")
        self.cell(40, 8, "Amount", 1, 1, "C")

        # Table Rows
        self.set_font("Helvetica", "", 10)
        total = 0
        for i, item in enumerate(items, 1):
            desc = item["desc"] or ""
            qty = item["qty"] or 0
            rate = item["rate"] or 0
            amount = qty * rate
            total += amount

            self.cell(10, 8, str(i), 1, 0, "C")
            self.cell(80, 8, desc, 1, 0)
            self.cell(25, 8, str(qty), 1, 0, "C")
            self.cell(35, 8, f"{rate:.2f}", 1, 0, "R")
            self.cell(40, 8, f"{amount:.2f}", 1, 1, "R")

        # Total
        self.set_font("Helvetica", "B", 10)
        self.cell(150, 8, "Total", 1, 0, "R")
        self.cell(40, 8, f"{total:.2f}", 1, 1, "R")

        # Warranty section
        if warranty_details:
            self.ln(10)
            self.set_font("Helvetica", "B", 11)
            self.cell(0, 8, "Warranty Details:", ln=True)
            self.set_font("Helvetica", "", 10)
            self.multi_cell(0, 6, warranty_details)
            self.ln(5)

        # Footer
        self.ln(5)
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, f"Rupees in words: {num2words(int(total))} only.")
        self.ln(10)
        self.cell(0, 6, "Signature: ___________________", ln=True, align="R")

# ---- Helper: Convert number to words ----
def num2words(num):
    import inflect
    p = inflect.engine()
    return p.number_to_words(num).capitalize()

# ---- Helper: Generate Next Invoice Number ----
def get_next_invoice_number():
    counter_file = "invoice_counter.txt"
    if not os.path.exists(counter_file):
        with open(counter_file, "w") as f:
            f.write("1")
        return "001"

    with open(counter_file, "r") as f:
        current = int(f.read().strip())

    next_num = current + 1
    with open(counter_file, "w") as f:
        f.write(str(next_num))

    return f"{next_num:03d}"  # format as 001, 002, etc.

# ---- STREAMLIT UI ----
st.set_page_config(page_title="Invoice Generator", layout="centered")
st.markdown("## 🧾 Prajapati Invoice Generator")
st.markdown("---")

invoice_no = get_next_invoice_number()

with st.form("invoice_form"):
    col1, col2 = st.columns(2)
    with col1:
        cust_name = st.text_input("Customer Name")
        cust_addr = st.text_area("Address")
    with col2:
        cust_phone = st.text_input("Phone Number")
        st.text_input("Invoice No", value=invoice_no, disabled=True)
        invoice_date = st.date_input("Invoice Date", value=date.today())

    st.markdown("### Add Items")
    num_items = st.number_input("Number of items", 1, 20, 3)
    items = []
    for i in range(num_items):
        st.markdown(f"**Item {i+1}**")
        col1, col2, col3 = st.columns([3, 1, 1])
        desc = col1.text_input(f"Description {i+1}", placeholder="Enter item name or detail")
        qty = col2.number_input(f"Qty {i+1}", min_value=1, value=1, step=1)
        rate = col3.number_input(f"Rate {i+1}", min_value=0.0, step=0.01, format="%.2f", value=0.0)
        items.append({"desc": desc, "qty": qty, "rate": rate})

    st.markdown("### Warranty Section")
    warranty_available = st.checkbox("Product has warranty?")
    warranty_details = None
    if warranty_available:
        warranty_period = st.text_input("Warranty Period", placeholder="e.g. 1 year")
        warranty_terms = st.text_area("Warranty Details", placeholder="Enter warranty terms, start date, etc.")
        warranty_details = f"Warranty Period: {warranty_period}\n{warranty_terms}"

    submit = st.form_submit_button("Generate Invoice PDF")

# ---- Generate PDF ----
if submit:
    pdf = PDF()
    pdf.add_page()
    pdf.invoice_body(cust_name, cust_addr, cust_phone, invoice_no, invoice_date, items, warranty_details)

    save_folder = r"D:\invoice"
    os.makedirs(save_folder, exist_ok=True)
    file_path = os.path.join(save_folder, f"Inv_{invoice_no}_{cust_name}.pdf")
    pdf.output(file_path)

    with open(file_path, "rb") as f:
        st.download_button("📥 Download PDF", f, file_name=f"Inv_{invoice_no}_{cust_name}.pdf")

    st.success(f"✅ Invoice {invoice_no} generated successfully!")
                           
