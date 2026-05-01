
# 🛡️ HHS / CBP Operational Command Center

### Predictive Intelligence for the UAC Program

Every year, thousands of children travel long distances—often alone—to reach the U.S. Southern Border.
This project acts like a **“weather forecast” for humanitarian operations**, predicting how many children will arrive at shelters **7 days in advance**—ensuring there is always a **bed, a doctor, and a safe pathway forward**.

An automated **Data Engineering Pipeline** and **Interactive Analytics Dashboard** built to monitor and audit the **HHS Unaccompanied Alien Children (UAC) Program**.
It transforms raw government datasets into a **Command Center** for tracking capacity, forecasting intake, and identifying system strain.

---

## 🚀 Engineering & Automation Highlights

* ⚙️ **Automated ETL Pipeline** – Cleans, processes, and exports structured data
* 📤 **Auto Data Export** – Generates `UAC_Clean_Final.csv` for audit/SQL use
* 🧹 **Data Sanitization** – Fixes comma-separated numbers (`"12,400"` → `12400`)
* 🧠 **Self-Generating App** – Generates `streamlit_app.py` from notebook/pipeline
* 🚨 **System Strain Detection** – Flags high-risk days using percentile logic

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Data**: Pandas, NumPy
* **Visualization**: Plotly
* **Dashboard**: Streamlit
* **Deployment**: Localtunnel, Google Colab

---

## ⚡ How to Use

You can interact with this project in **four ways**:

---

### ⚡ Option 1: Direct Access

* Open the deployed Streamlit link (**streamlit_interface_hhs**)
* Instant dashboard access

---

### 💻 Option 2: Local Execution (VS Code / Terminal)

* Place the following files in the **same folder**:

  * `healthcare1_(1).ipynb`
  * `HHS_Unaccompanied_Alien_Children_Program.csv`
  * `requirements.txt`

* Run the notebook to generate the app, then launch:
 ```bash
pip install -r requirements.txt
```

```bash
streamlit run streamlit_app.py
```

* Open: [http://localhost:8501](http://localhost:8501)

---

### 🌐 Option 3: Streamlit Cloud (Public Interface)

1. Push project to GitHub
2. Go to Streamlit Cloud
3. Select repository + `streamlit_app.py`
4. Click **Deploy**

✅ Get a public shareable link
✅ No setup required for users

---

### 🔧 Option 4: Execute Through Code (Google Colab)

**No installation required**

1. Open Google Colab

2. Upload:

   * `healthcare1_(1).ipynb`
   * `HHS_Unaccompanied_Alien_Children_Program.csv`

3. Run all cells

4. Access dashboard:

   * Copy IP from output
   * Open Localtunnel link
   * Paste IP → Submit

**Output:**

* `UAC_Clean_Final.csv` (clean dataset)
* `streamlit_app.py` (generated app)
* Live Streamlit dashboard

---

## 📁 Project Structure

```
├── HHS_Unaccompanied_Alien_Children_Program.csv   # Raw dataset
├── UAC_Clean_Final.csv                           # Clean dataset
├── healthcare1_(1).ipynb                         # Main pipeline notebook (ETL + generation)
├── streamlit_app.py                              # Dashboard app
├── steamlit_interface_hhs/                       # UI / interface assets
├── requirements.txt                              # Dependencies
├── README.md                                     # Documentation
├── medium_EDA_link                               # Project report
```

---

## 📊 Outputs

* 📄 Clean dataset (`UAC_Clean_Final.csv`)
* 📊 Interactive dashboard

---

## 📌 Use Cases

* Capacity planning
* Operational monitoring
* Data engineering showcase

---

## 👨‍💻 Author

**Vaishakh Sivarajan**




