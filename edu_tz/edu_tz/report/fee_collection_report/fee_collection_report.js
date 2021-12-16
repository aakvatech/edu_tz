frappe.query_reports["Fee Collection Report"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"fieldtype": "Date",
			"label": __("From Date"),
			"reqd": 1
		},
		{
			"fieldname": "to_date",
			"fieldtype": "Date",
			"label": __("To Date"),
			"reqd": 1
		},
		{
			"fieldname": "academic_year",
			"fieldtype": "Data",
			"label": __("Academic Year"),
			"reqd": 1
		},
		{
			"fieldname": "company",
			"fieldtype": "Link",
			"label": __("Company"),
			"options": "Company",
			"reqd": 1
		},
		{
			"fieldname": "program",
			"fieldtype": "Link",
			"label": __("Program"),
			"options": "Program",
			"reqd": 0
		},
		{
			"fieldname": "summary_based_on_program",
			"fieldtype": "Check",
			"label": __("Summary Based on Program"),
			"reqd": 0
		},
	]
};