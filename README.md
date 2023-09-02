# HooperHooper 🏀

> Connecting basketball enthusiasts around the globe.

## Vision

Bringing together and organizing the pickup basketball community. Our platform seeks to seamlessly connect players, enable the formation of squads, and schedule matches.

## 🌟 Features 

- **User Profiles:** Build your basketball resume with stats, videos, and more.
- **Find Nearby Courts:** Integrated with Google Maps and Apple MapKit.
- **Player Ratings:** Rookie, Baller, Hooper, HooperHooper, MVP - Where do you rank?
- **Notifications:** Get alerts for planned games in your vicinity.
- **Live Sessions:** Watch and join live basketball events.
- **Friend System:** Connect and build your basketball network.
- **Space Management:** Exclusive partnerships with gyms and court locations.

## 🚀 Getting Started

### Prerequisites

- Python (3.8+ recommended)
- PostgreSQL
- Docker
- AWS CLI (configured with appropriate credentials)

### Setting up the Development Environment

1. **Clone the Repository**
    ```bash
    git clone [your-repository-link]
    cd hooperhooper
    ```

2. **Set up the Backend**

    If using Flask:
    ```bash
    pip install flask
    ```

    Or Django:
    ```bash
    pip install django
    ```

3. **Database Setup**

    Set up a local PostgreSQL instance or connect to AWS RDS.

4. **Run the Application with Docker**

    ```bash
    docker build -t hooperhooper-app .
    docker run -p 8000:8000 hooperhooper-app
    ```

5. Visit `http://localhost:8000` in your browser.

## 🛠 Tech Stack

- **Backend**: Python with Django/Flask
- **Database**: PostgreSQL on Amazon RDS
- **Maps Integration**: Google Maps Platform & Apple MapKit
- **Hosting & Server**: AWS Elastic Beanstalk, Lambda & API Gateway
- **Storage**: Amazon S3
- **Caching**: Amazon ElastiCache
- **Mobile**: Flutter

## 🤝 Contributing

We encourage you to contribute to HooperHooper! Please check out the [CONTRIBUTING.md](#) for guidelines about how to proceed.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE.md](#) file for details.

## 🙌 Acknowledgments

- NBA & Big3 Leagues for the inspiration.
- YouTube basketball community for the influence.
- Special thanks to all our partners and the open-source community.
