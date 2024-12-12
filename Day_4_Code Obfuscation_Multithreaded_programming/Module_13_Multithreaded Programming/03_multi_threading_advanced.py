# Advanced Multithreading Example: Real-Time Stock Price Monitoring System
# Problem Statement:
# Build a multithreaded Python application that simulates real-time stock price monitoring.
# - A producer thread generates random stock prices for multiple companies.
# - Consumer threads process and log these prices to different files (one per company).
# - A summary thread periodically computes and displays the average price for each company.

import threading
import time
import random
from queue import Queue

# Global dictionary to hold stock data and associated locks
stock_data = {
    "CompanyA": Queue(),
    "CompanyB": Queue(),
    "CompanyC": Queue()
}
stock_locks = {company: threading.Lock() for company in stock_data}

# Function to simulate stock price generation (Producer Thread)
def stock_price_generator():
    companies = list(stock_data.keys())
    while True:
        company = random.choice(companies)
        price = round(random.uniform(100, 500), 2)
        with stock_locks[company]:
            stock_data[company].put(price)
        print(f"Generated price {price} for {company}")
        time.sleep(0.5)  # Simulate delay in stock price updates

# Function to log stock prices to files (Consumer Threads)
def stock_price_logger(company):
    file_name = f"{company}_prices.txt"
    with open(file_name, "w") as file:
        while True:
            with stock_locks[company]:
                if not stock_data[company].empty():
                    price = stock_data[company].get()
                    file.write(f"{time.ctime()}: {price}\n")
                    print(f"Logged {price} for {company} in {file_name}")
            time.sleep(1)  # Simulate delay in logging

# Function to compute and display average prices (Summary Thread)
def average_price_summary():
    while True:
        time.sleep(5)  # Compute average prices every 5 seconds
        print("\n=== Stock Price Summary ===")
        for company in stock_data:
            with stock_locks[company]:
                prices = list(stock_data[company].queue)
            if prices:
                avg_price = round(sum(prices) / len(prices), 2)
                print(f"{company}: Average Price = {avg_price}")
            else:
                print(f"{company}: No data available")
        print("===========================\n")

if __name__ == "__main__":
    # Create and start the producer thread
    producer_thread = threading.Thread(target=stock_price_generator, daemon=True)
    producer_thread.start()

    # Create and start consumer threads for each company
    consumer_threads = []
    for company in stock_data:
        thread = threading.Thread(target=stock_price_logger, args=(company,), daemon=True)
        consumer_threads.append(thread)
        thread.start()

    # Create and start the summary thread
    summary_thread = threading.Thread(target=average_price_summary, daemon=True)
    summary_thread.start()

    # Run the main program for 20 seconds
    time.sleep(20)
    print("\nMain program ends. Logs are saved in company-specific files.")