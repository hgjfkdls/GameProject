from .Component import Component


class System(object):
    """ identifica un juego de componentes y determina como deben ser procesados """

    Catalog = dict()

    def __new__(cls, name=None, components=[]):
        cls.name = cls.__name__ if name is None else name
        if name not in System.Catalog:
            system = super(System, cls).__new__(cls)
            System.Catalog[name] = system
        else:
            system = System.Catalog[name]
        return system

    def __init__(self, name=None, components=[]):
        super(System, self).__init__()
        self.name = name
        if components:
            self.components = components

    @staticmethod
    def init_all():
        """ Inicializa todos los sistemas """
        for k in System.Catalog:
            System.Catalog[k].init()

    @staticmethod
    def update_all(dt=None):
        """ Actualiza todos los sistemas """
        for k in System.Catalog:
            System.Catalog[k].update(dt)

    def init(self):
        raise NotImplemented('el método "init" no se encuentra implementado.')

    def update(self, dt=None):
        raise NotImplemented('el método "update" no se encuentra implementado.')

    @property
    def entities(self):
        return list(set(entity
                        for component_cls in self.component_classes
                        for entity in component_cls.Catalog.keys()
                        if entity is not None))

    @property
    def exclusive_entities(self):
        return list(set(entity
                        for component_cls in self.component_classes
                        for entity in component_cls.Catalog.keys()
                        if entity is not None))

    @property
    def component_classes(self):
        return list(set(Component.ComponentTypes.get(component_name)
                        for component_name in self.components
                        if component_name in Component.ComponentTypes))

    def __repr__(self):
        """ <System name> """
        cname = self.__class__.__name__
        name = self.name
        return '<{} {}>'.format(cname, name)
