🛡️ HHS / CBP Operational Command Center
Predictive Intelligence for the UAC Program

Every year, thousands of children travel long distances—often alone—to reach the U.S. Southern Border.
This project acts like a “weather forecast” for humanitarian operations, predicting how many children will arrive at shelters 7 days in advance—ensuring there is always a bed, a doctor, and a safe pathway forward.

An automated Data Engineering Pipeline and Interactive Analytics Dashboard built to monitor and audit the HHS Unaccompanied Alien Children (UAC) Program.
It transforms raw government datasets into a Command Center for tracking capacity, forecasting intake, and identifying system strain.

🚀 Engineering & Automation Highlights
⚙️ Automated ETL Pipeline – Cleans, processes, and exports structured data
📤 Auto Data Export – Generates UAC_Clean_Final.csv for audit/SQL use
🧹 Data Sanitization – Fixes comma-separated numbers ("12,400" → 12400)
🧠 Self-Generating App – Generates streamlit_app.py from notebook/pipeline
🚨 System Strain Detection – Flags high-risk days using percentile logic

🛠️ Tech Stack
Language: Python 3.10+
Data: Pandas, NumPy
Visualization: Plotly
Dashboard: Streamlit
Deployment: Localtunnel, Google Colab

*How to Use*
You can interact with this project in four ways:

⚡ Option 1: Direct Access
Open the deployed Streamlit link(steamlit interface hhs)
Instant dashboard access

💻 Option 2:### 🔧 Local Execution (VS Code / Terminal)

- Place the following files in the **same folder**:
   - `healthcare ipynb file`
   - `HHS_Unaccompanied_Alien_Children_Program.csv`
   - `requirements.txt`

- Run the script once to generate the app file:
   ```bash
   python streamlit_app.py


🌐 Option 3: Streamlit Cloud (Public Interface)

-Push project to GitHub
-Go to Streamlit Cloud
-Select repo + streamlit_app.py
-Click Deploy
✅ Get a public shareable link
✅ No setup required for viewers


🔧Option 4: Execute Through Code (Google Colab) ( No installation required)

Open Google Colab
-Upload:
healthcare1_(1).ipynb
HHS_Unaccompanied_Alien_Children_Program.csv

-Run all cells

-Access dashboard:
Copy IP from output
Open Localtunnel link
Paste IP → Submit

-Output:
Clean dataset (UAC_Clean_Final.csv)
Generated streamlit_app.py
Streamlit dashboard


📁 Project Structure
├── HHS_Unaccompanied_Alien_Children_Program.csv   # Raw dataset
├── UAC_Clean_Final.csv                           # Clean dataset
├── healthcare1_(1).ipynb                         # Main pipeline notebook (ETL + generation)
├── streamlit_app.py                              # Dashboard app
├── steamlit_interface_hhs/                       # UI / interface components & assets
├── requirements.txt                              # Dependencies
├── README.md                                     # Documentationn
├──medium EDA link                                #project report

📊 Outputs
 📄 Clean dataset (UAC_Clean_Final.csv)
 📊 Interactive dashboard

📌 Use Cases
-Capacity planning
-Operational monitoring
-Data engineering showcase

👨‍💻 Author
Vaishakh Sivarajan

