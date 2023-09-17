import mt

class Intercept(object):
    def __init__(self,distance,point,normal,obj):
        self.distance=distance
        self.point=point
        self.normal=normal
        self.obj=obj
        

class Shape(object):
    def __init__(self,position,material):
        self.position = position
        self.material = material

    def ray_intersect(self,orig,dir):
        return None
    
class Sphere(Shape):
    def __init__(self,position,radius,material):
        self.radius = radius
        super().__init__(position,material)
        
    def ray_intersect(self,orig,dir):
        L = mt.subtract_arrays(self.position,orig)
        lengthL = mt.calcular_norma(L)
        tca = mt.producto_punto(L,dir)
        d = (lengthL**2-tca**2)**0.5
        
        if d>self.radius:
            return None
        
        thc = (self.radius**2-d**2)**0.5
        t0 = tca-thc
        t1 = tca+thc
        
        if t0<0:
            t0=t1
        if t0<0:
            return None
        
        P = mt.add_arrays(orig,mt.multiply_scalar_array(t0,dir))
        normal = mt.subtract_arrays(P,self.position)
        normal = mt.normalizar_vector(normal)

        return Intercept(distance=t0,
                         point=P,
                         normal=normal,
                         obj=self)