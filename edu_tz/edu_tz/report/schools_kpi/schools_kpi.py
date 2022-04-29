# Copyright (c) 2013, Aakvatech and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.utils import cint, cstr


def execute(filters):
    columns = [
        {"fieldname": "class_name", "label": _("Class Name"), "fieldtype": "Data"},
        {
            "fieldname": "class_avilable",
            "label": _("No. of Classes Available"),
            "fieldtype": "Int",
        },
        {
            "fieldname": "class_in_use",
            "label": _("No. of Classes in Use"),
            "fieldtype": "Int",
        },
        {
            "fieldname": "rate",
            "label": _("Classroom Utilization Rate"),
            "fieldtype": "Data",
        },
        {
            "fieldname": "class_capacity",
            "label": _("Classes Capacity"),
            "fieldtype": "Int",
        },
        {
            "fieldname": "no_of_students",
            "label": _("No. of Students per Class"),
            "fieldtype": "Int",
        },
        {"fieldname": "vacancies", "label": _("No. of Vacancies"), "fieldtype": "Data"},
    ]

    data = []
    enrollment_details = frappe.get_all(
        "Program Enrollment",
        filters={
            "docstatus": 1,
            "academic_year": filters.academic_year,
            "company": filters.company,
        },
        fields=["program", "count(student) as no_of_students"],
        group_by="program",
    )

    room_details = frappe.db.sql(
        """
		SELECT p.name AS program, SUM(r.seating_capacity) AS total_students,
            COUNT(r.room_name) AS total_rooms, 
            COUNT(r.seating_capacity) AS no_of_room_used
		FROM `tabRoom` r
		INNER JOIN `tabProgram` p ON r.edu_tz_program = p.name
		WHERE p.company = %(company)s
		GROUP BY p.name
	""", filters, as_dict=1)
    
    for enroll in enrollment_details:
        for room in room_details:
            if enroll.program == room.program:
                d = enroll.no_of_students - room["total_students"]
                if d > 0:
                    vacancies = "+" + cstr(d)
                else:
                    vacancies = d

                data.append(
                    {
                        "class_name": enroll.program,
                        "class_avilable": room["total_rooms"],
                        "class_in_use": room["no_of_room_used"],
                        "rate": cstr(
                            (room["no_of_room_used"] / room["total_rooms"]) * 100
                        )
                        + "%",
                        "class_capacity": room["total_students"],
                        "no_of_students": enroll.no_of_students,
                        "vacancies": vacancies,
                    }
                )

    return columns, data
