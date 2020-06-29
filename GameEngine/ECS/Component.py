import json


class Component(object):
    """ class Component(object):
    - encapsula un componente el cual puede ser utilizado por
      una entidad [Entity]
    """

    __slots__ = ['entity']

    defaults = dict()
    Catalog = dict()
    ComponentTypes = dict()

    def __new__(cls, entity=None, **properties):
        cname = cls.__name__
        if cname not in Component.ComponentTypes:
            Component.ComponentTypes[cname] = cls
            cls.Catalog = dict()
        if entity is not None:
            if entity not in cls.Catalog:
                component = super(Component, cls).__new__(cls)
                cls.Catalog[entity] = component
            else:
                component = cls.Catalog[entity]
        else:
            component = super(Component, cls).__new__(cls)
        return component

    def __init__(self, entity=None, **properties):
        self.entity = entity
        for prop, value in self.defaults.items():
            setattr(self, prop, properties.get(prop, value))
            # setattr(self, prop, properties[prop])

    def reset(self):
        for prop_name, value in self.defaults.items():
            setattr(self, prop_name, value)

    def __hash__(self):
        return (hash(self.Catalog) ^
                hash(self.ComponentTypes) ^
                hash(self.defaults) ^
                hash(self.entity) ^
                hash(self)
                )

    def __iter__(self):
        for prop in self.defaults:
            yield prop

    def __repr__(self):
        cname = self.__class__.__name__
        entity_name = ''
        if self.entity:
            for prop_name, component in self.entity.components.items():
                if component == self:
                    entity_name = ' entity:{}.{}'.format(
                        self.entity.name, prop_name)
                    break
        return '<{}{}>'.format(cname, entity_name)

    def __str__(self):
        keys = self.defaults.keys()
        data = dict()
        for key in keys:
            if key != 'defaults':
                data[key] = getattr(self, key)
        json_string = '\n'.join(
            line.rstrip()
            for line in json.dumps(data, indent=4).split('\n')
        )
        return json_string

    def __getitem__(self, key):
        """ permite acceder a los atributos mediante un diccionario """
        return getattr(self, key)

    def __setitem__(self, key, value):
        """ permite acceder a los atributos mediante un diccionario """
        return setattr(self, key, value)

    def __del__(self):
        """ remueve las relaciones de la entidad """
        if self.entity:
            for attr, component in self.entity.components.items():
                if component == self:
                    self.entity.components.pop(attr)
                    break
        if self.entity in self.__class__.Catalog:
            self.__class__.Catalog.pop(self.entity)
