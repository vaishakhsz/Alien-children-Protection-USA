🛡️ HHS/CBP Operational Command Center

An automated Data Engineering Pipeline and Interactive Analytics Dashboard built to monitor and audit the HHS Unaccompanied Alien Children (UAC) Program. This project transforms raw government datasets into a high-fidelity "Command Center" for tracking system capacity and operational strain.

🚀 Engineering & Automation Highlights
Automated Data Export: Upon execution, the script automatically sanitizes the raw data and triggers an immediate download of the processed file (UAC_Clean_Final.csv), providing a clean dataset ready for external audit or SQL ingestion.

Self-Generating Architecture: The main Python script acts as a deployment engine. It performs the ETL (Extract, Transform, Load) process and then dynamically writes the standalone streamlit_app.py web-interface code to the local directory.

Data Sanitization (The "Comma Bug"): Implemented a regex-based cleaning pipeline to handle thousand-separator artifacts (e.g., converting "12,400" from a string to an integer) to ensure 100% calculation accuracy across all metrics.

Operational Intelligence: Developed custom logic for System Strain Identification, defined as days where both total population load and intake volatility exceed the 75th percentile.

🛠️ Tech Stack

Language: Python 3.10+

Analytics: Pandas, NumPy

Visuals: Plotly Express & Graph Objects

Web Framework: Streamlit

Deployment: Localtunnel / Google Colab

⚡ How to Run

Option 1: Google Colab (Fastest "No-Install" Method)
Upload the Main Script and the HHS_Unaccompanied_Alien_Children_Program.csv to your Colab session storage.

Run the script cells.

Automatic Export: The cleaned CSV will download to your computer automatically once the data engine finishes processing.

To Access the Dashboard:

Copy the IP Address printed in the Colab output (e.g., 35.243.x.x).

Click the Localtunnel Link provided in the output.

Paste the IP into the "Endpoint IP" box and hit Submit.


Option 2: Local Execution (VS Code / Terminal)
Ensure you have the main script and the .csv data in the same folder.

Run the script once to generate the app file: python your_script_name.py

Install dependencies: pip install streamlit pandas plotly numpy

Launch the dashboard: streamlit run streamlit_app.py

📊 Analytics Suite
System Load Analysis: Unified tracking of Agency Responsibility (HHS vs. CBP).

Monthly Throughput: Comparative bar charts for Intake vs. Discharge efficiency.

Strain Detection: Visual markers for acute operational pressure events.

Backlog Tracking: Cumulative growth visualization of net system pressure over time.
