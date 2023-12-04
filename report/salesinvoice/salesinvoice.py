# Copyright (c) 2023, sales and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns=[
        {
        "fieldname": "totalamount",
        "lable":"totalamount",
        "fieldtype":"Data",
        "width":150
        },
        {
        "fieldname": "invoicedate",
        "lable":"invoicedate",
        "fieldtype":"Date",
        "width":150
        }
        ,
        {
        "fieldname": "invoicenumber",
        "lable":"invoicenumber",
        "fieldtype":"Data",
        "width":150
        }
    ]
    main_doc_data = frappe.get_all("Sales Invoice", filters={}, fields=['*'])
    sales = []
    for item in main_doc_data:
        child_table_data = frappe.get_all("Invoice Items", filters={"parent": main_doc_data[0].name}, fields=['*'])
        for childitem in child_table_data:
            row_data = {"invoicedate": item.invoice_date,"totalamount": childitem.total_amount,"invoicenumber":childitem.invoice_number }
            sales.append(row_data)
    return columns, sales
