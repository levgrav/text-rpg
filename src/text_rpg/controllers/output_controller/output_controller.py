import processing.functions as pfun
import controllers.command_center.command_center as cc
from PySimpleGUI import Window

SW = 1920
font_size = 20
aspect_ratio = 0.8
font_width = font_size * aspect_ratio
num_chars = SW/font_width - 2
print(num_chars)

def output_all(world, msg):
    cc.set_output_text(break_text_into_lines(msg, num_chars))


def break_text_into_lines(text: str, line_length: int):
    paragraphs = text.split("\n")  # Split the text into individual paragraphs
    for i, paragraph in enumerate(paragraphs):
        words = paragraph.split()  # Split the paragraph into individual words
        lines = []
        current_line = ""
        
        for word in words:
            if len(current_line + " " + word) <= line_length:  # If adding the word to the current line doesn't exceed the line length
                if current_line:
                    current_line += " "
                current_line += word
            else:
                lines.append(current_line)  # Add the completed line to the list of lines
                current_line = word  # Start a new line with the current word
        
        if current_line:
            lines.append(current_line)  # Add the last line if there is any remaining text
        
        paragraphs[i] = "\n".join(lines)  # Join the lines with newline characters
    return "\n".join(paragraphs) # Join the paragraphs with newline characters
