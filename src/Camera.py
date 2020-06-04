class Camera:
    def __init__(self, pos, sight, zoom):
        self.pos=pos# use np array
        self.sight=sight# use np array
        self.zoom=zoom# gama angle
    
    def move(self, step):
        self.pos+=step
    
    def turn(self, angles):
        self.sight+=angles
    
    def rotate_points(self, points):
        rotation_angles=(-self.sight[0], -self.sight[1], -self.sight[2])
        npoints=[point.get_rotated_coor(rotation_angles) for point in points]
        return npoints
    
    def move_points(self, points):
        step=-self.pos
        npoints=[point.get_moved_coor(step) for point in points]
        return npoints
    
    def get_visible_points(self, points):
        npoints=[]
        for point in points:
            if point.is_visible(self.zoom):
                npoints.append(point)
        return npoints
    
    def project(self, point):
        f=1/math.sin(np.radians(self.zoom))
        x,y,z=point
        xl=f*x/z
        yl=f*y/z
        return (xl,yl)
    
    def project_points(self, points):
        npoints=[self.project(point) for point in points]
        return npoints
            
