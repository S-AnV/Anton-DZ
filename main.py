from multiprocessing import Process, Manager, Pipe, Queue


class WarehouseManager:
    def __init__(self, manager):
        self.data = manager.dict()

    def process_request(self, request):
        if request[1] == 'receipt':
            self.data[request[0]] = request[2]
        elif request[1] == 'shipment':
            if request[2] > 0:
                self.data[request[0]] -= request[2]
            else:
                self.run(requests)


    def run(self, requests):
        processes = []
        for request in requests:
            p = Process(target=self.process_request, args=(request,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()


if __name__ == '__main__':
    with Manager() as manager:
        manager = WarehouseManager(manager)

        requests = [
            ("product1", "receipt", 100),
            ("product2", "receipt", 150),
            ("product1", "shipment", 30),
            ("product3", "receipt", 200),
            ("product2", "shipment", 50)
        ]

        manager.run(requests)
        print(dict(manager.data))