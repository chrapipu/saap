import json

def read_firms(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.readlines()

def process_firms(firms_data):
    firms_profit = {}
    total_profit = 0
    profitable_firms = 0

    for line in firms_data:
        name, ownership, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms_profit[name] = profit

        if profit > 0:
            total_profit += profit
            profitable_firms += 1

    average_profit = total_profit / profitable_firms if profitable_firms > 0 else 0
    return [firms_profit, {"average_profit": average_profit}]

def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def main():
    file_path = 'firms.txt'
    firms_data = read_firms(file_path)
    processed_data = process_firms(firms_data)
    print(processed_data)  # Для проверки

    json_file_path = 'firms_summary.json'
    save_to_json(processed_data, json_file_path)

if __name__ == "__main__":
    main()
