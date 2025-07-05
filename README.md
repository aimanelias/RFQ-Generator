# RFQ-Vendor Management System

A Flask-based web application for managing Request for Quotation (RFQ) forms and vendor information for MIMOS BERHAD. This system allows users to fill out RFQ forms dynamically and manage vendor data.

## 🎯 Project Overview

This application provides a digital solution for creating and managing RFQ (Request for Quotation) documents. It includes:

- **Dynamic PDF Form Filling**: Web interface to fill RFQ forms with automatic PDF generation
- **Vendor Management**: Database of vendors with their specializations and contact information
- **Template Management**: Uses predefined RFQ templates for consistent document generation
- **Form Validation**: Ensures all required fields are properly filled

## 📁 Project Structure

```
RFQ-Vendor/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── test_fill.py          # PDF filling test script
├── vendor.csv            # Vendor database
├── vendorList.csv        # Additional vendor data
├── RFQ_template.pdf      # RFQ form template
├── RFQ_blank.pdf         # Blank RFQ form
├── RFQ_blank.docx        # Blank RFQ document
├── RFQ.html              # HTML version of RFQ form
├── template.json         # Form field templates
└── Various test PDFs     # Generated test documents
```

## 🚀 Features

### Core Functionality
- **Web-based RFQ Form**: Interactive form for entering RFQ details
- **PDF Generation**: Automatically generates filled PDF forms
- **Form Flattening**: Option to make generated PDFs non-editable
- **Vendor Database**: CSV-based vendor management system
- **Category Selection**: Support for different RFQ categories (IT, Facility, General, Book)

### Form Fields
- MIMOS Contact Person's Name
- Department
- Email Address
- Contact Number
- RFQ Reference Number
- RFQ Issue Date
- RFQ Closing Date & Time
- Date Received by MIMOS
- RFQ Category (with checkbox selection)

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd RFQ-Vendor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your web browser
   - Navigate to `http://127.0.0.1:5001/fill-rfq`

## 📖 Usage

### Web Interface
1. Open the application in your browser
2. Fill out the RFQ form with the required information:
   - **MIMOS Contact Person's Name**: Primary contact for the RFQ
   - **Department**: Department requesting the quotation
   - **Email Address**: Contact email
   - **Contact No.**: Phone number
   - **RFQ Reference Number**: Unique identifier for the RFQ
   - **RFQ Issue Date**: When the RFQ was issued
   - **RFQ Closing Date & Time**: Deadline for submissions
   - **Date Received by MIMOS**: Optional field for tracking
   - **Category**: Select the appropriate RFQ category

3. Click "Generate PDF" to create the filled RFQ document
4. The PDF will be automatically downloaded

### Programmatic Usage
You can also use the PDF filling functionality programmatically:

```python
from fillpdf import fillpdfs

fields = {
    'pic_name': 'John Doe',
    'department': 'IT Department',
    'email': 'john.doe@mimos.my',
    'contact': '0123456789',
    'rfq_ref_number': 'RFQ-2024-001',
    'rfq_issue_date': '2024-01-15',
    'rfq_closing_date': '2024-01-30',
    'date_received': '2024-01-16',
    'rfq_category1': 'Yes_rtdh',  # IT REQUISITION
    'rfq_category2': 'None',
    'rfq_category3': 'None',
    'rfq_category4': 'None'
}

fillpdfs.write_fillable_pdf(
    input_pdf_path="RFQ_template.pdf",
    output_pdf_path="filled_rfq.pdf",
    data_dict=fields
)
```

### Testing
Run the test script to verify PDF filling functionality:
```bash
python test_fill.py
```

## 📋 Dependencies

### Core Dependencies
- **Flask** (3.1.0): Web framework
- **fillpdf** (0.7.3): PDF form filling library
- **PyMuPDF** (1.25.5): PDF manipulation
- **pdf2image** (1.17.0): PDF to image conversion
- **Pillow** (11.2.1): Image processing

### Development Dependencies
- **gunicorn**: Production WSGI server
- **Werkzeug**: WSGI utilities

## 🔧 Configuration

### RFQ Categories
The application supports four RFQ categories:
- **IT REQUISITION**: Technology-related requests
- **FACILITY REQUISITION**: Facility and infrastructure requests
- **GENERAL REQUISITON**: General procurement requests
- **BOOK**: Book and publication requests

### Vendor Database
The `vendor.csv` file contains vendor information including:
- Vendor Name
- Specialization
- Past Projects
- Website Link
- Contact Information
- Location

## 🚀 Deployment

### Development
```bash
python app.py
```

### Production
```bash
gunicorn -w 4 -b 0.0.0.0:5001 app:app
```

## 📝 API Endpoints

### GET `/fill-rfq`
- Returns the RFQ form HTML interface

### POST `/fill-rfq`
- Accepts form data (JSON or form-encoded)
- Returns a filled PDF file for download

## 🔍 Troubleshooting

### Common Issues

1. **PDF Generation Fails**
   - Ensure `RFQ_template.pdf` exists in the project directory
   - Check that all required fields are provided

2. **Dependencies Installation Issues**
   - Use a virtual environment: `python -m venv venv`
   - Activate the environment: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate` (Windows)

3. **Port Already in Use**
   - Change the port in `app.py`: `app.run(host='0.0.0.0', port=5002, debug=True)`

## 📄 License

This project is developed for MIMOS BERHAD internal use.

## 👥 Contributing

For internal development:
1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📞 Support

For technical support or questions, please contact the development team at MIMOS BERHAD.

---

**Version**: 1.0.0  
**Last Updated**: January 2024  
**Maintained by**: MIMOS BERHAD Development Team 
