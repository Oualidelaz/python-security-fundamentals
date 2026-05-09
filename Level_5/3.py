import time
def memory_vault():
    storage = {}

    def store(key, value):
        storage[key] = value

    def recall(key):
        result = storage.get(key)
        if result is None:
            return "Memory not found!"
        else:
            return result

    storage_managment = {
        "store": store,
        "recall": recall,
        "vault": storage
    }
    return storage_managment


if __name__ == "__main__":
    memory = memory_vault()
    store = memory['store']
    recall = memory['recall']
    print("Storing DDoS ...")
    store("DDoS", "Distributed Denial of Service")
    time.sleep(1)
    print("Success!")
    print("Extract Data ...")
    result = recall("DDoS")
    time.sleep(1)
    print(f"The result is: {result}")
    print("Finished!")
