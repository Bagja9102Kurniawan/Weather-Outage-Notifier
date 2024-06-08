## Deliverable Project: Weather and Power Outage Notification System

### Project Overview
This project demonstrates various skills and technologies essential for a Fullstack Python AI and Automation Data Developer. The deliverables include:

1. **Weather Data Retrieval Using REST API**
2. **Automated Email Notifications for Power Outages**
3. **Unit Testing for Code Quality Assurance**
4. **Comprehensive Project Documentation**

### 1. Weather Data Retrieval Using REST API

#### Objective
Retrieve the current weather data for a specified location using a REST API.

#### Implementation
We used the Weatherbit API to fetch weather data for the city of Tangerang. The data includes temperature, weather description, and city name.

### 2. Automated Email Notifications for Power Outages

#### Objective
Automatically send email notifications if a power outage occurs in a specified region by scraping data from a relevant website.

#### Implementation
We scraped power outage information from `https://www.rri.co.id/sprint?query=pemadaman+listrik` and used the SMTP library to send an email notification.

### 3. Unit Testing

#### Objective
Write unit tests for the weather data retrieval function to ensure code quality and reliability.

#### Implementation
We used the `unittest` module to create tests for the `get_current_weather` function, covering both successful and error scenarios.

### 4. Documentation

#### Objective
Provide comprehensive documentation for the project, including descriptions of modules and functions.