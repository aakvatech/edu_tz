import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    new_custom_fields = {'Room': [
            dict(fieldname='edu_tz_column_break', label='', fieldtype='Column Break',
                insert_after='seating_capacity', read_only=1, bold=1),
            dict(fieldname='edu_tz_program', label='Program', fieldtype='Link',
                options='Program', insert_after='edu_tz_column_break', reqd=1, bold=1)
        ]
    }
    create_custom_fields(new_custom_fields, update=True)

