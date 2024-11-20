# Pixela Study Tracker

This project allows you to log, update, and delete daily study hour records using the **Pixela** API. With this script, you can interact with your Pixela account to keep track of your study progress in an easy and convenient way.

## Features

- **Add a new study day**: Logs the study hours for the current day.
- **Update an existing study day**: Modifies the study hours for a specific date.
- **Delete a study record**: Removes a study record for a specific date.

## Requirements

1. **Python 3.x**: Make sure you have Python installed on your machine. If not, download the latest version from the [official Python website](https://www.python.org/downloads/).
2. **Required Libraries**: The script uses the `requests` library to interact with the Pixela API. You can install it by running the following command:

   ```bash
   pip install requests
   ```

3. **Pixela Credentials**: The script requires Pixela API credentials (username, authentication token, and graph ID) to make requests. You can obtain these credentials by creating an account on [Pixela](https://pixe.la/).

## Setup

Before running the script, you need to configure the environment variables `USERNAME`, `TOKEN`, and `GRAPH_ID` with your Pixela credentials.

Create a `.env` file in the same directory as your script with the following content:

```env
USERNAME=your_username
TOKEN=your_token
GRAPH_ID=your_graph_id
```

If you don't have the `python-dotenv` library installed, you can install it with the command:

```bash
pip install python-dotenv
```

This will allow the script to load environment variables from the `.env` file.

## How to Use

1. Clone or download the repository.
2. Place your `.env` file with your credentials in the same directory as the script.
3. Run the script:

   ```bash
   python script_name.py
   ```

4. The script will ask which action you'd like to perform:

   - **1**: Add a new study day.
   - **2**: Update an existing study day.
   - **3**: Delete a study record.

   Respond with the number of your chosen option.

## Example of Execution

Here’s an example of how the execution might look in the terminal:

```bash
Would you like to 
1.add a new study day
2.update an existing one
3.delete a record?
Type 1, 2 or 3: 1
How many hours did you study today? 3
Process completed successfully!
```

## Contributions

If you encounter any issues or would like to suggest improvements, feel free to open an issue or submit a pull request.

---

