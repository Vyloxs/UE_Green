import matplotlib.pyplot as plt
import csv
import datetime

def parse_csv(filename: str, delimiter: str = ','):
    data = {}

    with open(filename) as file:
        csvfile = csv.reader(file, delimiter=delimiter)
        values = [line for line in csvfile]
        for date, cpu_usage, total, cpu_power, gpu_power in values[1:]:
            
            data[int(datetime.datetime.fromisoformat(date).timestamp())] = {
                'cpu_usage': float(cpu_usage),
                'total': float(total),
                'cpu_power': float(cpu_power),
                'gpu_power': float(gpu_power)
            }

    return data

def compute_avg(filename: str, key: str = 'total'):
        data = parse_csv(filename)
        return sum([x[key] for x in data.values()]) / len(data.values())

def get_consumption(filename: str, idle: float) -> float:
    avg = compute_avg(filename) - idle
    data = parse_csv(filename)
    return avg * len(data.values())

def power_evolution_graph(filename: str, idle: float = 0.0, key: str = 'total', name: str = None):
    data = parse_csv(filename)

    plt.figure(figsize=(10, 6))

    plt.title(name)
    plt.xlabel('Temps (s)')
    plt.ylabel('Puissance (W)')

    beg = list(data.keys())[0]

    values = [x['total'] - idle for x in data.values()]
    plt.plot([v - beg for v in data.keys()], values)


    plt.legend()
    plt.grid(True)
    plt.show()

def energy_comparison_graph(firefox: str, chrome: str, idle: float, method: str):
    firefox_consumption = get_consumption(firefox, idle)
    chrome_consumption = get_consumption(chrome, idle)

    plt.figure()

    plt.title(f'Comparaison de la consommation totale de Chrome et Firefox ({method})')
    plt.xlabel('Navigateur')
    plt.ylabel('Consommation (J)')

    plt.bar(('Firefox', 'Chrome'), (firefox_consumption, chrome_consumption), color=['blue', 'green'])

    plt.legend()
    plt.grid(False)
    plt.show()


idle_avg = compute_avg('idle.csv') # average power

print(f'Puissance (W) en IDLE : {idle_avg:.2f} W')
part = 1

if part == 1:
    print('Méthode 1')
    print('='*20)

    power_evolution_graph('firefox-1.csv', idle_avg, name='Evolution de la puissance pour "Firefox (méthode 1)"')
    power_evolution_graph('chrome-1.csv', idle_avg, name='Evolution de la puissance pour "Chrome" (méthode 1)')
    energy_comparison_graph('firefox-1.csv', 'chrome-1.csv', idle_avg, 'méthode 1')

    print('Méthode 2')
    print('='*20)

    power_evolution_graph('firefox-pid.csv', idle_avg, name='Evolution de la puissance pour "Firefox (méthode 2)"')
    power_evolution_graph('chrome-pid.csv', idle_avg, name='Evolution de la puissance pour "Chrome (méthode 2)"')
    energy_comparison_graph('firefox-pid.csv', 'chrome-pid.csv', idle_avg, 'méthode 2')

    print('Méthode 3')
    print('='*20)

    power_evolution_graph('firefox-pidN-1.csv', idle_avg, name='Evolution de la puissance pour "Firefox (méthode 3)"')
    power_evolution_graph('chrome-pidN-1.csv', idle_avg, name='Evolution de la puissance pour "Chrome (méthode 3)"')
    energy_comparison_graph('firefox-pidN-1.csv', 'chrome-pidN-1.csv', idle_avg, 'méthode 3')




    """
    Conclusion: Aucune différence notable de consommation électrique en fonction de la méthode de mesure. Firefox consomme plus que Chrome. cqfd.
    """

def power_lang_graph():
    plt.figure()
    
    idle_avg = compute_avg('idle.csv') # average power
    python = parse_csv('bench-python.csv')
    c = parse_csv('bench-c.csv')
    java = parse_csv('bench-java.csv')
    java2 = parse_csv('bench-java2.csv')


    plt.title('Evolution de la consommation électrique en fonction du langage / programme.')
    plt.xlabel('Langage')
    plt.ylabel('Puissance (W)')

    for data, color, label in zip((python, c, java, java2), ('blue', 'green', 'red', 'orange'), ('Python', 'C', 'Java', 'Java2')):
        beg = list(data.keys())[0]
        values = [x['total'] - idle_avg for x in data.values()]
        plt.plot([v - beg for v in data.keys()], values, label=label)

    
    plt.legend(loc="upper right")
    plt.grid(False)
    plt.show()

def lang_energy_comparison():
    idle_avg = compute_avg('idle.csv') # average power
    python = get_consumption('bench-python.csv', idle_avg)
    c = get_consumption('bench-c.csv', idle_avg)
    java = get_consumption('bench-java.csv', idle_avg)
    java2 = get_consumption('bench-java2.csv', idle_avg)

    plt.figure()

    plt.title(f'Comparaison de la consommation totale des différents programmes / langages')
    plt.xlabel('Langage')
    plt.ylabel('Consommation (J)')

    plt.bar(('Python', 'C', 'Java', 'Java2'), sorted([python, c, java, java2]), color=['blue', 'green', 'red', 'orange'])

    plt.grid(False)
    plt.show()

power_lang_graph()
lang_energy_comparison()

