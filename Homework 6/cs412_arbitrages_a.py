"""
    name:  Luke Hine

    Honor Code and Acknowledgments:

            This work complies with the JMU Honor Code.
"""
import math


def add_edge(graph, cIn, cOut, rate):
    graph.append((cIn, cOut, -math.log(rate)))


def has_arbitrage(graph, n):
    dist = [float('inf')] * n
    dist[0] = 0
    
    for _ in range(n - 1):
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    
    for u, v, w in graph:
        if dist[u] + w < dist[v]:
            return True
    
    return False


def find_arbitrage(exchange_rates):
    currencies = set()
    for cIn, cOut, _ in exchange_rates:
        currencies.add(cIn)
        currencies.add(cOut)
    
    currency_mapping = {currency: idx for idx, currency in enumerate(currencies)}
    
    n = len(currencies)
    graph = []
    
    for cIn, cOut, rate in exchange_rates:
        u, v = currency_mapping[cIn], currency_mapping[cOut]
        add_edge(graph, u, v, rate)
    
    if has_arbitrage(graph, n):
        return "Arbitrage Detected"
    else:
        return "No Arbitrage Detected"


def main():
    m = int(input())
    exchange_rates = []
    for _ in range(m):
        cIn, cOut, rate = input().split()
        rate = float(rate)
        exchange_rates.append((cIn, cOut, rate))

    result = find_arbitrage(exchange_rates)
    print(result)


if __name__ == "__main__":
    main()