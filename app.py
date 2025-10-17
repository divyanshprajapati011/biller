# import streamlit as st
# from fpdf import FPDF
# from datetime import date

# # ---- COMPANY DETAILS (Predefined) ----
# COMPANY_NAME = "Prajapati Electronics & Furniture Showroom "
# SLOGAN = "Style Your Space, Power Your Life!"
# ADDRESS = "Main Road, Sukheda, District Ratlam (M.P.)"
# PHONE = "+91 9977524020"
# EMAIL = "prajapatifurnitures@gmail.com"
# WEBSITE = ""

# # ---- PDF GENERATION ----
# class PDF(FPDF):
#     def header(self):
#         self.set_font("Helvetica", "B", 16)
#         self.set_text_color(220, 50, 50)
#         self.cell(0, 10, COMPANY_NAME, ln=True, align="L")
#         self.set_font("Helvetica", "", 10)
#         self.set_text_color(0, 0, 0)
#         self.cell(0, 6, SLOGAN, ln=True, align="L")
#         self.cell(0, 6, ADDRESS, ln=True, align="L")
#         self.cell(0, 6, f"Phone: {PHONE} | Email: {EMAIL}", ln=True, align="L")
#         self.cell(0, 6, WEBSITE, ln=True, align="L")
#         self.ln(10)

#     def invoice_body(self, cust_name, cust_addr, cust_phone, invoice_no, invoice_date, items):
#         self.set_font("Helvetica", "B", 12)
#         self.cell(0, 10, "INVOICE", ln=True, align="R")
#         self.set_font("Helvetica", "", 10)
#         self.cell(100, 6, f"Invoice No: {invoice_no}", align="L")
#         self.cell(0, 6, f"Date: {invoice_date}", ln=True, align="R")
#         self.ln(5)
#         self.cell(0, 6, f"Customer Name: {cust_name}", ln=True)
#         self.cell(0, 6, f"Address: {cust_addr}", ln=True)
#         self.cell(0, 6, f"Phone: {cust_phone}", ln=True)
#         self.ln(5)

#         # Table Header
#         self.set_font("Helvetica", "B", 10)
#         self.cell(10, 8, "No", 1, 0, "C")
#         self.cell(80, 8, "Description", 1, 0, "C")
#         self.cell(25, 8, "Qty", 1, 0, "C")
#         self.cell(35, 8, "Rate", 1, 0, "C")
#         self.cell(40, 8, "Amount", 1, 1, "C")

#         # Table Rows
#         self.set_font("Helvetica", "", 10)
#         total = 0
#         for i, item in enumerate(items, 1):
#             amount = item["qty"] * item["rate"]
#             total += amount
#             self.cell(10, 8, str(i), 1, 0, "C")
#             self.cell(80, 8, item["desc"], 1, 0)
#             self.cell(25, 8, str(item["qty"]), 1, 0, "C")
#             self.cell(35, 8, f"{item['rate']:.2f}", 1, 0, "R")
#             self.cell(40, 8, f"{amount:.2f}", 1, 1, "R")

#         self.set_font("Helvetica", "B", 10)
#         self.cell(150, 8, "Total", 1, 0, "R")
#         self.cell(40, 8, f"{total:.2f}", 1, 1, "R")

#         self.ln(10)
#         self.set_font("Helvetica", "", 10)
#         self.cell(0, 6, f"Rupees in words: {num2words(int(total))} only.", ln=True)
#         self.ln(10)
#         self.cell(0, 6, "Signature: ___________________", ln=True, align="R")

# def num2words(num):
#     # simple helper for words
#     import inflect
#     p = inflect.engine()
#     return p.number_to_words(num).capitalize()

# # ---- STREAMLIT UI ----
# st.set_page_config(page_title="Invoice Generator", layout="centered")

# st.markdown("## 🧾 Prajapati Invoice Generator")
# st.markdown("---")

# with st.form("invoice_form"):
#     col1, col2 = st.columns(2)
#     with col1:
#         cust_name = st.text_input("Customer Name")
#         cust_addr = st.text_area("Address")
#     with col2:
#         cust_phone = st.text_input("Phone Number")
#         invoice_no = st.text_input("Invoice No", value="001")
#         invoice_date = st.date_input("Invoice Date", value=date.today())

#     st.markdown("### Add Items")
#     num_items = st.number_input("Number of items", 1, 20, 3)
#     items = []
#     for i in range(num_items):
#         st.markdown(f"**Item {i+1}**")
#         col1, col2, col3 = st.columns([3,1,1])
#         desc = col1.text_input(f"Description {i+1}")
#         qty = col2.number_input(f"Qty {i+1}", min_value=1, value=1)
#         rate = col3.number_input(f"Rate {i+1}", min_value=0.0, value=0)
#         items.append({"desc": desc, "qty": qty, "rate": rate})

