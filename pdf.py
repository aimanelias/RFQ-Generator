#refer based on https://www.youtube.com/watch?v=TcBX2kb6g3o

from fillpdf import fillpdfs

form_fields = list(fillpdfs.get_form_fields('RFQ_template.pdf').keys())

print(form_fields)

pic_name = 'Test Name'
department = 'Test Department'
email = 'test@example.com'
contact = '0123456789'
rfq_ref_number = 'RFQ-999'
rfq_issue_date = '2025-04-24'
rfq_closing_date = '2025-05-01'
date_received = 'NA'
rfq_category1 = 'Yes_rtdh'
rfq_category2 = None #'Yes_jwwu'
rfq_category3 = None #'Yes_gtes'
rfq_category4 = None #'Yes_okkm' 

data_dict = {
    form_fields[0]: pic_name,
    form_fields[1]: department,
    form_fields[2]: email,
    form_fields[3]: contact,
    form_fields[4]: rfq_ref_number,
    form_fields[5]: rfq_issue_date,
    form_fields[6]: rfq_closing_date,
    form_fields[7]: date_received,
    form_fields[8]: rfq_category1,
    form_fields[9]: rfq_category2,
    form_fields[10]: rfq_category3,
    form_fields[11]: rfq_category4,
}

# Corrected function call - using = instead of :
fillpdfs.write_fillable_pdf(
    input_pdf_path='RFQ_template.pdf',
    output_pdf_path='manual_test_pdf.pdf',
    data_dict=data_dict
)

#to make it uneditable, make it flat
fillpdfs.flatten_pdf(input_pdf_path="manual_test.pdf", output_pdf_path = "flatten_manual_test.pdf")