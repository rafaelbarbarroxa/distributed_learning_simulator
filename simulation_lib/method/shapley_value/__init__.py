from ..algorithm_factory import CentralizedAlgorithmFactory
from ..common_import import AggregationWorker
from .GTG_shapley_value_server import GTGShapleyValueServer
from .multiround_shapley_value_server import MultiRoundShapleyValueServer

CentralizedAlgorithmFactory.register_algorithm(
    algorithm_name="multiround_shapley_value",
    client_cls=AggregationWorker,
    server_cls=MultiRoundShapleyValueServer,
)
CentralizedAlgorithmFactory.register_algorithm(
    algorithm_name="GTG_shapley_value",
    client_cls=AggregationWorker,
    server_cls=GTGShapleyValueServer,
)
