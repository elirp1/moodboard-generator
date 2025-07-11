def create_pdf(moodboard_path, palettes, filename="moodboard.pdf"):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    page_width, page_height = letter
    c = canvas.Canvas(filename, pagesize=letter)

    c.drawImage(moodboard_path, 50, page_height - 350, width=500, height=300)

    y = page_height - 400
    box_height = 30
    box_width = 100
    spacing = 10

    for palette in palettes:
        for color in palette:
            if y < 50:  # Start a new page if space runs out
                c.showPage()
                c.drawImage(moodboard_path, 50, page_height - 350, width=500, height=300)
                y = page_height - 400

            c.setFillColorRGB(color[0]/255, color[1]/255, color[2]/255)
            c.rect(50, y, box_width, box_height, fill=1)
            c.setFillColorRGB(0, 0, 0)
            c.drawString(160, y + 10, str(color))
            y -= box_height + spacing

    c.save()
