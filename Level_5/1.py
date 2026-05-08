result = dict()
cyber_data = [
    {
        "name": "Omar",
        "role": "Administrator",
        "power": 4,
        "last_login": "2026-05-01 14:22",
        "ip": "192.168.1.10"
    },
    {
        "name": "Lina",
        "role": "Security Analyst",
        "power": 2,
        "last_login": "2026-05-02 09:11",
        "ip": "192.168.1.25"
    },
    {
        "name": "Youssef",
        "role": "Guest",
        "power": 1,
        "last_login": "2026-04-30 20:45",
        "ip": "192.168.1.50"
    },
    {
        "name": "Sara",
        "role": "Penetration Tester",
        "power": 3,
        "last_login": "2026-05-03 18:05",
        "ip": "192.168.1.33"
    },
    {
        "name": "Ali",
        "role": "Intern",
        "power": 1,
        "last_login": "2026-05-01 08:30",
        "ip": "192.168.1.77"
    }
]

def sorter(data):
    a = sorted(data, key=lambda x: x["power"])
    return a

def filtering(min_power):
    b = list(filter(lambda x: x["power"] >= min_power, cyber_data))
    return b

def transformer():
    d = list(map(lambda x: f"* {x['name']} *", cyber_data))
    return d

mx = max(cyber_data, key=lambda x: x["power"]) 
mn = min(cyber_data, key=lambda x: x["power"])
sm = sum(map(lambda x: x["power"], cyber_data))

result["max_power"] = mx["power"]
result["min_power"] = mn["power"]
average = sm / len(cyber_data)
result["avegare"] = round(average, 2)

if __name__ == "__main__":
    print(result)
