# to test this code, run and search http://127.0.0.1:5001/fill-rfq

from flask import Flask, request, send_file
from fillpdf import fillpdfs
import tempfile

app = Flask(__name__)

@app.route('/fill-rfq', methods=['GET', 'POST'])
def fill_rfq():
    if request.method == 'GET':
        return '''
            <h1>RFQ Form Submission</h1>
            <form method="POST" action="/fill-rfq">
                <p>MIMOS Contact Person's Name: <input type="text" name="pic_name"></p>
                <p>Department: <input type="text" name="department"></p>
                <p>Email Address: <input type="email" name="email"></p>
                <p>Contact No.: <input type="text" name="contact"></p>
                <p>RFQ Reference Number: <input type="text" name="rfq_ref_number"></p>
                <p>RFQ Issue Date: <input type="date" name="rfq_issue_date"></p>
                <p>RFQ Closing Date & Time: <input type="date" name="rfq_closing_date"></p>
                <p>RFQ Date Received by MIMOS (optional): <input type="date" name="date_received"></p>
                <p>Category:
                    <select name="rfq_category">
                        <option value="general">IT REQUISITION</option>
                        <option value="FACILITY REQUISITION">Book</option>
                        <option value="it"> GENERAL REQUISITON</option>
                        <option value="other">BOOK</option>
                    </select>
                </p>
                <p><input type="submit" value="Generate PDF"></p>
            </form>
        '''
    
    # POST method handling (your existing code)
    try:
        data = request.json if request.is_json else request.form
        print("📥 Received data:", data)

        checkbox_fields = {
            'rfq_category1': None,  # Or 'No_rtdh' if PDF requires it
            'rfq_category2': None,
            'rfq_category3': None,
            'rfq_category4': None,
        }

        category = data.get('rfq_category', '').lower()
        if 'general' in category:
            checkbox_fields['rfq_category1'] = 'Yes_rtdh'
        elif 'book' in category:
            checkbox_fields['rfq_category2'] = 'Yes_jwwu'
        elif 'it' in category:
            checkbox_fields['rfq_category3'] = 'Yes_gtes'
        elif 'other' in category:
            checkbox_fields['rfq_category4'] = 'Yes_okkm'

        pdf_fields = {
            'pic_name': data.get('pic_name', ''),
            'department': data.get('department', ''),
            'email': data.get('email', ''),
            'contact': data.get('contact', ''),
            'rfq_ref_number': data.get('rfq_ref_number', ''),
            'rfq_issue_date': data.get('rfq_issue_date', ''),
            'rfq_closing_date': data.get('rfq_closing_date', ''),
            'date_received': data.get('date_received', ''),
            **checkbox_fields
        }

        print("📝 PDF fields to write:", pdf_fields)

        output_path = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name
        fillpdfs.write_fillable_pdf(
            input_pdf_path="RFQ_template.pdf",
            output_pdf_path=output_path,
            data_dict=pdf_fields
        )

        return send_file(output_path, as_attachment=True, download_name="filled_rfq.pdf")

    except Exception as e:
        print("🔥 ERROR:", e)
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)