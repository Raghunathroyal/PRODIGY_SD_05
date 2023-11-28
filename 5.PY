import request
import BeautifulSoup
import csv

def scrape_product_information(url):
    response = request.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        product_list = []

        # Extract product information from the website
        for product in soup.find_all('div', class_='product'):
            name = product.find('h2', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            rating = product.find('span', class_='product-rating').text.strip()

            product_info = {
                'Name': name,
                'Price': price,
                'Rating': rating
            }

            product_list.append(product_info)

        return product_list

    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return None

def save_to_csv(product_list, csv_filename='product_information.csv'):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for product in product_list:
            writer.writerow(product)

if __name__ == "__main__":
    # Example URL for an e-commerce website
    example_url = 'https://example.com/products'

    product_list = scrape_product_information(example_url)

    if product_list:
        print("Product Information:")
        for product in product_list:
            print(product)

        save_to_csv(product_list)
        print("Product information saved to product_information.csv")
