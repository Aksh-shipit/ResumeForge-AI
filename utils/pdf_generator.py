from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable
)

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.pdfbase.pdfmetrics import stringWidth

import os


def create_resume_pdf(data, filename):

    os.makedirs("generated/resumes", exist_ok=True)

    pdf_path = os.path.join(
        "generated",
        "resumes",
        filename
    )

    doc = SimpleDocTemplate(
        pdf_path,
        rightMargin=35,
        leftMargin=35,
        topMargin=35,
        bottomMargin=35
    )

    styles = getSampleStyleSheet()

    # ------------------------
    # Colors based on template
    # ------------------------

    template = data.get("template", "classic")

    if template == "modern":
        accent = HexColor("#1565C0")

    elif template == "dark":
        accent = HexColor("#37474F")

    else:
        accent = HexColor("#000000")

    # ------------------------
    # Styles
    # ------------------------

    title = ParagraphStyle(
        "Title",
        parent=styles["Title"],
        fontSize=24,
        leading=28,
        alignment=TA_CENTER,
        textColor=accent,
        spaceAfter=8
    )

    contact = ParagraphStyle(
        "Contact",
        parent=styles["BodyText"],
        alignment=TA_CENTER,
        fontSize=10,
        spaceAfter=5
    )

    heading = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=accent,
        spaceBefore=12,
        spaceAfter=6
    )

    normal = ParagraphStyle(
        "Normal",
        parent=styles["BodyText"],
        fontSize=10,
        leading=16
    )

    story = []

    # ======================
    # Header
    # ======================

    story.append(Paragraph(data["name"], title))

    contact_line = " | ".join(filter(None, [
        data["email"],
        data["phone"],
        data["address"]
    ]))

    story.append(
        Paragraph(contact_line, contact)
    )

    links = " | ".join(filter(None, [
        data["linkedin"],
        data["github"]
    ]))

    if links:
        story.append(
            Paragraph(links, contact)
        )

    story.append(
        HRFlowable(
            width="100%",
            thickness=1,
            color=accent,
            spaceBefore=8,
            spaceAfter=12
        )
    )

    # ======================
    # Summary
    # ======================

    if data["summary"]:

        story.append(
            Paragraph(
                "Professional Summary",
                heading
            )
        )

        story.append(
            Paragraph(
                data["summary"],
                normal
            )
        )

    # ======================
    # Education
    # ======================

    if data["education"]:

        story.append(
            Paragraph(
                "Education",
                heading
            )
        )

        for edu in data["education"]:

            story.append(
                Paragraph(
                    f"• {edu}",
                    normal
                )
            )

    # ======================
    # Skills
    # ======================

    if data["skills"]:

        story.append(
            Paragraph(
                "Skills",
                heading
            )
        )

        story.append(
            Paragraph(
                " • ".join(data["skills"]),
                normal
            )
        )

    # ======================
    # Experience
    # ======================

    if data["experience"]:

        story.append(
            Paragraph(
                "Experience",
                heading
            )
        )

        for exp in data["experience"]:

            story.append(
                Paragraph(
                    f"• {exp}",
                    normal
                )
            )

    # ======================
    # Projects
    # ======================

    if data["projects"]:

        story.append(
            Paragraph(
                "Projects",
                heading
            )
        )

        for project in data["projects"]:

            story.append(
                Paragraph(
                    f"• {project}",
                    normal
                )
            )

    doc.build(story)

    return pdf_path