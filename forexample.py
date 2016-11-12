import gisclass

hos1 = gisclass.House(2, 3);
hos2 = gisclass.House(4, 3);
hpa1 = gisclass.Hospital(3, 2);
sch = gisclass.School(5, 1);
edif1 = gisclass.Edification(1, 1);
edif2 = gisclass.Edification(1, 2);

edif = edif1 + edif2 + hos1 + hos2 + hpa1 + sch;

for e in edif.elements('house'):
    print e;
