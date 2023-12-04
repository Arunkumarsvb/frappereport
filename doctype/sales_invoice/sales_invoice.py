# Copyright (c) 2023, sales and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class SalesInvoice(Document):
    #pass
    document = frappe.get_all('Sales Invoice', filters={"Billing_Address":"sethiathope"})
    #print(document.date)
    #print(document.Billing_Address)
    #  # Fetch all sales invoices
    # sales_invoices = frappe.get_doc("Sales Invoice", filters={"docstatus": 1})
    # #print(sales_invoices)

    # # Print the header
    # print("{:<20} {:<15} {:<15}".format("Invoice Number", "Posting Date", "Total Amount"))
    # print("="*50)

    # Print the details of each sales invoice
    for invoice in document:
        invoice_number = invoice.get("invoice")
        posting_date = invoice.get("dates")
        total_amount = invoice.get("total_amounts")
        print("testsdf")

    #     print("{:<20} {:<15} {:<15}".format(invoice_number, posting_date, total_amount))

