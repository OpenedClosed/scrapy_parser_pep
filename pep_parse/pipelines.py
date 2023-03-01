import csv
import datetime as dt

from pep_parse.settings import BASE_DIR


class PepParsePipeline:

    def open_spider(self, spider):
        self.counter = {}
        date_time = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.filename = f'{BASE_DIR}/status_summary_{date_time}.csv'

    def process_item(self, item, spider):
        status = item['status']
        self.counter[status] = self.counter.get(status, 0) + 1
        return item

    def close_spider(self, spider):
        with open(self.filename, mode='w', encoding='utf-8') as file:
            fieldnames = ['Статус', 'Количество']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer = csv.writer(file, delimiter=",")
            result = [
                ('Статус', 'Количество')
            ] + (
                list(self.counter.items())
            ) + [
                ('Total', sum(self.counter.values()))
            ]
            writer.writerows(result)
