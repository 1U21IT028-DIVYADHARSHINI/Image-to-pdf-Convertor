# Find more python Projects at CodeWithCurious.com
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os
# function to convert images to PDF
def images_to_pdf(images, pdf_name):
    try:
        # create a new pdf file
        pdf = Image.open(images[0])
        pdf.save(pdf_name, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:])
        messagebox.showinfo("Success", "Images have been successfully converted to PDF.")
    except Exception as e:
        messagebox.showerror("Error", "Failed to convert images to PDF.\nError: " + str(e))
# function to select images
def select_images():
    images = filedialog.askopenfilenames(title="Select Images", filetypes=(("Image files", "*.jpg;*.jpeg;*.png"),("All files", "*.*")), initialdir = "C:/")
    return images
# function to select pdf name and path
def select_pdf():
    pdf = filedialog.asksaveasfilename(title="Save PDF As", defaultextension=".pdf", initialdir = "C:/", filetypes=(("PDF files", "*.pdf"),("All files", "*.*")))
    return pdf
# create GUI
root = tk.Tk()
root.title("Convert Images to PDF")

# Increase the overall size of the main window
root.geometry("400x300")

# Function to apply a common style to the buttons
def apply_button_style(button):
    button.configure(
        font=('Helvetica', 14),  # Increase the font size
        foreground='white',
        background='#3498db',
        padx=15,  # Increase the padding on the x-axis
        pady=8,   # Increase the padding on the y-axis
        activebackground='#2980b9'
    )

# Create buttons with the styled configuration
select_images_btn = tk.Button(root, text="Select Images", command=select_images)
apply_button_style(select_images_btn)

select_pdf_btn = tk.Button(root, text="Select PDF", command=select_pdf)
apply_button_style(select_pdf_btn)

convert_btn = tk.Button(root, text="Convert", command=lambda: images_to_pdf(select_images(), select_pdf()))
apply_button_style(convert_btn)

# Pack the buttons into the main window
select_images_btn.pack(pady=15)  # Increase the vertical padding
select_pdf_btn.pack(pady=15)     # Increase the vertical padding
convert_btn.pack(pady=15)        # Increase the vertical padding

# Start the Tkinter event loop
root.mainloop()