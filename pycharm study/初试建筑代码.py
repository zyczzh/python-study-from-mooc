"""

design team : Geongu Lee, HyeJi Yang

FORM AND ALGORITHM, PennDesign 2014

Instructor: Cecil Balmond, Ezio Blasetti

code developed in python for rhinoceros beta 5.0

"""
import rhinoscriptsyntax
import scriptcontext


class Turtle():
    def __init__(self, PLANE, TYPE):

        self.pos = PLANE[0]

        self.vec = PLANE[1]

        self.plane = PLANE

        self.type = TYPE

        self.state = True

    def move(self, myTurtles):

        if self.state:

            tempPos = rs.PointAdd(self.pos, self.vec)

            pts = []

            for otherTurtle in myTurtles:

                if otherTurtle.pos != self.pos:
                    pts.append(otherTurtle.pos)

            if len(pts) > 0:

                index = rs.PointArrayClosestPoint(pts, tempPos)

                clOtherTurtlePos = pts[index]

                otherTurtle = myTurtles[index]

                dist = rs.Distance(tempPos, clOtherTurtlePos)

                if dist < .9:
                    tempPos = clOtherTurtlePos

                    self.vec = rs.VectorCreate(tempPos, self.pos)

                    # vec = rs.VectorCreate(clOtherTurtlePos,self.pos)

                    # length = rs.VectorLength(self.vec)

                    # self.vec = rs.VectorUnitize(vec)

                    # self.vec = rs.VectorScale(self.vec,length)

                    # if tempPos!=rs.PointAdd(self.pos,self.vec):

                    #    rs.AddLine(tempPos,rs.PointAdd(self.pos,self.vec))

                    # self.vec = vec

                    otherTurtle.state = False

            if tempPos != self.pos:
                self.id = rs.AddLine(self.pos, tempPos)

            self.pos = tempPos

            # rs.AddTextDot(self.type,self.pos)

            xform = rs.XformTranslation(self.vec)

            self.plane = rs.PlaneTransform(self.plane, xform)

    def branch(self):

        # define how to make branch(selecting two planes -> changing the angle, the scale)

        newTurtles = []

        if self.state:

            if self.type == "A":
                newTurtles.append(Turtle(self.plane, "B"))

            if self.type == "B":
                newTurtles.append(Turtle(self.plane, "C"))

                myZ = self.plane[3]

                myY = self.plane[2]

                xform = rs.XformRotation2(360, myZ, self.pos)

                newPlane = rs.PlaneTransform(self.plane, xform)

                # xform = rs.XformRotation2(0, newPlane[2], self.pos)

                newPlane = rs.PlaneTransform(newPlane, xform)

                # newPlane = self.plane

                newTurtles.append(Turtle(newPlane, "A"))

                # xform = rs.XformRotation2(-80, myZ, self.pos)

            if self.type == "C":
                myZ = self.plane[3]

                myY = self.plane[2]

                xform = rs.XformRotation2(90, myZ, self.pos)

                newPlane = rs.PlaneTransform(self.plane, xform)

                xform = rs.XformRotation2(120, newPlane[2], self.pos)

                newPlane = rs.PlaneTransform(newPlane, xform)

                newTurtles.append(Turtle(newPlane, "A"))

                xform = rs.XformRotation2(-145, myZ, self.pos)

                newPlane = rs.PlaneTransform(self.plane, xform)

                newTurtles.append(Turtle(newPlane, "B"))

            return newTurtles

        else:

            return None


def Main():
    myTurtle = Turtle(rs.WorldXYPlane(), "A")

    myTurtles = []

    myTurtles.append(myTurtle)

    for i in range(17):

        if sc.escape_test(): break

        rs.EnableRedraw(False)

        newTurtles = []

        for myTurtle in myTurtles:

            if myTurtle.state:

                myTurtle.move(myTurtles)

                newTs = myTurtle.branch()

                if newTs != None:
                    newTurtles.extend(newTs)

                myTurtle.state = False

        myTurtles.extend(newTurtles)

        rs.EnableRedraw(True)

    print
    "jdrt"


Main()