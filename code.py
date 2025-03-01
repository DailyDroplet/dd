
import qrcode
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib import colors


story1 = " 'The Most Disgraceful Foreign Policy Spectacle in US History' - Vance and Trump slammed after they team up to shout down Zelenskyy in the oval office in bizarre spectacle"
url1 = "https://www.thenation.com/article/politics/disgraceful-foreign-policy-spectacle-in-us-history/"

story2 = "ICE signs $900 million contract for immigrant detention facility in New Jersey" 

url2 = "https://newjerseymonitor.com/2025/02/27/ice-plans-massive-new-immigrant-detention-center-in-newark/"
story3 = "Instagram 'Error' Turned Reels Into Neverending Scroll of Murder, Gore, and Violence"
url3 = "https://www.404media.co/instagram-error-turned-reels-into-neverending-scroll-of-murder-gore-and-violence/"

story_details = [(story1,url1), (story2,url2), (story3,url3)]
current_date = datetime.now()
tomorrow = current_date + timedelta(days=1)  
tomorrow_str = tomorrow.strftime("%A, %B %d, %Y")
file_name = tomorrow_str+".pdf"

qr_urls = [url for _, url in story_details]




# Create a function to generate the PDF
def create_pdf(tomorrow_str , qr_urls, story_details):
    file_name = tomorrow_str+".pdf"
    # Create a canvas object
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 26)
    c.drawString(100, height - 30, "The Daily Droplet")
    c.setFont("Helvetica-Bold", 18)
    c.drawString(150, height - 50, tomorrow_str )
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    normal_style.fontSize = 22 # Set font size to a larger value
    qr_code_width = 100  # Define QR code width
    normal_style.leading = 30 # Adjust leading (space between lines)
    y_position = height - 150
    for text, url in story_details:
        # Create a Paragraph object for the detail text to handle wrapping
        paragraph = Paragraph(f"• {text}", normal_style)
        paragraph_width = width - 250  # set the width of the text box
        paragraph_height = paragraph.wrap(paragraph_width, 100)[1]  # calculate height based on text width
        paragraph.drawOn(c, 100, y_position - paragraph_height)
        qr = qrcode.make(url)
        qr_path = text[0:15]+".png"
        qr.save(qr_path)
        c.drawImage(qr_path, width - 150, y_position - paragraph_height - 20, width=100, height=100)
        y_position -= paragraph_height + 120  # increase space for the next detail
    c.save()


create_pdf(tomorrow_str,  qr_urls, story_details)