#     submit = st.form_submit_button("Generate Invoice PDF")

# if submit:
#     pdf = PDF()
#     pdf.add_page()
#     pdf.invoice_body(cust_name, cust_addr, cust_phone, invoice_no, invoice_date, items)
#     file_path = f"invoice_{invoice_no}.pdf"
#     pdf.output(file_path)

#     with open(file_path, "rb") as f:
#         st.download_button("📥 Download PDF", f, file_name=file_path)
#     st.success("✅ Invoice generated successfully!")





# # import streamlit as st
# # from reportlab.lib import colors
# # from reportlab.lib.pagesizes import A4
# # from reportlab.lib.units import mm
# # from reportlab.pdfgen import canvas
# # from reportlab.platypus import Table, TableStyle
# # from datetime import date
# # import io

# # # ===== COMPANY DETAILS =====
# # COMPANY_NAME = "Prajapati Electronics & Furniture Showroom (Sukheda)"
# # SLOGAN = "Style Your Space, Power Your Life!"
# # ADDRESS = "Main Road, Sukheda, District Ratlam (M.P.)"
# # PHONE = "+91 98765 43210"
# # EMAIL = "prajapatifurnitures@gmail.com"

# # # ===== STREAMLIT PAGE CONFIG =====
# # st.set_page_config(page_title="Invoice Generator", layout="centered")
# # st.markdown("## 🧾 Prajapati Invoice Generator")
# # st.divider()

# # # ===== FORM INPUT =====
# # with st.form("invoice_form"):
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         cust_name = st.text_input("Customer Name")
# #         cust_addr = st.text_area("Customer Address")
# #     with col2:
# #         cust_phone = st.text_input("Customer Phone Number")
# #         invoice_no = st.text_input("Invoice No", "001")
# #         invoice_date = st.date_input("Invoice Date", value=date.today())

# #     st.markdown("### 🛒 Add Items")
# #     num_items = st.number_input("Number of items", 1, 20, 3)

# #     items = []
# #     for i in range(num_items):
# #         st.markdown(f"**Item {i+1}**")
# #         col1, col2, col3 = st.columns([3, 1, 1])
# #         desc = col1.text_input(f"Description {i+1}")
# #         qty = col2.number_input(f"Qty {i+1}", min_value=1, value=1)
# #         rate = col3.number_input(f"Rate {i+1}", min_value=0.0, value=None)
# #         items.append({"desc": desc, "qty": qty, "rate": rate})

# #     submit = st.form_submit_button("Generate PDF Invoice")

# # # ===== HELPER FUNCTION =====
# # def create_invoice_pdf(buffer, cust_name, cust_addr, cust_phone, invoice_no, invoice_date, items):
# #     c = canvas.Canvas(buffer, pagesize=A4)
# #     width, height = A4

# #     # ---- Header Bar ----
# #     c.setFillColorRGB(0.85, 0.1, 0.1)  # red
# #     c.rect(0, height - 25, width, 25, fill=1)
# #     c.setFillColorRGB(0.1, 0.6, 0.8)   # blue bar
# #     c.rect(0, height - 28, width / 3, 3, fill=1)

# #     # ---- Company Name ----
# #     c.setFillColor(colors.red)
# #     c.setFont("Helvetica-Bold", 14)
# #     c.drawString(25, height - 40, COMPANY_NAME)

# #     c.setFillColor(colors.black)
# #     c.setFont("Helvetica", 10)
# #     c.drawString(25, height - 55, SLOGAN)
# #     c.drawString(25, height - 70, ADDRESS)
# #     c.drawString(25, height - 85, f"Phone: {PHONE}  |  Email: {EMAIL}")

# #     # ---- Invoice Label ----
# #     c.setFont("Helvetica-Bold", 12)
# #     c.setFillColor(colors.red)
# #     c.drawRightString(width - 25, height - 40, "INVOICE")

# #     # ---- Invoice Details ----
# #     c.setFont("Helvetica", 10)
# #     c.setFillColor(colors.black)
# #     c.drawRightString(width - 25, height - 55, f"Invoice No: {invoice_no}")
# #     c.drawRightString(width - 25, height - 70, f"Date: {invoice_date}")

# #     # ---- Customer Info ----
# #     y = height - 110
# #     c.setFont("Helvetica", 10)
# #     c.drawString(25, y, f"Name: {cust_name}")
# #     c.drawString(25, y - 15, f"Address: {cust_addr}")
# #     c.drawString(25, y - 30, f"Phone: {cust_phone}")

# #     # ---- Table ----
# #     data = [["Sl.No", "Description", "Qty", "Rate", "Amount"]]
# #     total = 0
# #     for i, item in enumerate(items, 1):
# #         amount = item["qty"] * item["rate"]
# #         total += amount
# #         data.append([
# #             str(i),
# #             item["desc"],
# #             str(item["qty"]),
# #             f"{item['rate']:.2f}",
# #             f"{amount:.2f}"
# #         ])

