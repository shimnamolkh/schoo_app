# Copyright (c) 2022, shimna and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus
from dateutil import relativedelta
from datetime import datetime
class studentregistration(Document):
	def before_save(self):
      		  self.full_name = f'{self.first__name} {self.last_name or ""}'

	@frappe.whitelist()
	def get_age(self):
		if(self.dob):
			today = datetime.now()
			dob = datetime.strptime(self.dob, '%Y-%m-%d')
			t = relativedelta.relativedelta(today, dob)
			return t.years



	