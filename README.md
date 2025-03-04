**PCAP Analyzer Tool**

:pushpin:**Overview**

The PCAP Analyzer Tool is a machine learning-based network security tool that analyzes packet capture (PCAP) files to detect potential security threats. It leverages Scapy, PyShark, and a trained Random Forest model to classify network traffic as either normal or anomalous.

:pushpin:**Features**

1. PCAP File Parsing: Extracts essential network traffic details from PCAP files.

2. Feature Extraction: Computes key traffic metrics such as source/destination IP counts and packet lengths.

3. Machine Learning-Based Detection: Utilizes a pre-trained Random Forest Classifier for anomaly detection.

4. Automated Threat Alerts: Identifies potential threats in new network traffic.

5. Performance Evaluation: Provides accuracy, precision, and recall metrics.

:pushpin:**Installation**

Ensure you have Python 3.x installed and then install the required dependencies:

pip install scapy pyshark pandas numpy scikit-learn joblib

:pushpin:**Usage**

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

:pushpin:**Future Enhancements**

Integration with Deep Learning for advanced threat detection.

Real-time PCAP analysis for continuous monitoring.

Web-based UI for user-friendly interaction.

:pushpin:**Author**

Developed by Muntaha Nasir.

For inquiries, contact muntahanasir786@gmail.com.
