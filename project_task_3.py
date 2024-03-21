import networkx as nx
import heapq

roads = {("Lviv", "Rivne"): {"weight": 211}, ("Rivne", "Zhytomyr"): {"weight": 190},
         ("Zhytomyr", "Kyiv"): {"weight": 139}, ("Kyiv", "Uman"): {"weight": 211},
         ("Uman", "Odesa"): {"weight": 271}, ("Kyiv", "Poltava"): {"weight": 351},
         ("Poltava", "Kharkiv"): {"weight": 143}, ("Kharkiv", "Dnipro"): {"weight": 221},
         ("Dnipro", "Zaporizhzhya"): {"weight": 85}, ("Dnipro", "Kryvyi Rih"): {"weight": 146},
         ("Kryvyi Rih", "Mykolayiv"): {"weight": 182}, ("Mykolayiv", "Kherson"): {"weight": 68},
         ("Mykolayiv", "Odesa"): {"weight": 135}, ("Uman", "Vinnytsya"): {"weight": 160},
         ("Vinnytsya", "Khmelnytskyi"): {"weight": 121}, ("Khmelnytskyi", "Ternopil"): {"weight": 112},
         ("Ternopil", "Lviv"): {"weight": 128}
         }

G = nx.Graph()
for edge, attributes in roads.items():
    G.add_edge(*edge, **attributes)


def dijkstra(G, start):
    distances = {vertex: float('infinity') for vertex in G}
    distances[start] = 0
    dist_vert = [(0, start)]

    while dist_vert:
        cur_dis, cur_vert = heapq.heappop(dist_vert)

        if cur_dis > distances[cur_vert]:
            continue

        for neighbor, weight in G[cur_vert].items():
            distance = cur_dis + weight["weight"]
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(dist_vert, (distance, neighbor))

    return distances


print(dijkstra(G, "Lviv"))
