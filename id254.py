import streamlit as st
import socket
from datetime import datetime

st.title("DNS Resolver and Port Scanner")

# Input for the domain name
domain_name = st.text_input("Enter a domain name:")

if st.button("Resolve"):
    try:
        ip_address = socket.gethostbyname(domain_name)
        st.success(f"The IP address for {domain_name} is: {ip_address}")
    except socket.gaierror:
        st.error(f"Hostname {domain_name} could not be resolved.")

# Input for port range
st.subheader("Port Scanning")
start_port = st.number_input("Start Port", 1, 65535, 1)
end_port = st.number_input("End Port", 1, 65535, 1000)

if st.button("Scan Ports"):
    open_ports = []
    closed_ports = []

    st.write("-" * 50)
    st.write("Scanning IP:", ip_address)
    st.write("Time started:", datetime.now())
    st.write("-" * 50)

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
            st.write(f"Port {port}: Open")
        else:
            closed_ports.append(port)
        sock.close()

    if open_ports:
        st.success("Open Ports:")
        st.write(open_ports)
    if closed_ports:
        st.error("Closed Ports:")
        st.write(closed_ports)
