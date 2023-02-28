import csv
import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.counter = {}
        date_time = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f'{BASE_DIR}/status_summary_{date_time}.csv'
        self.file = open(filename, mode='w', encoding='utf-8')

    def process_item(self, item, spider):
        status = item['status']
        self.counter[status] = self.counter.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        fieldnames = ['Статус', 'Количество']
        writer = csv.DictWriter(self.file, fieldnames=fieldnames)
        writer = csv.writer(self.file, delimiter=",")
        writer.writerow(fieldnames)
        for item in self.counter.items():
            writer.writerow([item[0], item[1]])
        writer.writerow(['Total', sum(self.counter.values())])
        self.file.close()
