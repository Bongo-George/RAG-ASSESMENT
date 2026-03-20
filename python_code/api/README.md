# 🛠️ API Folder

This folder contains the code for deploying the chatbot's agent-based system. This is considered the backend of the application. Below is an overview of the folder structure and its components.

## 📂 Folder Structure

### Agents Folder

The `agents` folder follows an agent-based architecture, where each agent is responsible for a specific task within the chatbot system:

- **guard_agent.py**: Responsible for blocking unrelated or harmful queries.
- **classification_agent.py**: Classifies the user's input and determines which agent should respond.
- **details_agent.py**: Handles questions related to coffee shop details and menu items.
- **order_taking_agent.py**: Manages the order-taking process, ensuring structured and accurate order data.
- **recommendation_agent.py**: Interacts with the recommendation engine to provide personalized product suggestions.
- **utils.py**: Contains utility functions for:
  - Retrieving responses from the LLM (Large Language Model).
  - Generating embeddings.
  - Validating JSON outputs for structured data.

### Recommendation Objects Folder

- **recommendation_objects**: Contains the trained recommendation models that are used by the `recommendation_agent.py` to suggest products.

### Other Files

- **agent_controller.py**: Orchestrates the interaction between the agents, coordinating their responses and managing the flow of information.
- **main.py**: Calls the `agent_controller` and integrates with RunPod's deploy functionality.
- **Dockerfile**: Builds the code into a Docker image for deployment.

# 🐳 Deploying on RunPod
To deploy the chatbot API on RunPod:

1. Push Docker Image:
    Push the Dockerfile to your DockerHub account, or you can use the pre-built image:
    ```
    *******/chatbot
    ```
2. Create RunPod Endpoint:

Go to the RunPod serverless section and create a new endpoint.
Fill in the required information, including the DockerHub image.
Add the necessary environment variables from your .env file.

## 🤖 Telegram Bot Integration

The chatbot can be integrated with Telegram to provide a user-friendly interface for customers. The Telegram bot connects to the agent-based chatbot system to handle conversations.

### Setting Up the Telegram Bot

1. **Create a Telegram Bot**:
   - Open Telegram and search for [@BotFather](https://t.me/botfather)
   - Send `/newbot` and follow the instructions
   - Choose a name and username for your bot
   - Copy the **Bot Token** provided by BotFather

2. **Configure Environment Variables**:
   Add the following to your `.env` file:
   ```
   TELEGRAM_BOT_TOKEN=<your_bot_token_from_botfather>
   ```

3. **Running the Telegram Bot Locally**:
   - The bot uses polling (checks for new messages regularly)
   - The bot can be run alongside the main API
   - Simply start the bot script and it will begin listening for messages

4. **Deploying to Production**:
   - Deploy using Docker on RunPod or your preferred cloud platform
   - The bot will connect to your main API endpoints
   - Messages are processed through the agent system and responses are sent back via Telegram

## 🚀 Running the Code Locally

1. **Set Up Environment Variables**:  
   Ensure that the required variables are set in your `.env` file.
   
2. **Install Dependencies**:  
   Install the necessary dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Code**:   
    You can run the chatbot locally by executing:
    ```bash
    python development_code.py
    ```