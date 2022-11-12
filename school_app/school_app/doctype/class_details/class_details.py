# Copyright (c) 2022, shimna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class Classdetails(Document):
	def validate(self):
		exists = frappe.db.exists(
			"Class Details",
			{
				# "class teacher":self.class_teacher,
				# "docstatus":DocStatus.saved(),
				"maximum number of students":("<",self.number_of_students)

			},
			
		)
		if exists:
			frappe.throw("faculty already assists with maximum number of students")
	
maximum number of students = frappe.db.get_single_value("Faculty","maximum_number_of_students")