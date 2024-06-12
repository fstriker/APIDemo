import requests as rs

ip = "0.0.0.0" # Replace with actual ip

if __name__ == '__main__':
    print(f"Testing Connection...")
    status = rs.get(f"http://{ip}").status_code
    print(f"Status Code: {status}")
    if status == 200:
        print("Connection successful")
        
    print(f"Simulating federated learning process...")
    print(f"Starting device registration...")
    print(rs.get(f"http://{ip}/register").status_code)
    print(rs.get(f"http://{ip}/register").content)
    print(f"Fetch selected participants...")
    print(rs.get(f"http://{ip}/fl-runs/0/participants").content)
    print(f"Fetch FL configuration...")
    print(rs.get(f"http://{ip}/fl-runs/0/configuration").content)
    print(f"Fetch process status...")
    print(rs.get(f"http://{ip}/fl-runs/0/status").content)
