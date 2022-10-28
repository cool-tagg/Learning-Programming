from extractors.extract_themes import get_themes_allPage, get_themes_onePage
import os

def save_to_file():
    themes = get_themes_allPage()

    file = open("Themes List.csv", "w")
    file.write("page, order, name, link\n")
    for theme in themes:
        file.write(f"{theme['page']},{theme['order']}, {theme['name']}, {theme['link']}\n")
    file.close()



