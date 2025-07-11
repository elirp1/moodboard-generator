def create_pdf(moodboard_path, palettes, filename="moodboard.pdf"):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(filename, pagesize=letter)
    c.drawImage(moodboard_path, 50, 400, width=500, height=300)

    y = 350
    for palette in palettes:
        for color in palette:
            c.setFillColorRGB(color[0]/255, color[1]/255, color[2]/255)
            c.rect(50, y, 100, 30, fill=1)
            c.drawString(160, y + 10, str(color))
            y -= 40

    c.save()
