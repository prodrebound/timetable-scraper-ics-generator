# timetable-scraper-ics-generator

A Python project for extracting university timetables and generating ICS calendar files.

## Features

- Scrapes timetables from supported sources
- Converts data to ICS format
- Easy integration with calendar applications

## Installation

```bash
pip install -r requirements.txt
```

## Usage

1. Configure the scraper with the env.py
2. Run the main script:
    ```bash
    python main.py
    ```
3. Import the generated ICS file into your calendar application or publish it on your server. For further instructions, refer to the docs of your web server.

## Project Structure
- `main.py`: Entry point of the application
- `env.py`: Configuration file for environment variables
- `requirements.txt`: List of dependencies
- `output/`: Directory where generated ICS files are stored
- `datatypes/`: Contains data models used in the project
- `utils/`: Utility functions for various tasks'

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.