# Employee ID Generator

This project creates a single PDF file with employee ID cards, one per page, based on a predefined ID template image, a CSV file containing employee information, and a folder of employee photos. Each ID card follows standard dimensions (3.375 x 2.125 inches), displaying the employee's name in the bottom-left corner and their photo in the top-left corner.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)

## Features
- Produces a PDF containing one employee ID card per page.
- Utilizes a template image (`ute_id_template.png`) for uniform ID design.
- Retrieves employee information (name, title, photo path) from a CSV file.
- Displays employee photos, names, and titles on each ID card.
- Positions the name at the bottom-left with a 10-point font size.
- Places the title at (1.7 inches x, 0.6 inches from bottom) using an 8-point font.
- Positions the photo at (0.37 inches x, 0.33 inches from top) with a 1x1 inch dimension.

## Requirements
- **Python**: Version 3.8 or later
- **Libraries**:
  - `reportlab`: For PDF generation
  - `pillow`: For handling image processing
- **Input Files**:
  - `ute_id_template.png`: ID template image (1013x638 pixels for 3.375x2.125 inches at 300 DPI)
  - `employeesDetails.csv`: CSV file with columns `name`, `photo_location`
  - Employee photos in `src/profilephotoes/` (e.g., `photo1.jpg`, `photo2.jpg`)

Install dependencies via:
```bash
pip install -r requirements.txt
```

## Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/employee_id_generator.git
   cd employee_id_generator
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare Input Files**
   - Place `ute_id_template.png` in `src/`.
   - Place employee photos (e.g., `photo1.jpg`, `photo2.jpg`) in `src/profilePhotos/`.
   - Create or update `src/employeesDetails.csv` with the following format:
   ```csv
   name,photo_location
   Rock,photo1.jpg
   Hrithik,photo2.jpg
   Anushka,photo3.jpg
   Sitara,photo4.jpg
   ```

## Usage
1. **Navigate to the `src/` directory:**
    ```bash
    cd src
    ```

2. **Run the script:**
    ```bash
    python main.py
    ```

3. **Check the output:**
    - A file named `id_cards.pdf` will be generated in `src/`.
    - Each page contains one ID card with the template, employee photo, name, and title.


