import frappe


def execute():
    frappe.db.set_value("DocType", "Student Applicant", "is_submittable", 1)
