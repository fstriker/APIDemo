import requests as rs

ip = "0.0.0.0" # Replace with actual ip

if __name__ == '__main__':
    print(f"Testing Connection...")
    status = rs.get(f"http://{ip}").status_code
    print(f"Status Code: {status}")
    if status == 200:
        print("Connection successful")
        
    print(f"Simulating Federated Learning Registration...")
    print(rs.get(f"http://{ip}/register").status_code)
    print(rs.get(f"http://{ip}/register").content)
