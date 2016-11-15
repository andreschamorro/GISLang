"""ICOM 3046 Programming Languaget
"""
import math

class Point(object):

    def __init__(self, x = 0, y = 0, label = "NONAME"):
        self.X = x
        self.Y = y
        self.L = label

    def __str__(self):
        return "Point(%s,%s,%s)"%(self.X, self.Y,self.L)

    def move(self, dx, dy):
        self.X = self.X + dx
        self.Y = self.Y + dy

    def Distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.sqrt(dx**2 + dy**2)

class Line(object):

    def __init__(self, puntos, label = "NoName"):
        self.Puntos = puntos
        self.label = label

    def __add__(self, other):
        self.Puntos.append(other)

    def __str__(self):
        s = ''
        for x in self.Puntos:
            s += x.__str__()
        return s

    def Print(self):
        for x in self.Puntos:
            print (x)

class Edification(object):
    def __init__ (self, point = Point()):
        self.point = point;
        self.key = 'edification'
        self.edifications = {'edification' : [self]};
    def __add__(self, other):
        edif_temp = self;
        if other.key in edif_temp.edifications:
            edif_temp.edifications[other.key].append(other);
        else:
            edif_temp.edifications[other.key] = [other];
        return edif_temp;
    def __str__(self):
        temp_str = '';
        for keys in self.edifications:
            temp_str += keys.title() + '\n';
            for edif in self.edifications[keys]:
                temp_str += str(edif.point.X) + ',' + str(edif.point.Y) + '\n' ;
        return temp_str[:-1];
    def elements(self, key):
        if key in self.edifications:
            return iter(self.edifications[key]);
        else:
            return iter([]);

class House(Edification):
    def __init__ (self, point = Point()):
        self.point = point;
        self.key = 'house'
        self.edifications = {'house' : [self]};
    def __add__(self, other):
        hos_temp = self;
        if other.key in hos_temp.edifications:
            hos_temp.edifications[other.key].append(other);
        else:
            hos_temp.edifications[other.key] = [other];
        return hos_temp;

class School(Edification):
    def __init__ (self, point = Point()):
        self.point = point;
        self.key = 'school'
        self.edifications = {'school' : [self]};
    def __add__(self, other):
        hos_temp = self;
        if other.key in hos_temp.edifications:
            hos_temp.edifications[other.key].append(other);
        else:
            hos_temp.edifications[other.key] = [other];
        return hos_temp;

class Hospital(Edification):
    def __init__ (self, point = Point()):
        self.point = point;
        self.key = 'hospital'
        self.edifications = {'hospital' : [self]};
    def __add__(self, other):
        hos_temp = self;
        if other.key in hos_temp.edifications:
            hos_temp.edifications[other.key].append(other);
        else:
            hos_temp.edifications[other.key] = [other];
        return hos_temp;

class Commercial(Edification):
    def __init__ (self, point = Point()):
        self.point = point;
        self.key = 'commercial'
        self.edifications = {'commercial' : [self]};
    def __add__(self, other):
        hos_temp = self;
        if other.key in hos_temp.edifications:
            hos_temp.edifications[other.key].append(other);
        else:
            hos_temp.edifications[other.key] = [other];
        return hos_temp;

class Street(object):
    def __init__ (self, point = Point()):
        self.point = point;
        self.key = 'street'
        self.edifications = {'street' : [self]};
    def __add__(self, other):
        edif_temp = self;
        if other.key in edif_temp.edifications:
            edif_temp.edifications[other.key].append(other);
        else:
            edif_temp.edifications[other.key] = [other];
        return edif_temp;
    def __str__(self):
        temp_str = '';
        for keys in self.edifications:
            temp_str += keys.title() + '\n';
            for edif in self.edifications[keys]:
                temp_str += str(edif.point.X) + ',' + str(edif.point.Y) + '\n' ;
        return temp_str[:-1];

    def Print(self):
        print(self.__str__)

    def elements(self, key):
        if key in self.edifications:
            return iter(self.edifications[key]);
        else:
            return iter([]);

class Region(object):

    def __init__(self, puntos, label = "NoName"):
        self.Puntos = puntos
        self.label = label
        self.n = len(puntos)

    def __add__(self, other):
        self.Puntos.append(other)

    def Print(self):
        for punto in self.Puntos:
            print (punto.X,punto.Y)

    def Perimeter(self):
        perimeter = 0
        for x in range(-1,self.n-1):
            perimeter = perimeter + self.Puntos[x].Distance(self.Puntos[x+1])
        print(perimeter)
        return perimeter

class Block(Region):

    def __init__(self,edificaciones, limites, label = "NONAME"):
        self.Viviendas = edificaciones
        self.Limites = limites
        self.Label = label

    def __add__(self, other):
        self.Viviendas.append(other)

    def Print(self):
        for edi in self.Viviendas:
            edi.Print()
        self.Limites.Print()

class Neighborhoood(Region):

    def __init__(self, bloques, limites, label = "NONAME"):
        self.Bloques = bloques
        self.Limites = limites
        self.Label = label

    def __add__(self, other):
        self.Bloques.append(other)



class Town(Region):

    def __init__(self, vecindarios, limites, label = "NONAME"):
        self.Vecindarios = vecindarios
        self.Limites = limites
        self.Label = label

    def __add__(self, other):
        self.Vecindarios.append(other)


class State(Region):

    def __init__(self, ciudades, limites, label = "NONAME"):
        self.Ciudadades = ciudades
        self.Limites = limites
        self.Label = label

    def __add__(self, other):
        self.Ciudadades.append(other)


class Lake(object):

    def __init__(self, puntos, label = "NoName"):
        self.Puntos = puntos
        self.label = label
        self.n = len(puntos)

    def __add__(self, other):
        self.Puntos.append(other)

    def Print(self):
        for punto in self.Puntos:
            print (punto.X,punto.Y)

    def Perimeter(self):
        perimeter = 0
        for x in range(-1,self.n-1):
            perimeter = perimeter + self.Puntos[x].Distance(self.Puntos[x+1])
        print (perimeter)
        return perimeter

class River(object):

    def __init__(self, ladoa, ladob, label = "NoName"):
        self.ladoA = ladoa
        self.ladoB = ladob
        self.label = label
