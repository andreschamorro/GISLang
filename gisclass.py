"""ICOM 3046 Programming Languaget
"""
class Edification(object):
    def __init__ (self, x = 0, y = 0):
        self.x = x;
        self.y = y;
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
                temp_str += str(edif.x) + ',' + str(edif.y) + '\n' ;
        return temp_str[:-1];
    def elements(self, key):
        if key in self.edifications:
            return iter(self.edifications[key]);
        else:
            return iter([]);

class House(Edification):
    def __init__ (self, x = 0, y = 0):
        self.x = x;
        self.y = y;
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
    def __init__ (self, x = 0, y = 0):
        self.x = x;
        self.y = y;
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
    def __init__ (self, x = 0, y = 0):
        self.x = x;
        self.y = y;
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
    def __init__ (self, x = 0, y = 0):
        self.x = x;
        self.y = y;
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
    def __init__ (self, x = 0, y = 0):
        self.x = x;
        self.y = y;
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
                temp_str += str(edif.x) + ',' + str(edif.y) + '\n' ;
        return temp_str[:-1];
    def elements(self, key):
        if key in self.edifications:
            return iter(self.edifications[key]);
        else:
            return iter([]);

#Agregue la clase Point y la Clase Line

class Point(object):

    def __init__(self, x, y,label = "NONAME"):
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
        print perimeter
        return perimeter



class Line(object):

    def __init__(self, puntos, label = "NoName"):
        self.Puntos = puntos
        self.label = label

    def __add__(self, other):
        self.Puntos.append(other)

    def Print(self):
        for x in self.Puntos:
            print x

class Block(Edification,Region):

    def __init__(self,edificaciones, limites, label = "NONAME"):
        self.Viviendas = edificaciones
        self.Limites = Region(limites)
        self.Label = label

    def __add__(self, other):
        self.Viviendas.append(other)

    def Print(self):
        for edi in self.Viviendas:
            edi.Print()
        Limites.Print()

class Neighborhoood(Block,Region):

    def __init__(self, bloques, limites, label = "NONAME"):
        self.Bloques = bloques
        self.Limites = Region(limites)
        self.Label = label

    def __add__(self, other):
        self.Bloques.append(other)



class Town(Neighborhoood,Region):

    def __init__(self, vecindarios, limites, label = "NONAME"):
        self.Vecindarios = vecindarios
        self.Limites = Region(limites)
        self.Label = label

    def __add__(self, other):
        self.Vecindarios.append(other)


class State(Town,Region):

    def __init__(self, ciudades, limites, label = "NONAME"):
        self.Ciudadades = ciudades
        self.Limites = Region(limites)
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
        print perimeter
        return perimeter

class River(Line):

    def __init__(self, puntosA, puntosB, label = "NoName"):
        self.ladoA = Line(puntosA)
        self.ladoB = Line(puntosB)
        self.label = label
        self.n = len(puntosA)
        
        
