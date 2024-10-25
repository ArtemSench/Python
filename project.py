import os
import pandas as pd


class PriceMachine:

    def __init__(self):
        self.data = []
        self.result = ''

    def load_prices(self, directory='D:/UserFiles/Downloads/1/Python/Praktika/PriceMachine'):
        """
        Сканирует указанный каталог. Ищет файлы со словом price в названии.
        В файле ищет столбцы с названием товара, ценой и весом.
        """
        for filename in os.listdir(directory):
            if 'price' in filename and filename.endswith('.csv'):
                file_path = os.path.join(directory, filename)
                df = pd.read_csv(file_path, sep=',', encoding='utf-8')
                self._process_file(df, filename)

    def _process_file(self, df, filename):
        """
        Обрабатывает DataFrame, извлекая необходимые столбцы.
        """
        headers = df.columns.str.lower()
        print(headers)

        product_col = self._search_product_price_weight(headers, ['название', 'продукт', 'товар', 'наименование'])
        price_col = self._search_product_price_weight(headers, ['цена', 'розница'])
        weight_col = self._search_product_price_weight(headers, ['фасовка', 'масса', 'вес'])

        if product_col is not None and price_col is not None and weight_col is not None:
            for _, row in df.iterrows():
                self.data.append({
                    'name': row[product_col],
                    'price': row[price_col],
                    'weight': row[weight_col],
                    'file': filename,
                    'price_per_kg': row[price_col] / row[weight_col] if row[weight_col] != 0 else 0
                })

    def _search_product_price_weight(self, headers, possible_names):
        """
        Возвращает название столбца, если найдено.
        """
        for name in possible_names:
            if name in headers:
                return headers.get_loc(name)
        return None

    def export_to_html(self, fname='output.html'):
        """
        Экспортирует данные в HTML файл.
        """
        html_content = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Позиции продуктов</title>
        </head>
        <body>
            <table border="1">
                <tr>
                    <th>Номер</th>
                    <th>Название</th>
                    <th>Цена</th>
                    <th>Фасовка</th>
                    <th>Файл</th>
                    <th>Цена за кг.</th>
                </tr>
        '''
        for idx, item in enumerate(self.data, start=1):
            html_content += f'''
                <tr>
                    <td>{idx}</td>
                    <td>{item['name']}</td>
                    <td>{item['price']}</td>
                    <td>{item['weight']}</td>
                    <td>{item['file']}</td>
                    <td>{item['price_per_kg']:.2f}</td>
                </tr>
            '''

        html_content += '''
            </table>
        </body>
        </html>
        '''

        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html_content)

    def find_text(self, text):
        """
        Ищет товары по введенному тексту и возвращает список позиций.
        """
        results = [item for item in self.data if text.lower() in item['name'].lower()]
        results.sort(key=lambda x: x['price_per_kg'])
        return results


if __name__ == '__main__':
    pm = PriceMachine()
    pm.load_prices()  # Загрузка прайс-листов

    while True:
        search_text = input("Введите текст для поиска (или 'exit' для выхода): ")
        if search_text.lower() == 'exit':
            print('Работа завершена.')
            break

        results = pm.find_text(search_text)
        print(results)

        if results:
            print(f"{'№':<3} {'Наименование':<30} {'Цена':<10} {'Вес':<10} {'Файл':<15} {'Цена за кг.':<15}")
            for idx, item in enumerate(results, start=1):
                print(f"{idx:<3} {item['name']:<30} {item['price']:<10} {item['weight']:<10} {item['file']:<15} {item['price_per_kg']:<15.2f}")
        else:
            print("Нет товаров, соответствующих вашему запросу.")

    pm.export_to_html()
