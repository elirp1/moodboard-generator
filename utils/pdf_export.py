def create_pdf(moodboard_path, moodboard_size, palettes, filename="moodboard.pdf"):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    page_width, page_height = letter
    c = canvas.Canvas(filename, pagesize=letter)

    def add_moodboard():
        moodboard_width, moodboard_height = moodboard_size
        aspect_ratio = moodboard_width / moodboard_height
        max_width = page_width - 100
        max_height = 300

        if moodboard_width > moodboard_height:
            draw_width = max_width
            draw_height = max_width / aspect_ratio
        else:
            draw_height = max_height
            draw_width = max_height * aspect_ratio

        x = (page_width - draw_width) / 2
        y = page_height - draw_height - 50

        c.drawImage(moodboard_path, x, y, width=draw_width, height=draw_height)

    add_moodboard()

    y = page_height - 400
    box_height = 30
    box_width = 100
    spacing = 10

    for palette in palettes:
        for color in palette:
            if y < 50:
                c.showPage()
                add_moodboard()
                y = page_height - 400

            c.setFillColorRGB(color[0]/255, color[1]/255, color[2]/255)
            c.rect(50, y, box_width, box_height, fill=1)
            c.setFillColorRGB(0, 0, 0)
            c.drawString(160, y + 10, str(color))
            y -= box_height + spacing

    c.save()
