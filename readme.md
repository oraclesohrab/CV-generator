# CV Generator 📄

This is a **Python-based CV Generator** that creates a **PDF resume** using data from a JSON file. The script utilizes `reportlab` to format and structure the CV with a professional layout.

## 🚀 Features
- **Dynamic CV Generation**: Automatically generates a structured CV from `data.json`.
- **Customizable Layout**: Includes sections for summary, work experience, education, and contact details.
- **Auto Page Breaks**: Ensures content is properly formatted across multiple pages.
- **Supports Icons**: Displays icons for contact information.
- **Formatted Work Experience**: Highlights job roles, companies, and responsibilities clearly.

## 📦 Requirements
Before running the script, ensure you have the required dependencies installed:

```sh
pip install reportlab
```

## 🔧 Usage
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/oraclesohrab/CV-generator.git
   cd CV-generator
   ```

2. **Prepare Your Data**:
   - Modify `data.json` to include your personal details, work experience, and skills.

3. **Run the Script**:
   ```sh
   python main.py
   ```

4. **Generated PDF**:
   - Your CV will be saved as `cv.pdf` in the project directory.

## 📂 File Structure
```
CV-generator/
│-- main.py           # CV Generator Script
│-- data.json         # JSON data for the CV
│-- assets/           # Icons for contact information
│-- cv.pdf            # Output file (generated CV)
│-- README.md         # Project Documentation
```

## ✨ Example `data.json`
```json
{
  "name": "John Doe",
  "title": "Senior Python Developer",
  "contact": {
    "email": "johndoe@example.com",
    "location": "New York, USA",
    "phone": "+1 234 567 890",
    "linkedin": "https://linkedin.com/in/johndoe"
  },
  "summary": "Experienced Python Developer with expertise in backend development...",
  "work_experience": [
    {
      "position": "Software Engineer",
      "company": "TechCorp",
      "duration": "2020 - Present",
      "responsibilities": [
        "Developed scalable REST APIs using Django.",
        "Implemented CI/CD pipelines to automate deployment."
      ]
    }
  ],
  "education": {
    "degree": "BSc in Computer Science",
    "university": "MIT",
    "duration": "2015 - 2019"
  }
}
```

## 🛠 Customization
- Modify `main.py` to adjust **fonts, layout, or design**.
- Update `data.json` with **new fields** to personalize your CV.

## 📝 License
This project is open-source under the **MIT License**.

## 🤝 Contributing
Feel free to submit **issues** or **pull requests** to improve the project!

---
🔹 **Created by [@oraclesohrab](https://github.com/oraclesohrab)**