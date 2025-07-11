def extract_palette(image_path, color_count=6):
    from colorthief import ColorThief
    color_thief = ColorThief(image_path)
    return color_thief.get_palette(color_count=color_count)
