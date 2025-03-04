import pyshark

def parse_pcap(file_path):
    packets = []
    capture = pyshark.FileCapture(file_path, display_filter="ip")

    for pkt in capture:
        try:
            packet_info = {
                "timestamp": float(pkt.sniff_time.timestamp()),
                "src_ip": pkt.ip.src,
                "dst_ip": pkt.ip.dst,
                "protocol": pkt.highest_layer,
                "length": int(pkt.length),
                "dst_port": int(pkt[pkt.transport_layer].dstport) if hasattr(pkt, "tcp") or hasattr(pkt, "udp") else None,
                "tcp_flags": getattr(pkt.tcp, "flags", None) if hasattr(pkt, "tcp") else None,  
                "dns_query": getattr(pkt.dns, "qry_name", None) if hasattr(pkt, "dns") else None,  
                "arp_opcode": getattr(pkt.arp, "opcode", None) if hasattr(pkt, "arp") else None  
            }
            packets.append(packet_info)
        except AttributeError:
            continue

    capture.close()
    return packets
