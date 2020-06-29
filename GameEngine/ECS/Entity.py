from .Component import Component
from uuid import uuid4


class Entity(object):
    """ class Entity(object):

    - define una entidad.
    - por defecto tiene los atributos ('name' y 'uid').
    - contiene componentes que pueden ser creados en tiempo de ejecución.
    - se puede acceder a los componentes mediante atributos o items.
    - las entidades tienen una relacion con sus componentes.
    """

    __slots__ = ['uid', 'name', 'components', '__components_type']

    Catalog = dict()

    def __new__(cls, name=None, uid=None):
        if name not in cls.Catalog:
            entity = super(Entity, cls).__new__(cls)
            cls.Catalog[name] = entity
        else:
            entity = cls.Catalog[name]
        return entity

    def __init__(self, name=None, uid=None):
        self.uid = uuid4() if uid is None else uid
        self.name = name or ''
        self.components = dict()
        self.__components_type = dict()

    def __repr__(self):
        """ <Entity player:0> """
        cname = self.__class__.__name__
        name = self.name or self.uid
        if name != self.uid:
            name = '{}:{}'.format(self.name, self.uid)
        return '<{} {}>'.format(cname, name)

    def __str__(self):
        """ TODO: Esto se puede hacer mejor """
        return str(self.components)

    def __hash__(self):
        return hash(self.uid)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.uid == other.uid
        elif isinstance(other, self.uid.__class__):
            return self.uid == other

    def __getitem__(self, key):
        """ retorna el componente segun la clave"""
        return self.components[key]

    def __setitem__(self, key, value):
        """ asigna un componente mediante Entity[key] """
        if isinstance(value, Component):
            vCatalog = value.__class__.Catalog
            if value.entity is not self:
                value.entity = self
                for entity, component in vCatalog.items():
                    if component == value:
                        if entity in vCatalog:
                            vCatalog.pop(entity)
                vCatalog[self] = value
        self.__components_type[value.__class__] = value
        self.components[key] = value

    def __getattr__(self, key):
        """ permite el acceso a las propiedades o componentes"""
        if key in super(Entity, self).__getattribute__('__slots__'):
            return super(Entity, self).__getattr__(key)
        else:
            return self.components[key]

    def __setattr__(self, key, value):
        """ permite el acceso a las propiedades o componentes mediante atributos """
        if key in super(Entity, self).__getattribute__('__slots__'):
            super(Entity, self).__setattr__(key, value)
        else:
            """ si el valor es un componente, la entidad se guarda en el catago """
            if isinstance(value, Component):
                print(value.__class__)
                vCatalog = value.__class__.Catalog
                if value.entity is not self:
                    value.entity = self
                    for entity, comp in vCatalog.items():
                        if comp == value:
                            if entity in vCatalog:
                                vCatalog.pop(entity)
                    vCatalog[self] = value
            self.components[key] = value
            self.__components_type[value.__class__] = value

    def get_component(self, type_component):
        if type_component not in self.__components_type:
            return None
        return self.__components_type[type_component]
