import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from textwrap import wrap


class CVGenerator:
    def __init__(self, json_data, output_filename="cv.pdf"):
        self.data = json_data
        self.output_filename = output_filename
        self.c = canvas.Canvas(output_filename, pagesize=letter)
        self.width, self.height = letter
        self.margin = 50
        self.bottom_padding = 50
        self.line_height = 15
        self.y_position = self.height - 120  # Added extra padding
        self.max_width = self.width - 2 * self.margin

    def check_new_page(self, lines_needed):
        if self.y_position - (lines_needed * self.line_height) < self.bottom_padding:
            self.c.showPage()
            self.y_position = self.height - 50
            self.c.setFont("Helvetica", 10)  # Reset font after new page

    def draw_header(self):
        header_color = (0, 0.3, 0.6)
        self.c.setFillColorRGB(*header_color)
        self.c.rect(0, self.height - 120, self.width, 120, fill=True, stroke=False)
        self.c.setFillColor(colors.white)
        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(self.margin, self.height - 80, self.data.get("name", "Unknown"))
        self.c.setFont("Helvetica", 14)
        self.c.drawString(self.margin, self.height - 100, self.data.get("title", "No Title"))
        self.c.setFillColor(colors.black)
        self.y_position -= 50  # Adjusting position after header

    def add_contact_info(self):
        """Adds contact information below the header with icons."""
        self.y_position -= 10
        contact_info = self.data.get("contact", {})
        contact_icons = {
            "email": "assets/email_icon.png",
            "location": "assets/location_icon.png",
            "phone": "assets/phone_icon.png",
            "linkedin": "assets/linkedin_icon.png",
            "github": "assets/github_icon.png",
        }

        self.c.setFont("Helvetica", 12)
        icon_size = 12
        x_offset = self.margin + icon_size + 5  # Space for icons

        for key, icon_path in contact_icons.items():
            value = contact_info.get(key, "")
            if value:
                if icon_path:
                    self.c.drawImage(icon_path, self.margin, self.y_position - 4, icon_size, icon_size, mask='auto')
                self.c.drawString(x_offset, self.y_position, value)
                self.y_position -= self.line_height

        self.y_position -= 10  # Extra spacing

    def add_section(self, title, content, font_size=10, bullet=False):
        self.check_new_page(2)
        self.c.setFont("Helvetica-Bold", 14)
        self.c.drawString(self.margin, self.y_position, title)
        self.y_position -= 20
        self.c.setFont("Helvetica", font_size)

        if isinstance(content, list):
            for item in content:
                if isinstance(item, dict):
                    role_text = f"{item.get('position', '')}, {item.get('company', '')} ({item.get('duration', '')})"
                    wrapped_role = wrap(role_text, width=90)
                    self.check_new_page(len(wrapped_role) + 1)
                    self.c.setFont("Helvetica-Bold", 13)
                    for line in wrapped_role:
                        self.c.drawString(self.margin + 10, self.y_position, line)
                        self.y_position -= self.line_height
                    self.c.setFont("Helvetica", font_size)
                    for resp in item.get("responsibilities", []):
                        wrapped_resp = wrap(f"- {resp}", width=90)
                        self.check_new_page(len(wrapped_resp))
                        for line in wrapped_resp:
                            self.c.drawString(self.margin + 20, self.y_position, line)
                            self.y_position -= self.line_height
                    self.y_position -= 10
                else:
                    wrapped_text = wrap(str(item), width=90)
                    self.check_new_page(len(wrapped_text))
                    for line in wrapped_text:
                        self.c.drawString(self.margin + 10, self.y_position, f"• {line}" if bullet else line)
                        self.y_position -= self.line_height
        else:
            wrapped_text = wrap(str(content), width=90)
            self.check_new_page(len(wrapped_text))
            for line in wrapped_text:
                self.c.drawString(self.margin + 10, self.y_position, line)
                self.y_position -= self.line_height
        self.y_position -= 10

    def generate_pdf(self):
        self.draw_header()
        self.add_contact_info()
        sections = [
            ("Summary", self.data.get("summary", "")),
            ("Work Experience", self.data.get("work_experience", [])),
            ("Education", self.data.get("education", {}).get('degree', "") + ", " +
             self.data.get("education", {}).get('university', "") +
             " (" + self.data.get("education", {}).get('duration', "") + ")")
        ]
        for title, content in sections:
            self.add_section(title, content, bullet=isinstance(content, list))
        self.c.save()
        print(f"CV saved as {self.output_filename}")


if __name__ == "__main__":
    with open("data.json", "r") as file:
        data = json.load(file)
    cv_generator = CVGenerator(data)
    cv_generator.generate_pdf()