# #     data.append(["", "", "", "Total", f"{total:.2f}"])

# #     table = Table(data, colWidths=[25, 220, 50, 70, 80])
# #     style = TableStyle([
# #         ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
# #         ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
# #         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
# #         ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
# #         ('ALIGN', (2, 1), (-1, -1), 'CENTER'),
# #         ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
# #     ])
# #     table.setStyle(style)

# #     table.wrapOn(c, width, height)
# #     table.drawOn(c, 25, y - 160)

# #     # ---- Footer ----
# #     c.setFont("Helvetica", 10)
# #     c.drawString(25, 70, f"Rupees in words: {int(total)} only.")
# #     c.drawString(25, 50, "Terms & Conditions:")
# #     c.drawString(40, 35, "• Goods once sold will not be returned.")
# #     c.drawString(40, 22, "• Warranty as per manufacturer policy.")

# #     c.drawRightString(width - 50, 40, "Signature")

# #     # ---- Bottom Bar ----
# #     c.setFillColorRGB(0.1, 0.6, 0.8)  # blue
# #     c.rect(0, 0, width / 3, 8, fill=1)
# #     c.setFillColorRGB(0.85, 0.1, 0.1)  # red
# #     c.rect(width / 3, 0, width, 8, fill=1)

# #     c.showPage()
# #     c.save()

# # # ===== PDF GENERATION =====
# # if submit:
# #     pdf_buffer = io.BytesIO()
# #     create_invoice_pdf(pdf_buffer, cust_name, cust_addr, cust_phone, invoice_no, invoice_date, items)
# #     pdf_buffer.seek(0)

# #     st.success("✅ Invoice generated successfully!")
# #     st.download_button(
# #         label="📥 Download Invoice PDF",
# #         data=pdf_buffer,
# #         file_name=f"invoice_{invoice_no}.pdf",
# #         mime="application/pdf"
# #     )



import streamlit as st
from fpdf import FPDF
from datetime import date

# ---- COMPANY DETAILS (Predefined) ----
COMPANY_NAME = "Prajapati Electronics & Furniture Showroom "
SLOGAN = "Style Your Space, Power Your Life!"
ADDRESS = "Main Road, Sukheda, District Ratlam (M.P.)"
PHONE = "+91 9977524020"
EMAIL = "prajapatifurnitures@gmail.com"
WEBSITE = ""

# ---- PDF GENERATION ----
class PDF(FPDF):
    def header(self):
        # Company details
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

    def invoice_body(self, cust_name, cust_addr, cust_phone, invoice_no, invoice_date, items):
        # Invoice heading
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

        # Footer details
        self.ln(10)
        self.set_font("Helvetica", "", 10)
        self.multi_cell(0, 6, f"Rupees in words: {num2words(int(total))} only.")
        self.ln(10)
        self.cell(0, 6, "Signature: ___________________", ln=True, align="R")

# ---- Number to Words Helper ----
def num2words(num):
    import inflect
    p = inflect.engine()
    return p.number_to_words(num).capitalize()

# ---- STREAMLIT UI ----
st.set_page_config(page_title="Invoice Generator", layout="centered")

st.markdown("## 🧾 Prajapati Invoice Generator")
st.markdown("---")

with st.form("invoice_form"):
    col1, col2 = st.columns(2)
    with col1:
        cust_name = st.text_input("Customer Name")
        cust_addr = st.text_area("Address")
    with col2:
        cust_phone = st.text_input("Phone Number")
        invoice_no = st.text_input("Invoice No", value="001")
        invoice_date = st.date_input("Invoice Date", value=date.today())

    st.markdown("### Add Items")
    num_items = st.number_input("Number of items", 1, 20, 3)
    items = []
    for i in range(num_items):
        st.markdown(f"**Item {i+1}**")
        col1, col2, col3 = st.columns([3, 1, 1])
        desc = col1.text_input(f"Description {i+1}", placeholder="Enter item name or detail")
        qty = col2.number_input(f"Qty {i+1}", min_value=1, value=1, step=1, placeholder="Qty")
        rate = col3.number_input(f"Rate {i+1}", min_value=0.0, step=0.01, format="%.2f", value=0.0)
        items.append({"desc": desc, "qty": qty, "rate": rate})

    submit = st.form_submit_button("Generate Invoice PDF")

# ---- Generate PDF ----
if submit:
    pdf = PDF()
    pdf.add_page()
    pdf.invoice_body(cust_name, cust_addr, cust_phone, invoice_no, invoice_date, items)
    file_path = fr"D:\invoice\Inv_{cust_name}.pdf"
    pdf.output(file_path)

    with open(file_path, "rb") as f:
        st.download_button("📥 Download PDF", f, file_name=file_path)
    st.success("✅ Invoice generated successfully!")
