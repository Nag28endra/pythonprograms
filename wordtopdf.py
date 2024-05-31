import os
import win32com.client as win32

def convert_word_to_pdf(input_file, output_file):
    # Create an instance of the Word application
    word_app = win32.gencache.EnsureDispatch('Word.Application')
    
    try:
        # Open the Word document
        doc = word_app.Documents.Open(input_file)
        
        # Save the document as PDF
        doc.SaveAs(output_file, FileFormat=17)  # 17 represents the PDF file format
        
        # Close the document
        doc.Close()
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        # Quit Word application
        word_app.Quit()

# Specify the input Word document and output PDF file paths
input_file_path = r'C:\Users\NAGENDRA\OneDrive\Desktop\operation 4-2\unit-I ob.docx'
output_file_path = r'C:\Users\NAGENDRA\OneDrive\Desktop\operation 4-2\unit-1.pdf'

# Convert Word to PDF
convert_word_to_pdf(input_file_path, output_file_path)
