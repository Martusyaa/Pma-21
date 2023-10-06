from TransportFactory import RedTransportFactory, BlueTransportFactory, create_transport
if __name__ == '__main__':
    red_factory = RedTransportFactory()
    create_transport(red_factory)

    blue_factory = BlueTransportFactory()
    create_transport(blue_factory)