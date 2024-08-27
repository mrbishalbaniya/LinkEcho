# LinkEcho

**LinkEcho** is a recursive URL finder designed to extract and list all URLs from a given web page up to a specified depth. It can be useful for web scraping, site crawling, or simply discovering links within a website.

## Features

- Recursive URL discovery up to a specified depth
- Option to save results to a file
- Customizable URL fetch depth

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/mrbishalbaniya/LinkEcho.git

# LinkEcho

**LinkEcho** is a recursive URL finder designed to extract and list all URLs from a given web page up to a specified depth. It can be useful for web scraping, site crawling, or simply discovering links within a website.

## Features

- Recursive URL discovery up to a specified depth
- Option to save results to a file
- Customizable URL fetch depth

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mrbishalbaniya/LinkEcho.git
    ```

2. Navigate to the project directory:

    ```bash
    cd LinkEcho
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the script, use the following command:

    ```bash
    python LinkEcho.py -u <URL> [-d <depth>] [-o <output_file>]
    ```

### Arguments

- `-u`, `--url`: **Required**. The URL to fetch.
- `-d`, `--depth`: **Optional**. Maximum depth for URL recursion (default is `1`).
- `-o`, `--output`: **Optional**. File to save results (if not specified, results will not be saved to a file).

### Example

    ```bash
    python LinkEcho.py -u http://example.com -d 2 -o results.txt
    ```

This command will fetch URLs from `http://example.com` up to a depth of `2` and save the results to `results.txt`.



## Contributing

Contributions are welcome! Please open an issue or submit a pull request to contribute to this project.


