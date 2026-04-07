import tkinter as tk
from organizer import FileOrganizer
from scraper import scrape
from monitor import check_system

organizer = FileOrganizer("test_folder", "organized")

# CREATE WINDOW
root = tk.Tk()
root.title("Python Automation Suite")
root.geometry("400x400")

tk.Label(root, text="Automation Suite", font=("Arial", 14)).pack(pady=10)

# 👉 CREATE OUTPUT BOX FIRST (IMPORTANT)
output_box = tk.Text(root, height=10, width=40)
output_box.pack(pady=10)

# 👉 NOW FUNCTIONS CAN USE output_box
def run_organizer():
    output_box.delete(1.0, tk.END)
    organizer.organize()
    output_box.insert(tk.END, "Files Organized Successfully\n")

def run_scraper():
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "Scraping website...\n")
    scrape()

def run_monitor():
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, "Checking system...\n")
    check_system()

# BUTTONS
tk.Button(root, text="Run Organizer", command=run_organizer).pack(pady=5)
tk.Button(root, text="Run Scraper", command=run_scraper).pack(pady=5)
tk.Button(root, text="Check System", command=run_monitor).pack(pady=5)

root.mainloop()