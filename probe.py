from multiprocessing import Process, Pipe, Queue
from queue import Empty


class WarehouseManager(Process):

    def __init__(self, data=None):
        super().__init__()
        if data is None:
            data = {}
        self.data = data

    def process_request(self, request):
        if request[1] == 'receipt':
            self.data[request[0]] = request[2]
        elif request[1] == 'shipment':
            if request[2] > 0:
                self.data[request[0]] -= request[2]

    def run(self, requests):
        for request in requests:
            self.process_request(request)


if __name__ == '__main__':
    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    manager.run(requests)
    print(manager.data)