import tkinter as tk
from tkinter import filedialog
import joblib
import pandas as pd
from pcap_parser import parse_pcap
from analysis import detect_threats

def select_pcap_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a PCAP file", filetypes=[("PCAP files", "*.pcap")])
    return file_path

import joblib
import pandas as pd

def detect_anomalies(packets):
    model = joblib.load("threat_model.pkl")  # Load trained ML model
    df = pd.DataFrame(packets)

    # Debugging: Print feature names
    print("✅ Model trained with features:", model.feature_names_in_)
    print("🔍 Input DataFrame features:", df.columns.tolist())

    # Align df with the trained model's features
    df = df.reindex(columns=model.feature_names_in_, fill_value=0)

    # Ensure input is numeric
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)

    predictions = model.predict(df)

    if 1 in predictions:
        print("\n⚠️ ML DETECTION: Suspicious network activity detected!")
    else:
        print("\n✅ ML DETECTION: No anomalies found.")




if __name__ == "__main__":
    pcap_file = select_pcap_file()
    if not pcap_file:
        print("No file selected. Exiting...")
        exit()

    packets = parse_pcap(pcap_file)  
    detect_threats(packets) 
    detect_anomalies(packets)  
