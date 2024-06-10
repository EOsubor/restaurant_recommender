# Restaurant Recommender

This project is a basic restaurant recommendation program. By entering a cuisine type, the program suggests restaurants that serve that cuisine. The program is implemented using Python and can be run as a Streamlit web application.

## Project Structure

- `linkedlist.py`: Defines the `ChainList` class.
- `node.py`: Defines the `NodeItem` class used by the `ChainList`.
- `welcome.py`: Contains a function to display a welcome message.
- `data.py`: Contains data about different cuisines and restaurants.
- `script.py`: Main script to load data into the linked list structures.
- `app.py`: Streamlit application to interact with the recommender system.

## How to Run

1. **Clone the repository**:
    ```sh
    git clone https://github.com/EOsubor/restaurant_recommender.git
    cd restaurant_recommender
    ```

2. **Install dependencies**:
    ```sh
    pip install streamlit
    ```

3. **Run the Streamlit app**:
    ```sh
    streamlit run app.py
    ```

## How to Use

1. When you run the app, you will see a welcome message.
2. Use the dropdown menu to select a cuisine type.
3. The app will display a list of restaurants offering the selected cuisine.

## Deployment

To deploy this app using Streamlit Sharing:

1. Push your code to GitHub.
2. Follow the instructions on [Streamlit Sharing](https://streamlit.io/sharing) to deploy your app.

Alternatively, you can use a platform like Netlify with Docker to deploy your app.

## License

This project is licensed under the MIT License.
