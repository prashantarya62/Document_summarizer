import pandas as pd

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def create_csv(results, path):

    df = pd.DataFrame(results)

    df.to_csv(path, index=False)


def create_pdf(results, path):

    doc = SimpleDocTemplate(path)

    styles = getSampleStyleSheet()

    elements = []

    for item in results:

        elements.append(
            Paragraph(
                f"<b>{item['file_name']}</b>",
                styles['Heading2']
            )
        )

        elements.append(
            Paragraph(
                item['summary'],
                styles['BodyText']
            )
        )

        elements.append(Spacer(1, 12))

    doc.build(elements)