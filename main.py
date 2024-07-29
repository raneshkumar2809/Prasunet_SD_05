import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

def scrape_data():
    url = url_entry.get()
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'lxml')

    # Adjust the class names based on the actual HTML structure
    product_listings = soup.find_all('div', class_='tUxRFH')  # Assuming this is the class for product listings

    product_data = []

    for product in product_listings:
        try:
            name_div = product.find('div', class_='KzDlHZ')  # Adjust class name
            name = name_div.text.strip() if name_div else 'N/A'

            price_div = product.find('div', class_='Nx9bqj _4b5DiR')  # Adjust class name
            price = price_div.text.strip() if price_div else 'N/A'

            rating_div = product.find('div', class_='XQDdHH')  # Adjust class name
            rating = rating_div.text.strip() if rating_div else 'N/A'

            product_data.append({
                "name": name,
                "price": price,
                "rating": rating
            })
        except Exception as e:
            print(f"Error processing product: {e}")

    display_results(product_data)

def display_results(product_data):
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    for product in product_data:
        result_text.insert(tk.END, f"Name: {product['name']}\n")
        result_text.insert(tk.END, f"Price: {product['price']}\n")
        result_text.insert(tk.END, f"Rating: {product['rating']}\n")
        result_text.insert(tk.END, "-"*40 + "\n")
    result_text.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Flipkart Scraper")
root.geometry("600x500")
root.configure(bg='#f0f0f0')

# Create and place the URL entry widget
url_label = tk.Label(root, text="Enter Flipkart URL:", font=('Helvetica', 12, 'bold'), bg='#f0f0f0')
url_label.pack(pady=10)

url_entry = ttk.Entry(root, width=60)
url_entry.pack(pady=5)

# Create and place the scrape button
scrape_button = ttk.Button(root, text="Scrape Data", command=scrape_data)
scrape_button.pack(pady=10)

# Create and place the results text area
result_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD, font=('Helvetica', 10))
result_text.pack(pady=10)
result_text.config(state=tk.DISABLED)

# Add a style
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=5)
style.configure('TEntry', padding=5)
style.map('TButton', foreground=[('pressed', 'blue'), ('active', 'black')], background=[('pressed', '!disabled', 'yellow'), ('active', 'white')])

# Start the GUI event loop
root.mainloop()
