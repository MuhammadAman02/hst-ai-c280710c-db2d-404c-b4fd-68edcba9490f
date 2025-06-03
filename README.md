# Hello World Landing Page

A modern, professional landing page built with NiceGUI that demonstrates a clean design, professional visuals, and responsive layout.

![Hello World Landing Page](https://source.unsplash.com/1200x600/?technology&sig=12345)

## Features

- ✨ Modern, responsive design that works on all devices
- 🖼️ Professional imagery with dynamic loading
- 🚀 Fast loading and performance optimized
- 🎨 Beautiful UI with animations and transitions
- 📱 Mobile-friendly interface

## Quick Start

### Running Locally

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
4. Open your browser and navigate to `http://localhost:8000`

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t hello-world-landing .
   ```
2. Run the container:
   ```bash
   docker run -p 8000:8000 hello-world-landing
   ```
3. Open your browser and navigate to `http://localhost:8000`

## Project Structure

```
hello-world-landing/
├── app/
│   ├── core/
│   │   └── assets.py         # Professional asset management
│   ├── static/
│   │   └── css/
│   │       └── main.css      # Professional styling
│   └── main.py               # Main application code
├── main.py                   # Entry point
├── requirements.txt          # Dependencies
├── Dockerfile                # Container configuration
└── README.md                 # Documentation
```

## Technologies Used

- [NiceGUI](https://nicegui.io/) - Python UI framework
- [Unsplash API](https://unsplash.com/) - Professional imagery
- Modern CSS with custom design system
- Docker for containerization

## Customization

You can easily customize this landing page by:

1. Modifying the content in `app/main.py`
2. Adjusting the styling in `app/static/css/main.css`
3. Changing the image categories in `app/core/assets.py`

## Deployment

This application is ready for deployment to platforms like:

- Fly.io
- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run
- Azure App Service

## License

MIT