from exceptions import InvalidFieldException
from services.segmento_service import get_segmentos_ativos
from util.graph.Graph import Graph, dijkstra_algorithm, get_rota_segmentos
from util.validator import validate_rota_params


def get_rota(params: dict) -> list[dict]:

    if validate_rota_params(params):
        nodes = []
        segmentos = get_segmentos_ativos()

        for segmento in segmentos:
            if segmento['ponto_inicial'] not in nodes:
                nodes.append(segmento['ponto_inicial'])
            elif segmento['ponto_final'] not in nodes:
                nodes.append(segmento['ponto_final'])

        init_graph = {}
        for node in nodes:
            init_graph[node] = {}

        for segmento in segmentos:
            init_graph[segmento['ponto_inicial']][segmento['ponto_final']] = segmento['distancia']

        graph = Graph(nodes, init_graph)

        previous_nodes = dijkstra_algorithm(graph, params['origem'])

        return get_rota_segmentos(previous_nodes, params['origem'], params['destino'])
    else:
        raise InvalidFieldException("rota")
