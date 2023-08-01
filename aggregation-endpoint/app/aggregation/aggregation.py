from .consumer import Consumer

param = {"recipient": "https://edge-contributor-1:8080/api/ids/data"}


def edgeNodeConsumer(port):
    try:
        consumer = Consumer(port, param)

        consumer.getCatalogs()
        consumer.getCurrentCatalog(consumer.catalogs)
        consumer.getResources()
        consumer.getArtifacts()
        consumer.negotiateContract()
        consumer.getNegotiatedArtifacts()

        return consumer.data
    except:
        return None
