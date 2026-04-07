from organizer import FileOrganizer
from scraper import scrape
from monitor import check_system

organizer = FileOrganizer("test_folder", "organized")

print("Running once...\n")

organizer.organize()
scrape()
check_system()