#!/usr/bin/python3

import requests
import csv
import json

r = requests.get("https://jsonplaceholder.typicode.com/posts")

if r.status_code == 200:
    posts = r.json()
else:
    print("Failed to fetch data")


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status code:", response.status_code)

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(f"{post['title']}")
    else:
        print("Failed to fetch posts.")

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        csv_filename = "posts.csv"
        with open(csv_filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, 
            fieldnames=["userId", "id", "title", "body"])
            writer.writeheader()
            for post in posts:
                writer.writerow({
                "userId": post["userId"],
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
                })
        print(f"Posts saved succesfully to {csv_filename}!")
    else:
        print("Failed to fetch posts.")