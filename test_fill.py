from fillpdf import fillpdfs

fields = {
    'pic_name': 'Test Name',
    'department': 'Test Department',
    'email': 'test@example.com',
    'contact': '0123456789',
    'rfq_ref_number': 'RFQ-999',
    'rfq_issue_date': '2025-04-24',
    'rfq_closing_date': '2025-05-01',
    'date_received': 'NA',
    'rfq_category1': 'Yes_rtdh',
    'rfq_category2': 'None',
    'rfq_category3': 'None',
    'rfq_category4': 'None'
}

fillpdfs.write_fillable_pdf(
    input_pdf_path="RFQ_template.pdf",
    output_pdf_path="manual_test_fill.pdf",
    data_dict=fields
)

#to make it uneditable, make it flat
fillpdfs.flatten_pdf(input_pdf_path="manual_test_fill.pdf", output_pdf_path = "flatten_manual_test.pdf")