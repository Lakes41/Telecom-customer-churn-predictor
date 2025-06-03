import re
import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ArticleManager:
    def __init__(self, article_text, options=None):
        if not isinstance(article_text, str):
            raise ValueError("The article text must be a string.")

        if options is None:
            options = {}

        self.article_text = article_text
        self.pages = []
        self.words = []
        self.options = {
            'words_per_line': options.get('words_per_line', 12),
            'lines_per_page': options.get('lines_per_page', 20),
            'payment_structure': options.get(
                'payment_structure', {
                    1: 30,
                    2: 30,
                    3: 60,
                    4: 60,
                    'default': 100,
                }
            )
        }
        logging.info("ArticleManager initialized with options: %s", self.options)

    def split_into_pages(self):
        """Splits the article into pages based on the specified words per line and lines per page."""
        words_per_line = self.options['words_per_line']
        lines_per_page = self.options['lines_per_page']

        # Split the article into words
        self.words = re.split(r'\s+', self.article_text.strip())
        logging.info("Total words in article: %d", len(self.words))

        # Calculate total pages
        words_per_page = words_per_line * lines_per_page
        total_pages = math.ceil(len(self.words) / words_per_page)
        logging.info("Total pages calculated: %d", total_pages)

        # Generate pages
        for i in range(total_pages):
            page_words = self.words[i * words_per_page:(i + 1) * words_per_page]
            page_lines = []

            # Create lines for the current page
            for j in range(0, len(page_words), words_per_line):
                page_lines.append(' '.join(page_words[j:j + words_per_line]))

            # Combine lines to form a page
            page = '\n'.join(page_lines)
            self.pages.append(page)

    def calculate_payment(self):
        """Calculates the payment based on the number of pages."""
        payment_structure = self.options['payment_structure']
        total_pages = len(self.pages)
        payment = payment_structure.get(total_pages, payment_structure['default'])

        logging.info("Total pages: %d, Payment due: %d", total_pages, payment)
        return payment

    def display_pages(self):
        """Displays each page and payment information in the console."""
        payment = self.calculate_payment()
        print(f"Total Pages: {len(self.pages)}")
        print(f"Payment Due: ${payment}")
        for index, page in enumerate(self.pages):
            print(f"\nPage {index + 1}:\n{page}\n")
        logging.info("Pages and payment details displayed successfully.")

    def process_article(self):
        """Encapsulates the full process of splitting and displaying the article."""
        logging.info("Starting article processing...")
        self.split_into_pages()
        self.display_pages()
        logging.info("Article processing completed.")

# Example usage
article_text = """
Pain itself is important, being the main focus of life. But it happens that toil and pain sometimes result in great pleasure. To receive even the smallest favor, one must undergo hard work and effort. Avoid pain unless it brings some resulting pleasure. Any resulting pain is to be endured unless it comes from wrongdoing or neglect of duty.
"""
options = {
    'words_per_line': 12,
    'lines_per_page': 20,
    'payment_structure': {
        1: 30,
        2: 50,
        3: 70,
        4: 90,
        'default': 120,
    }
}

article_manager = ArticleManager(article_text, options)
article_manager.process_article()
