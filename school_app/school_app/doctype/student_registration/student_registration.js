// Copyright (c) 2022, shimna and contributors
// For license information, please see license.txt

frappe.ui.form.on('student registration', {

	refresh: function(frm) {
		if(frm.is_new()){

			frm.set_intro('Now start a new student registration')
		}
		if(!frm.is_new()){
			
			frm.set_intro('Complete the registration')
		}
	},
	
			//frm.set_intro('Complete the registration')
	
	dob: function (frm) {
		frappe.call({
		  doc:frm.doc,
		  method:'get_age', 
		  callback:function(r){
			let doc = frm.doc
			doc.age = r.message
			frm.refresh_field('age')
		  }
		})
	}

});
