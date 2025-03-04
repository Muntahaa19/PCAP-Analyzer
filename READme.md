PCAP Analyzer Tool

Overview

The PCAP Analyzer Tool is a machine learning-based network security tool that analyzes packet capture (PCAP) files to detect potential security threats. It leverages Scapy, PyShark, and a trained Random Forest model to classify network traffic as either normal or anomalous.

Features

PCAP File Parsing: Extracts essential network traffic details from PCAP files.

Feature Extraction: Computes key traffic metrics such as source/destination IP counts and packet lengths.

Machine Learning-Based Detection: Utilizes a pre-trained Random Forest Classifier for anomaly detection.

Automated Threat Alerts: Identifies potential threats in new network traffic.

Performance Evaluation: Provides accuracy, precision, and recall metrics.

Installation

Ensure you have Python 3.x installed and then install the required dependencies:

pip install scapy pyshark pandas numpy scikit-learn joblib

Usage

1. Load a PCAP File and Extract Network Data

from pcap_analyzer import load_pcap

pcap_df = load_pcap("network_traffic.pcap")
print(pcap_df.head())

2. Extract Features for Machine Learning

from pcap_analyzer import extract_features

feature_df = extract_features(pcap_df)
print(feature_df)

3. Train the Machine Learning Model

from pcap_analyzer import train_model
train_model("network_dataset.csv")  # Trains and saves the model

4. Detect Anomalies in New PCAP Files

from pcap_analyzer import detect_anomalies

detect_anomalies("new_traffic.pcap")

Future Enhancements

Integration with Deep Learning for advanced threat detection.

Real-time PCAP analysis for continuous monitoring.

Web-based UI for user-friendly interaction.

Author

Developed by Muntaha Nasir.

For inquiries, contact muntahanasir786@gmail.com.
