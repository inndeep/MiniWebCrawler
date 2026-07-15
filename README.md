```markdown
# 🕷️ WebRecon - Mini Web Crawler

WebRecon is a lightweight, fast, and targeted Python web crawler designed for the reconnaissance (information gathering) phase of penetration testing. It analyzes the HTML source code of a target page to map out its attack surface and discover potential entry points.

## 🚀 Features

* **Endpoint Discovery:** Extracts all visible links (`<a>`), background JavaScript files (`<script>`), and data submission targets (`<form>`).
* **Intelligent URL Joining:** Automatically resolves and combines relative paths (e.g., `/api/v1/login`) with the base domain to generate fully clickable URLs.
* **Deduplication:** Uses Python's `set()` data structure to prevent duplicate URLs, ensuring clean and concise output.
* **Categorized & Colored Output:** Neatly organizes the discovered assets in the terminal using ANSI color codes (Green for headers, Yellow for JS files, Red for form actions).
* **Error Handling:** Safely handles connection errors and invalid responses without crashing.

## 🛠️ Installation

Ensure you have Python 3.x installed on your system.

1. Clone the repository:
```bash
git clone [https://github.com/YOUR_USERNAME/WebRecon.git](https://github.com/YOUR_USERNAME/WebRecon.git)
cd WebRecon

```

2. Install the required dependencies:

```bash
pip install requests beautifulsoup4 lxml

```

## 💻 Usage

Run the script from your terminal and provide the target URL using the `-u` or `--url` argument.

```bash
python main.py -u [https://example.com](https://example.com)

```

### Example Output:

```text
[+] JAVASCRIPT FILES
--------------------------------------------------
[https://example.com/assets/js/main.js](https://example.com/assets/js/main.js)
[https://example.com/api/tracker.js](https://example.com/api/tracker.js)

[+] LINKS FOUND
--------------------------------------------------
[https://example.com/about-us](https://example.com/about-us)
[https://example.com/contact](https://example.com/contact)
[https://example.com/product?id=1](https://example.com/product?id=1)

[+] FORMS (DATA TARGETS)
--------------------------------------------------
[https://example.com/login_process.php](https://example.com/login_process.php)

```

## ⚠️ Legal Disclaimer

This tool is developed strictly for **legal, authorized penetration testing** and educational purposes. Using this tool against targets without explicit permission is illegal. The developer assumes no liability and is not responsible for any misuse or damage caused by this program. Use it only on systems you own or have explicit permission to test (e.g., Bug Bounty programs, VDPs).

```
```
