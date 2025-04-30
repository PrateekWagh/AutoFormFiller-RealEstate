🏡 AutoFormFiller-RealEstate

A Python automation script that scrapes apartment listings from a dummy real estate site and auto-fills a Google Form using Selenium. The submitted data is stored directly in a linked Google Sheet—simulating a real-world lead generation and data entry pipeline.

📌 Features

- Scrapes apartment **price**, **address**, and **URL**
- Auto-fills a **Google Form** using Selenium
- Form responses are stored in a **Google Sheet**
- Fully automated — no manual data entry needed
- Clean, modular code structure

🛠️ Tech Stack

- Python 
- requests module  
- beautifulsoup4  
- selenium
- Google Forms + Google Sheets (linked)


🚀 How It Works

1. Scrape apartment listings from the dummy site.
2. Extract relevant fields (price, address, link).
3. Launch Selenium to open the Google Form.
4. Automatically fill and submit the form for each entry.
5. Google Sheets auto-updates with each response.


📂 Project Structure
AutoFormFiller-RealEstate

/
│
└── main.py

📌 Note
1. This project uses a dummy site to simulate real estate listings.

2. Built for educational/demo purposes—not meant for scraping live platforms like Zillow or others.

🙌 Contributions

Feel free to fork, suggest improvements, or create pull requests!
