from ..algorithm_factory import CentralizedAlgorithmFactory
from ..common_import import (AggregationServer, AggregationWorker,
                             FedAVGAlgorithm)

CentralizedAlgorithmFactory.register_algorithm(
    algorithm_name="fed_avg",
    client_cls=AggregationWorker,
    server_cls=AggregationServer,
    algorithm_cls=FedAVGAlgorithm,
)
