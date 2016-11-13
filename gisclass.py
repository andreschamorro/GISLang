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
