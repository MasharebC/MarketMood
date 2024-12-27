# MarktMood

MarktMood is an AI-powered platform that performs sentiment analysis on news articles to predict stock market movements. The project integrates AWS services to provide a seamless experience for analyzing sentiment and predicting stock price trends.

## Features

- **Sentiment Analysis**: Extract sentiment scores from news articles using AWS Comprehend.
- **Stock Price Prediction**: Employ linear regression models to predict stock price trends based on sentiment.
- **Customizable Queries**: Users can analyze sentiment for a stock of their choice.
- **Web Interface**: Interactive dashboard hosted on AWS Elastic Beanstalk.
- **Scalable Infrastructure**: Built using AWS services like Lambda, S3, DynamoDB, and SageMaker.

## Tech Stack

- **Frontend**: React.js
- **Backend**: Flask (Python)
- **Machine Learning**: TensorFlow, AWS SageMaker
- **Cloud Services**: AWS (Elastic Beanstalk, Lambda, S3, DynamoDB, Comprehend)
- **Deployment**: Dockerized for seamless cloud deployment

## Project Workflow

1. **Data Collection**: News articles and stock data are fetched via APIs.
2. **Sentiment Analysis**: AWS Comprehend analyzes article sentiment.
3. **Prediction Model**: A linear regression model predicts stock movements based on sentiment scores.
4. **Dashboard**: Results are displayed on an intuitive web interface.

## How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/MarktMood.git
   cd MarktMood
   ```

2. **Set Up Environment**
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Configure AWS credentials for accessing services.

3. **Run Locally**
   ```bash
   flask run
   ```

4. **Deploy to AWS**
   - Build and push Docker images.
   - Deploy the application to Elastic Beanstalk.

## Future Enhancements

- Integrate advanced predictive models using SageMaker.
- Add visualization tools for enhanced user insights.
- Expand sentiment analysis to cover more data sources.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

---

Let me know if you need additional customization!
