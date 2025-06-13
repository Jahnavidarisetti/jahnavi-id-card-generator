import csv
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from PIL import Image

# Configuration constants
CARD_DIMENSIONS = {'width': 3.375 * inch, 'height': 2.125 * inch}
IMAGE_DPI_SIZE = (300, 300)  # 300 DPI for 1x1 inch


class EmployeeDataProcessor:
    @staticmethod
    def load_csv_data(file_path):
        """Load employee data from CSV file"""
        employees = []
        try:
            with open(file_path, newline='') as csv_file:
                data_reader = csv.DictReader(csv_file)
                print("Available columns:", data_reader.fieldnames)
                employees = list(data_reader)
        except Exception as error:
            print(f"Failed to read CSV: {error}")
        return employees


class ImageProcessor:
    @staticmethod
    def process_employee_photo(source_path, output_filename):
        """Resize and save employee photo"""
        try:
            photo = Image.open(source_path)
            resized_photo = photo.resize(IMAGE_DPI_SIZE, Image.LANCZOS)
            resized_photo.save(output_filename)
            return output_filename
        except Exception as error:
            print(f"Photo processing failed for {source_path}: {error}")
            return None


class IDCardRenderer:
    def __init__(self, canvas_obj):
        self.canvas = canvas_obj
    
    def render_single_card(self, background_image, employee_info, photo_location, card_index):
        """Render a single ID card on the canvas"""
        employee_name = employee_info['name'].strip()

        # Render background template
        self.canvas.drawImage(background_image, 0, 0, 
                             width=CARD_DIMENSIONS['width'], height=CARD_DIMENSIONS['height'])

        # Handle photo rendering
        if os.path.exists(photo_location):
            temp_filename = f"temp_photo_{card_index}_{employee_name.replace(' ', '_')}.png"
            processed_photo = ImageProcessor.process_employee_photo(photo_location, temp_filename)
            if processed_photo:
                self.canvas.drawImage(processed_photo, 1.9 * inch, 
                                    0.73 * inch,
                                    width=1.1 * inch, height=1.1 * inch)
                os.remove(temp_filename)
        else:
            print(f"Photo missing: {photo_location}")

        # Render text elements
        self._render_text_elements(employee_name)
        self.canvas.showPage()
    
    def _render_text_elements(self, name):
        """Render name text on the card"""
        self.canvas.setFont("Helvetica-Bold", 12)
        self.canvas.drawString(0.25 * inch, 0.22 * inch, name)


class IDCardGenerator:
    def __init__(self, template_image, employee_csv, photos_directory, output_file):
        self.template_path = template_image
        self.csv_file_path = employee_csv
        self.photo_directory = photos_directory
        self.output_pdf_path = output_file
    
    def generate_cards(self):
        """Main method to generate all ID cards"""
        pdf_canvas = canvas.Canvas(self.output_pdf_path, pagesize=(CARD_DIMENSIONS['width'], CARD_DIMENSIONS['height']))
        card_renderer = IDCardRenderer(pdf_canvas)
        employee_list = EmployeeDataProcessor.load_csv_data(self.csv_file_path)

        for idx, employee_record in enumerate(employee_list):
            if not self._validate_employee_data(employee_record):
                print(f"Skipping invalid record: {employee_record}")
                continue

            photo_full_path = os.path.join(self.photo_directory, employee_record['photo_location'].strip())
            print(f"Generating card for {employee_record['name']} using photo {photo_full_path}")
            card_renderer.render_single_card(self.template_path, employee_record, photo_full_path, idx)

        pdf_canvas.save()
        print(f"ID cards generated successfully: {self.output_pdf_path}")
    
    def _validate_employee_data(self, record):
        """Validate that employee record has required fields"""
        required_fields = ['name', 'photo_location']
        return all(field in record and record[field].strip() for field in required_fields)


def main():
    """Entry point for the application"""
    generator = IDCardGenerator(
        template_image="ute_id_template.png",
        employee_csv="employeesDetails.csv",
        photos_directory="profilephotoes",
        output_file="id_cards.pdf"
    )
    generator.generate_cards()


if __name__ == "__main__":
    main()